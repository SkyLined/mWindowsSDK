from mWindowsSDK import *;

def fTestKernel32DLL(oConsole):
  # Testing is currently extremely rudimentary.
  oKernel32 = foLoadKernel32DLL();

  uBufferSize = MAX_PATH;
  oBuffer = WCHAR[uBufferSize]();
  
  ouResult = oKernel32.GetWindowsDirectoryW(
    oBuffer.foCreatePointer(), # lpBuffer
    uBufferSize, # uSize
  );
  assert ouResult != 0, \
      "oKernel32.GetWindowsDirectoryW(lpBuffer=0x%X, uSize=0x%X) => 0x%X" % \
      (oBuffer.fuGetAddress(), uBufferSize, oKernel32.GetLastError());
  assert ouResult <= uBufferSize, \
      "Path is larger than MAX_PATH !?";
  oConsole.fOutput("Windows directory = %s" % oBuffer.fsGetValue());

