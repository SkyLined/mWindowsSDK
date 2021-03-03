from .cDLL import cDLL;
from .mWindowsPrimitives import *;
from .mWindowsStructures import *;

goWinHTTP = None;
def foLoadWinHTTPDLL():
  global goWinHTTP;
  if goWinHTTP is None:
    goWinHTTP = cDLL(
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
  return goWinHTTP;