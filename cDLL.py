import ctypes, threading, os;

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
    oSelf.bSingleThreaded = bSingleThreaded;
    ffxFunctionConstructor = ctypes.WINFUNCTYPE(oSelf.xReturnType, *oSelf.txArgumentTypes);
    fxBasicFunctionWrapper = ffxFunctionConstructor(
      (sFunctionName, oWinDLL),
      tuple([(1, "p%d" % u, 0) for u in xrange(len(oSelf.txArgumentTypes))])
    );
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
    except ctypes.ArgumentError:
      print "*" * 80;
      for uIndex in xrange(len(txArguments)):
        xArgument = txArguments[uIndex];
        xExpectedArgumentType = oSelf.txArgumentTypes[uIndex];
        if xArgument.__class__ != xExpectedArgumentType:
          print "* Argument %d (%s) is type %s instead of type %s." % \
                (uIndex + 1, repr(xArgument), repr(xArgument.__class__), repr(xExpectedArgumentType));
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
    oSelf.__class__.fAddFunctions(oSelf, dxFunctions);
  
  @staticmethod
  def fAddFunctions(oSelf, dxFunctions):
    for (sFunctionName, dxDefinitionElements) in dxFunctions.items():
      oSelf.__class__.fAddFunction(oSelf, sFunctionName, dxDefinitionElements);
  
  @staticmethod
  def fAddFunction(oSelf, sFunctionName, dxDefinitionElements = {}):
    sDLLFileName = os.path.basename(oSelf.__sDLLFilePath);
    oWinDLL = ctypes.WinDLL(oSelf.__sDLLFilePath);
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
    oDLLFunction = cDLLFunction(
      sDLLFileName,
      oWinDLL,
      xReturnType,
      sFunctionName,
      txArgumentTypes,
      bSingleThreaded
    );
    setattr(oSelf, sFunctionName, oDLLFunction);
  
  def __str__(oSelf):
    return "<cDLL(%s)>" % os.path.basename(sDLLFilePath);
