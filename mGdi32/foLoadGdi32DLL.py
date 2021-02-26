from ..cDLL import cDLL;
from .mPrimitiveTypes import *;
from .mStructureTypes import *;

goGdi32DLL = None;
def foLoadGdi32DLL():
  global goGdi32DLL;
  if goGdi32DLL is None:
    goGdi32DLL = cDLL(
      "Gdi32.dll", 
      {
        "CreateDCA": {
          "xReturnType": HDC, 
          "txArgumentTypes": (LPCSTR, LPCSTR, LPCSTR, PDEVMODEA),
        },
        "CreateDCW": {
          "xReturnType": HDC, 
          "txArgumentTypes": (LPCSTR, LPCSTR, LPCSTR, PDEVMODEW),
        },
        "D3DKMTOpenAdapterFromHdc": {
          "xReturnType": NTSTATUS, 
          "txArgumentTypes": (PD3DKMT_OPENADAPTERFROMHDC,),
        },
        "D3DKMTCreateDevice": {
          "xReturnType": NTSTATUS, 
          "txArgumentTypes": (PD3DKMT_CREATEDEVICE,),
        },
        "D3DKMTCreateContext": {
          "xReturnType": NTSTATUS,
          "txArgumentTypes": (PD3DKMT_CREATECONTEXT,),
        },
      },
    );
  return goGdi32DLL;