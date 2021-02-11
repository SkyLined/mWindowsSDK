from .mWindowsSDK import *;

__all__ = [
  "cBufferType",
  "cCharacterType",
  "cIntegerType",
  "cFloatType",
  "cPointerType",
  "cStructureType",
  "cUnionType",
  "fsGetStringAtAddress",
  "fcCreatePointerType",
  "foCreateBuffer",
  "fcTypeDefStructure",
  "fcTypeDefStructure32",
  "fcTypeDefStructure64",
  "fcTypeDefUnion",
  "foParseGUID",
  "FAILED",
  "SUCCEEDED",
  "NT_SUCCESS",
  "NT_ERROR",
  "HRESULT_FROM_WIN32",
  "WIN32_FROM_HRESULT",
  "mWindowsDefines",
  "mErrorDefines",
  "mPrimitiveTypes",
  "mStructureTypes",
  "mGUIDs",
  "cDLL",
  "foLoadAdvAPI32DLL",
  "foLoadDbgHelpDLL",
  "foLoadKernel32DLL",
  "foLoadNTDLL",
  "foLoadOle32DLL",
  "foLoadUser32DLL",
  "foLoadWinHTTPDLL",
  "fs0GetErrorDefineName",
];

for mModule in (mWindowsDefines, mErrorDefines, mPrimitiveTypes, mStructureTypes, mGUIDs):
  for sName in dir(mModule):
    if sName[0] != "_":
      globals()[sName] = getattr(mModule, sName);
      __all__.append(sName);
