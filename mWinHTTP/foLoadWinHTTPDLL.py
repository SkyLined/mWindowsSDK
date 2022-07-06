from ..cDLL import cDLL;
from .mPrimitiveTypes import \
    BOOL, DWORD, HINTERNET, LPCWSTR;
from .mStructures import \
    PWINHTTP_AUTOPROXY_OPTIONS, PWINHTTP_PROXY_INFO;

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
