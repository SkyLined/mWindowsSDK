from ..cDLL import cDLL;
from .mPrimitiveTypes import \
    BOOL, DWORD, HANDLE, HMODULE, LPDWORD, LPSTR, LPWSTR, PHMODULE;

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