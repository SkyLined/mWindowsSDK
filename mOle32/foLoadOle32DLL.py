from ..cDLL import cDLL;
from .mPrimitives import *;
from .mStructures import *;

def foLoadOle32DLL():
  return cDLL(
    "Ole32.dll", 
    {
      "CoCreateInstance": {
        "xReturnType": HRESULT, 
        "txArgumentTypes": (REFCLSID, LPUNKNOWN, DWORD, REFIID, LPVOID),
      },
      "CoInitialize": {
        "xReturnType": HRESULT,
        "txArgumentTypes": (LPVOID),
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
        "txArgumentTypes": (REFCLSID, LPOLESTR.fcCreatePointer()),
      },
    },
  );
