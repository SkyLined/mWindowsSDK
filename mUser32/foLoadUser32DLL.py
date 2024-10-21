from ..cDLL import cDLL;
from .mPrimitiveTypes import \
    BOOL, DWORD, HWND, LPCWSTR, PVOID, UINT;
from .mStructures import \
    PWINDOWPLACEMENT, PDISPLAY_DEVICEA, PDISPLAY_DEVICEW;

def foLoadUser32DLL():
  return cDLL(
    "User32.dll", 
    {
      "SystemParametersInfoA": {
        "xReturnType": BOOL, 
        "txArgumentTypes": (UINT, UINT, PVOID, UINT),
      },
      "SystemParametersInfoW": {
        "xReturnType": BOOL,
        "txArgumentTypes": (UINT, UINT, PVOID, UINT),
      },
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
