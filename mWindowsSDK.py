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

from .foParseGUID import foParseGUID;

from .STRUCT import STRUCT;
from .UNION import UNION;

from . import mWindowsMacros;
from . import mWindowsConstants;
from . import mWindowsPrimitives;
from . import mWindowsStructures;
from . import mWindowsGUIDs;

from .cDLL import cDLL;

from .foLoadAdvAPI32DLL import foLoadAdvAPI32DLL;
from .foLoadDbgHelpDLL import foLoadDbgHelpDLL;
from .foLoadKernel32DLL import foLoadKernel32DLL;
from .foLoadNTDLL import foLoadNTDLL;
from .foLoadOle32DLL import foLoadOle32DLL;
from .foLoadUser32DLL import foLoadUser32DLL;
from .foLoadWinHTTPDLL import foLoadWinHTTPDLL;

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
  # DLL base class
  "cDLL",
  
  # Miscelanious stuff
  "fsGetStringAtAddress",
  
  "foParseGUID",
  # Windows specific stuff
  "mWindowsConstants",
  "mWindowsGUIDs",
  "mWindowsMacros",
  "mWindowsPrimitives",
  "mWindowsStructures",
  # Windows DLL loaders
  "foLoadAdvAPI32DLL",
  "foLoadDbgHelpDLL",
  "foLoadKernel32DLL",
  "foLoadNTDLL",
  "foLoadOle32DLL",
  "foLoadUser32DLL",
  "foLoadWinHTTPDLL",
  
  "fs0GetHResultDefineName",
  "fsGetHResultDescription",
  "fs0GetNTStatusDefineName",
  "fsGetNTStatusDescription",
  "fs0GetWin32ErrorCodeDefineName",
  "fsGetWin32ErrorCodeDescription",
  "fs0GetExceptionDefineName",
  "fsGetExceptionDescription",
];

for mModule in (mWindowsConstants, mWindowsGUIDs, mWindowsMacros, mWindowsPrimitives, mWindowsStructures):
  for sName in dir(mModule):
    if sName[0] != "_":
      globals()[sName] = getattr(mModule, sName);
      __all__.append(sName);
