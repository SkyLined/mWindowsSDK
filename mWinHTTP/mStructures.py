from ..mStructureTypes import iStructureType;
from ..STRUCT import STRUCT;
from ..UNION import UNION;
from ..mWindowsStructures import *;
from .mConstants import *;
from .mPrimitives import *;

__all__ = [];

def fExportStructure(sName, *atxFields):
  cStructure = iStructureType.fcCreateClass(sName, *atxFields);
  cStructurePointer = cStructure.fcCreatePointer();
  globals()[sName] = cStructure; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.
  # Also create "P" + name as a pointer to this type:
  globals()["P" + sName] = cStructurePointer; # Make it available in the context of this file
  __all__.append("P" + sName); # Make it available as an export from this module.

#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
fExportStructure("WINHTTP_AUTOPROXY_OPTIONS",
  (DWORD,       "dwFlags"),
  (DWORD,       "dwAutoDetectFlags"),
  (LPCWSTR,     "lpszAutoConfigUrl"),
  (LPVOID,      "lpvReserved"),
  (DWORD,       "dwReserved"),
  (BOOL,        "fAutoLogonIfChallenged"),
);
fExportStructure("WINHTTP_PROXY_INFO",
  (DWORD,       "dwAccessType"),
  (LPWSTR,      "lpszProxy"),
  (LPWSTR,      "lpszProxyBypass"),
);

