from ..mWindowsPrimitiveTypes import __all__ as asWindowsPrimitiveNames;
from ..mWindowsPrimitiveTypes import *;
__all__ = asWindowsPrimitiveNames[:];

from ..mWindowsPrimitiveTypes import \
    HANDLE, UINT, ULONGLONG;

def fExportPrimitive(sName, xBaseType):
  cType = type(sName, (xBaseType,), {"sName": sName});
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

# Add additional primitives here using fExportPrimitive:
# Source for these is internet searches, nothing reliable.
fExportPrimitive("HDC", HANDLE);
fExportPrimitive("D3DDDI_VIDEO_PRESENT_SOURCE_ID", UINT);
fExportPrimitive("D3DGPU_VIRTUAL_ADDRESS", ULONGLONG);
fExportPrimitive("D3DKMT_HANDLE", UINT);
fExportPrimitive("D3DKMT_CLIENTHINT", UINT);
