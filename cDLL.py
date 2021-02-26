import ctypes, inspect, threading, os, re;

from .iPrimitiveBaseType import iPrimitiveBaseType;

class cFunctionDoesNotExistException(Exception):
  def __init__(oSelf, sDLLName, sFunctionName):
    oSelf.sDLLName = sDLLName;
    oSelf.sFunctionName = sFunctionName;

class cDLLFunction(object):
  def __init__(
    oSelf,
    sDLLName, 
    oWinDLL,
    xReturnType,
    sFunctionName,
    txArgumentTypes,
    bSingleThreaded
  ):
    oSelf.sDLLName = sDLLName;
    oSelf.xReturnType = xReturnType;
    oSelf.sName = sFunctionName;
    oSelf.txArgumentTypes = txArgumentTypes;
    for uArgumentIndex in xrange(len(txArgumentTypes)):
      xArgumentType = txArgumentTypes[uArgumentIndex];
      assert inspect.isclass(xArgumentType) and issubclass(xArgumentType, iPrimitiveBaseType), (
        "You are trying to define `%s`, `function %s()` with %s as the type of argument #%d.\n" + \
        "This is not a primitive type and cannot be used as an argument.\n" + \
        "Perhaps you forgot to make it a point to this type?"
      ) % (sDLLName, sFunctionName, repr(xArgumentType), uArgumentIndex);
    
    oSelf.bSingleThreaded = bSingleThreaded;
    ffxFunctionConstructor = ctypes.WINFUNCTYPE(oSelf.xReturnType, *oSelf.txArgumentTypes);
    try:
      fxBasicFunctionWrapper = ffxFunctionConstructor(
        (sFunctionName, oWinDLL),
        tuple([(1, "p%d" % u, 0) for u in xrange(len(oSelf.txArgumentTypes))])
      );
    except AttributeError as oException:
      # The DLL does not implement this function.
      raise cFunctionDoesNotExistException(sDLLName, sFunctionName)
    if oSelf.bSingleThreaded:
      # This function cannot be called concurrently from multiple threads: wrap it in a function that holds a lock
      # while a call is in progress. This allows only a single thread to call it at the same time.
      oSelf.oCallLock = threading.Lock();
      def fxSingleThreadedFunctionWrapper(*txArguments):
        oSelf.oCallLock.acquire();
        try:
          return fxBasicFunctionWrapper(*txArguments);
        finally:
          oSelf.oCallLock.release();
      oSelf.__fFunctionWrapper = fxSingleThreadedFunctionWrapper;
    else:
      oSelf.__fFunctionWrapper = fxBasicFunctionWrapper;
    
  def __call__(oSelf, *txArguments):
    try:
      xReturnValue = oSelf.__fFunctionWrapper(*txArguments);
    except ctypes.ArgumentError as oException:
      oArgumentNumberMatch = re.match(r"argument (\d+):.*", oException.message);
      u0WrongArgumentIndex = oArgumentNumberMatch and long(oArgumentNumberMatch.group(1)) - 1;
      print "*" * 80;
      print "* Invalid arguments passed to %s.%s():" % (oSelf.sDLLName, oSelf.sName);
      for uArgumentIndex in xrange(len(txArguments)):
        xArgument = txArguments[uArgumentIndex];
        xExpectedArgumentType = oSelf.txArgumentTypes[uArgumentIndex];
        if (
          xArgument.__class__ != xExpectedArgumentType
            if u0WrongArgumentIndex is None else
          uArgumentIndex == u0WrongArgumentIndex
        ):
          print "- Argument %d is %s (%s), which %s correct." % \
              (uArgumentIndex + 1, repr(xArgument.__class__), repr(xArgument), "may not be" if u0WrongArgumentIndex is None else "is not");
          print "  Expected type = %s." % (repr(xExpectedArgumentType),);
        else:
          print "+ Argument %d is %s (%s) as expected." % \
              (uArgumentIndex + 1, repr(xArgument.__class__), repr(xArgument));
      print "*" * 80;
      raise;
    if oSelf.xReturnType is not None:
      assert type(xReturnValue) == oSelf.xReturnType, \
          "Expected %s to return %s but got %s" % (oSelf.sName, oSelf.xReturnType, repr(xReturnValue));
#      return oSelf.xReturnType(xReturnValue);
    else:
      assert xReturnValue is None, \
          "%s should return None but got %s" % (oSelf.sName, repr(xReturnValue));
    return xReturnValue;
  def __str__(oSelf):
    return "<cDLLFunction(%s!%s)>" % (oSelf.oDLL.sName, oSelf.sName);

gtsValidDefinitionElementNames = ("xReturnType", "txArgumentTypes", "bSingleThreaded");

class cDLL(object):
  def __init__(oSelf, sDLLFilePath, dxFunctions):
    oSelf.__sDLLFilePath = sDLLFilePath;
    oSelf.__oWinDLL = ctypes.WinDLL(sDLLFilePath);
    oSelf.fbAddFunctions(dxFunctions);
  
  def fbAddFunctions(oSelf, dxFunctions):
    bFoundMissingFunctions = False;
    for (sFunctionName, dxDefinitionElements) in dxFunctions.items():
      if not oSelf.fbAddFunction(sFunctionName, dxDefinitionElements):
        bFoundMissingFunctions = True;
    return not bFoundMissingFunctions;
  
  def fbAddFunction(oSelf, sFunctionName, dxDefinitionElements = {}):
    sDLLFileName = os.path.basename(oSelf.__sDLLFilePath);
    for sDefinitionElementName in dxDefinitionElements:
      if (sDefinitionElementName not in gtsValidDefinitionElementNames):
        raise AssertionError(
          "Unknown definition element %s for function %s in DLL %s"
          % (sDefinitionElementName, sFunctionName, sDLLFileName)
        );
    xReturnType = dxDefinitionElements.get("xReturnType");
    txArgumentTypes = dxDefinitionElements.get("txArgumentTypes", tuple());
    if not isinstance(txArgumentTypes, tuple): # Single argument (DWORD) => (DWORD,)
      txArgumentTypes = (txArgumentTypes,);
    bSingleThreaded = dxDefinitionElements.get("bSingleThreaded", False);
    try:
      oDLLFunction = cDLLFunction(
        sDLLFileName,
        oSelf.__oWinDLL,
        xReturnType,
        sFunctionName,
        txArgumentTypes,
        bSingleThreaded
      );
    except cFunctionDoesNotExistException as oException:
      oDLLFunction = None;
    setattr(oSelf, sFunctionName, oDLLFunction);
    return oDLLFunction is not None;
  
  def __repr__(oSelf):
    return "<cDLL %s>" % os.path.basename(sDLLFilePath);
