import importlib;
from .iArrayBaseType import iArrayBaseType;
from .iCharacterBaseType import iCharacterBaseType;
from .mCharacterClasses import \
  cCharacterA, cCharacterW;

# Integer Types
from .iIntegerBaseType import iIntegerBaseType;
from .iBooleanBaseType import iBooleanBaseType;
from .iSignedIntegerBaseType import iSignedIntegerBaseType;
from .iUnsignedIntegerBaseType import iUnsignedIntegerBaseType;
# Integer Classes
from .mBooleanClasses import \
    cBoolean8, cBoolean16, cBoolean32, cBoolean64, cBoolean;
from .mSignedIntegerClasses import \
    cSignedInteger8, cSignedInteger16, cSignedInteger32, cSignedInteger64, cSignedInteger;
from .mUnsignedIntegerClasses import \
    cUnsignedInteger8, cUnsignedInteger16, cUnsignedInteger32, cUnsignedInteger64, cUnsignedInteger;
# Floating Types
from .iFloatingPointBaseType import iFloatingPointBaseType;
# Floating Classes
from .mFloatingPointClasses import \
    cFloatingPoint32, cFloatingPoint64;
# Pointer Types
from .iPointerBaseType import iPointerBaseType
from .mPointerTypes import \
    iPointerType, iPointerType32, iPointerType64;
# Pointer Classes
from .mPointerClasses import \
    cVoidPointer32, cVoidPointer64, cVoidPointer, \
    cVoidPointerPointer32, cVoidPointerPointer64, cVoidPointerPointer;
# Structure Types
from .iStructureBaseType import iStructureBaseType;
from .mStructureTypes import \
  iStructureType8, iStructureType16, iStructureType32, iStructureType64, iStructureType;
# Union Types
from .iUnionBaseType import iUnionBaseType;
from .mUnionTypes import \
  iUnionType8, iUnionType16, iUnionType32, iUnionType64, iUnionType;

from .fsGetStringAtAddress import fsGetStringAtAddress;

from .STRUCT import STRUCT;
from .UNION import UNION;

from .cDLL import cDLL;

from .foLoadAdvAPI32DLL import foLoadAdvAPI32DLL;
from .foLoadDbgHelpDLL import foLoadDbgHelpDLL;
from .foLoadNTDLL import foLoadNTDLL;

from .fs0GetHResultDefineName import fs0GetHResultDefineName;
from .fsGetHResultDescription import fsGetHResultDescription;
from .fs0GetNTStatusDefineName import fs0GetNTStatusDefineName;
from .fsGetNTStatusDescription import fsGetNTStatusDescription;
from .fs0GetWin32ErrorCodeDefineName import fs0GetWin32ErrorCodeDefineName;
from .fsGetWin32ErrorCodeDescription import fsGetWin32ErrorCodeDescription;
from .fs0GetExceptionDefineName import fs0GetExceptionDefineName;
from .fsGetExceptionDescription import fsGetExceptionDescription;

__all__ = [
  # Base Types
  "iArrayBaseType",
  "iBooleanBaseType",
  "iCharacterBaseType",
  "iFloatingPointBaseType",
  "iIntegerBaseType",
  "iPointerBaseType",
  "iSignedIntegerBaseType",
  "iStructureBaseType",
  "iUnionBaseType",
  "iUnsignedIntegerBaseType",
  # Base Types with size/alignment defined.
  "iPointerType",
  "iPointerType32",
  "iPointerType64",
  "iStructureType",
  "iStructureType8",
  "iStructureType16",
  "iStructureType32",
  "iStructureType64",
  "iUnionType",
  "iUnionType8",
  "iUnionType16",
  "iUnionType32",
  "iUnionType64",
  # Type Classes
  "cBoolean",
  "cBoolean8",
  "cBoolean16",
  "cBoolean32",
  "cBoolean64",
  "cCharacterA",
  "cCharacterW",
  "cFloatingPoint32",
  "cFloatingPoint64",
  "cSignedInteger",
  "cSignedInteger8",
  "cSignedInteger16",
  "cSignedInteger32",
  "cSignedInteger64",
  "cUnsignedInteger",
  "cUnsignedInteger8",
  "cUnsignedInteger16",
  "cUnsignedInteger32",
  "cUnsignedInteger64",
  "cVoidPointerPointer",
  "cVoidPointerPointer32",
  "cVoidPointerPointer64",
  "cVoidPointer",
  "cVoidPointer32",
  "cVoidPointer64",
  # Structure/Union helper classes
  "STRUCT",
  "UNION",
  # DLL base class
  "cDLL",
  
  # Miscellaneous stuff
  "fsGetStringAtAddress",
  
  # Windows specific stuff
  "mWindowsConstants",
  "mWindowsMacros",
  "mWindowsPrimitiveTypes",
  "mWindowsStructures",
  # Windows DLL loaders
  "foLoadAdvAPI32DLL",
  "foLoadDbgHelpDLL",
  "foLoadNTDLL",
  
  "fs0GetHResultDefineName",
  "fsGetHResultDescription",
  "fs0GetNTStatusDefineName",
  "fsGetNTStatusDescription",
  "fs0GetWin32ErrorCodeDefineName",
  "fsGetWin32ErrorCodeDescription",
  "fs0GetExceptionDefineName",
  "fsGetExceptionDescription",
];
dsSourceModuleName_by_sExportName = {};
for sModuleName in ("mWindowsConstants", "mWindowsMacros", "mWindowsPrimitiveTypes", "mWindowsStructures"):
  mModule = importlib.import_module(".%s" % sModuleName, "mWindowsSDK");
  globals()[sModuleName] = mModule;
  __all__.append(sModuleName);
  assert hasattr(mModule, "__all__"), \
      "%s does not have an __all__ list defined!" % sModuleName;
  for sExportName in mModule.__all__:
    assert sExportName not in __all__, \
        "Cannot define %s twice in %s and %s!" % (sExportName, dsSourceModuleName_by_sExportName.get(sExportName, "<module>"), sModuleName);
    globals()[sExportName] = getattr(mModule, sExportName);
    __all__.append(sExportName);
    dsSourceModuleName_by_sExportName[sExportName] = sModuleName;
