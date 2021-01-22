from cDLL import cDLL;
from mPrimitiveTypes import *;
from mStructureTypes import *;

goUser32DLL = None;
def foLoadUser32DLL():
  global goUser32DLL;
  if goUser32DLL is None:
    goUser32DLL = cDLL(
      "User32.dll", 
      {
        "GetWindowPlacement": {
          "xReturnType": BOOL, 
          "txArgumentTypes": (HWND, PWINDOWPLACEMENT),
        },
        "SetWindowPlacement": {
          "xReturnType": BOOL, 
          "txArgumentTypes": (HWND, PWINDOWPLACEMENT),
        },
      },
    );
  return goUser32DLL;