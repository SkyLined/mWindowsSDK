from cDLL import cDLL;
from mWindowsPrimitiveTypes import *;
from mWindowsStructureTypes import *;

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
        "EnumDisplayDevicesA": {
          "xReturnType": BOOL, 
          "txArgumentTypes": (LPCWSTR, DWORD, PDISPLAY_DEVICEA, DWORD),
        },
        "EnumDisplayDevicesW": {
          "xReturnType": BOOL, 
          "txArgumentTypes": (LPCWSTR, DWORD, PDISPLAY_DEVICEW, DWORD),
        },
      },
    );
  return goUser32DLL;