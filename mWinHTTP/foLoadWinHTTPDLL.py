from ..cDLL import cDLL;
from .mPrimitives import *;
from .mStructures import *;

def foLoadWinHTTPDLL():
  return cDLL(
    "Winhttp.dll",
    {
      "WinHttpGetProxyForUrl": {
        "xReturnType": BOOL,
        "txArgumentTypes": (HINTERNET, LPCWSTR, PWINHTTP_AUTOPROXY_OPTIONS, PWINHTTP_PROXY_INFO),
      },
      "WinHttpOpen": {
        "xReturnType": HINTERNET,
        "txArgumentTypes": (LPCWSTR, DWORD, LPCWSTR, LPCWSTR, DWORD),
      },
    },
  );
