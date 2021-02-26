from mWindowsSDK import *;

def fTestUser32GDIDLL(oConsole):
  oUser32DLL = foLoadUser32DLL();
  oDisplayDevice = DISPLAY_DEVICEA();
  # oDisplayDevice.fClear();
  oDisplayDevice.cb = oDisplayDevice.fuGetSize();
  uDisplayIndex = 0;
  while True:
    oConsole.fStatus("Test GDI: Enumerating Display Devices...");
    if not oUser32DLL.EnumDisplayDevicesA(NULL, uDisplayIndex, oDisplayDevice.foCreatePointer(), 0):
      break;
    
    for sLine in oDisplayDevice.fasDump("oDisplayDevice #%d" % uDisplayIndex):
      oConsole.fOutput(sLine);
    uDisplayIndex += 1;