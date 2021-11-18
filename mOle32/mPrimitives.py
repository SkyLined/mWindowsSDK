from ..mWindowsPrimitives import __all__ as asWindowsPrimitiveNames;
from ..mWindowsPrimitives import *;
__all__ = asWindowsPrimitiveNames[:];

def fExportPrimitive(sName, xBaseType):
  cType = type(sName, (xBaseType,), {"sName": sName});
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

# Add additional primitives here using fExportPrimitive:
fExportPrimitive("LPCOLESTR",  PWCHAR); # The "C" is for "Constant"
fExportPrimitive("LPOLESTR",   PWCHAR);
fExportPrimitive("CLSCTX",     SIZE_T); # The size of enums is not defined; assume ISA default word size.