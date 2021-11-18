import ctypes, inspect, threading, os, re;

from .iPrimitiveBaseType import iPrimitiveBaseType;

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
    for uArgumentIndex in range(len(txArgumentTypes)):
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
        tuple([(1, "p%d" % u, 0) for u in range(len(oSelf.txArgumentTypes))])
      );
    except AttributeError as oException:
      # The DLL does not implement this function.
      raise cDLL.cFunctionDoesNotExistException(sDLLName, sFunctionName)
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
      oArgumentNumberMatch = re.match(r"argument (\d+):.*", oException.args[0]);
      u0WrongArgumentIndex = oArgumentNumberMatch and int(oArgumentNumberMatch.group(1)) - 1;
      aoArgumentDetails = [];
      uMaxArguments = max(len(oSelf.txArgumentTypes), len(txArguments));
      for uArgumentIndex in range(uMaxArguments):
        sStatusChar = " ";
        xProvidedValue = txArguments[uArgumentIndex] if uArgumentIndex < len(txArguments) else None;
        cExpectedType = oSelf.txArgumentTypes[uArgumentIndex] if uArgumentIndex < len(oSelf.txArgumentTypes) else None;
        aoArgumentDetails.append(cDLL.cFunctionArgumentDetails(
          uArgumentIndex,
          xProvidedValue,
          cExpectedType,
        ));
      uNumberOfProvidedArguments = len(txArguments);
      uNumberOfExpectedArguments = len(oSelf.txArgumentTypes);
      if uNumberOfProvidedArguments < uNumberOfExpectedArguments:
        sMessage = "missing %d arguments" % (uNumberOfExpectedArguments - uNumberOfProvidedArguments,);
      elif uNumberOfProvidedArguments > uNumberOfExpectedArguments:
        sMessage = "provided %d superfluous arguments" % (uNumberOfProvidedArguments - uNumberOfExpectedArguments,);
      elif u0WrongArgumentIndex is not None:
        sMessage = "provided invalid argument #%d: type is %s:%s instead of %s:%s" % (
          u0WrongArgumentIndex + 1,
          txArguments[u0WrongArgumentIndex].__class__.__module__, txArguments[u0WrongArgumentIndex].__class__.__name__,
          oSelf.txArgumentTypes[u0WrongArgumentIndex].__module__, oSelf.txArgumentTypes[u0WrongArgumentIndex].__name__,
        );
      else:
        sMessage = "provided invalid arguments";
      sMessage += " in call to function %s in DLL %s" % (oSelf.sName, oSelf.sDLLName);
      mDebugOutput_HideInCallStack = True;
      raise cDLL.cInvalidFunctionArgumentsException(
        sMessage,
        oSelf.sDLLName,
        oSelf.sName,
        uNumberOfProvidedArguments,
        uNumberOfExpectedArguments,
        u0WrongArgumentIndex,
        aoArgumentDetails,
      );
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
  class cFunctionDoesNotExistException(Exception):
    def __init__(oSelf, sDLLName, sFunctionName):
      oSelf.sDLLName = sDLLName;
      oSelf.sFunctionName = sFunctionName;

  class cFunctionArgumentDetails(object):
    def __init__(oSelf, uIndex, xProvidedValue, cExpectedType):
      oSelf.uIndex = uIndex;
      oSelf.xProvidedValue = xProvidedValue;
      oSelf.cExpectedType = cExpectedType;
      
  class cInvalidFunctionArgumentsException(Exception):
    def __init__(oSelf,
      sMessage,
      sDLLName,
      sFunctionName,
      uNumberOfProvidedArguments,
      uNumberOfExpectedArguments,
      u0WrongArgumentIndex,
      aoArgumentDetails,
    ):
      oSelf.sMessage = sMessage;
      oSelf.sDLLName = sDLLName;
      oSelf.sFunctionName = sFunctionName;
      oSelf.uNumberOfProvidedArguments = uNumberOfProvidedArguments;
      oSelf.uNumberOfExpectedArguments = uNumberOfExpectedArguments;
      oSelf.u0WrongArgumentIndex = u0WrongArgumentIndex;
      oSelf.aoArgumentDetails = aoArgumentDetails;
      super().__init__(sMessage);
  
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
    except cDLL.cFunctionDoesNotExistException as oException:
      oDLLFunction = None;
    setattr(oSelf, sFunctionName, oDLLFunction);
    return oDLLFunction is not None;
  
  def __repr__(oSelf):
    return "<cDLL %s>" % os.path.basename(sDLLFilePath);
