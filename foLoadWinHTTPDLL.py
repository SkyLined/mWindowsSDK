from cDLL import cDLL;
from mPrimitiveTypes import *;
from mStructureTypes import *;

goWinHTTP = None;
def foLoadWinHTTPDLL():
  global goWinHTTP;
  if goWinHTTP is None:
    goWinHTTP = cDLL(
      "Winhttp.dll",
      {
        "WinHttpGetProxyForUrl": {
          "xReturnType": BOOL,
          "txArgumentTypes": (HINTERNET, LPCWSTR, WINHTTP_AUTOPROXY_OPTIONS, WINHTTP_PROXY_INFO),
        },
        "WinHttpOpen": {
          "xReturnType": HINTERNET,
          "txArgumentTypes": (LPCWSTR, DWORD, LPCWSTR, LPCWSTR, DWORD),
        },
      },
    );
  return goWinHTTP;