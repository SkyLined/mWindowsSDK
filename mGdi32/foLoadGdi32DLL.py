from ..cDLL import cDLL;
from .mPrimitives import *;
from .mStructures import *;

def foLoadGdi32DLL():
  return cDLL(
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
