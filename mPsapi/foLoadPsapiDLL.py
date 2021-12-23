from ..cDLL import cDLL;
from .mConstants import *;
from .mPrimitives import *;
from .mStructures import *;
from ..uProcessBits import uProcessBits;

goPsapiDLL = None;
def foLoadPsapiDLL():
  global goPsapiDLL;
  if goPsapiDLL is None:
    goPsapiDLL = cDLL(
      "psapi.dll",
      {
        "GetModuleFileNameExA": {
          "xReturnType": DWORD,
          "txArgumentTypes": (HANDLE, HMODULE, LPSTR, DWORD),
        },
        "GetModuleFileNameExW": {
          "xReturnType": DWORD,
          "txArgumentTypes": (HANDLE, HMODULE, LPWSTR, DWORD),
        },
      },
    );
  return goPsapiDLL;