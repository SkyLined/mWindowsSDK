from cDLL import cDLL;
from mPrimitiveTypes import *;
from mStructureTypes import *;

goOle32DLL = None;
def foLoadOle32DLL():
  global goOle32DLL;
  if goOle32DLL is None:
    goOle32DLL = cDLL(
      "Ole32.dll", 
      {
        "CoCreateInstance": {
          "xReturnType": HRESULT, 
          "txArgumentTypes": (REFCLSID, LPUNKNOWN, DWORD, REFIID, LPVOID),
        },
        "CLSIDFromProgID": {
          "xReturnType": HRESULT, 
          "txArgumentTypes": (LPCOLESTR, LPCLSID),
        },
        "CLSIDFromProgIDEx": {
          "xReturnType": HRESULT, 
          "txArgumentTypes": (LPCOLESTR, LPCLSID),
        },
        "ProgIDFromCLSID": {
          "xReturnType": HRESULT, 
          "txArgumentTypes": (REFCLSID, fcCreatePointerType(LPOLESTR)),
        },
      },
    );
  return goOle32DLL;