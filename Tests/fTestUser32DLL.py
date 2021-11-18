from mWindowsSDK import *;

def fTestUser32DLL(oConsole):
  from mWindowsSDK import foLoadUser32DLL;
  oUser32DLL = foLoadUser32DLL();
  oDisplayDevice = DISPLAY_DEVICEA();
  # oDisplayDevice.fClear();
  oDisplayDevice.cb = oDisplayDevice.fuGetSize();
  uDisplayIndex = 0;
  while True:
    oConsole.fStatus("Test User32: Enumerating Display Devices...");
    if not oUser32DLL.EnumDisplayDevicesA(NULL, uDisplayIndex, oDisplayDevice.foCreatePointer(), 0):
      break;
    
    for sLine in oDisplayDevice.fasDump("oDisplayDevice #%d" % uDisplayIndex):
      oConsole.fOutput(sLine);
    uDisplayIndex += 1;