from ..mWindowsPrimitives import *;
# Source for these is internet searches, nothing reliable.

def fExportPrimitive(sName, xBaseType):
  cType = type(sName, (xBaseType,), {"sName": sName});
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

fExportPrimitive("LPCOLESTR",  PWCHAR); # The "C" is for "Constant"
fExportPrimitive("LPOLESTR",   PWCHAR);
fExportPrimitive("CLSCTX",     SIZE_T); # The size of enums is not defined; assume ISA default word size.