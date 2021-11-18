from mWindowsSDK import *;

def fTestKernel32DLL(oConsole):
  from mWindowsSDK.mKernel32 import oKernel32DLL;
  # Testing is currently extremely rudimentary.
  uBufferSize = MAX_PATH;
  oBuffer = WCHAR[uBufferSize]();
  
  ouResult = oKernel32DLL.GetWindowsDirectoryW(
    oBuffer.foCreatePointer().foCastTo(PWSTR), # lpBuffer
    uBufferSize, # uSize
  );
  assert ouResult != 0, \
      "oKernel32DLL.GetWindowsDirectoryW(lpBuffer=0x%X, uSize=0x%X) => 0x%X" % \
      (oBuffer.fuGetAddress(), uBufferSize, oKernel32DLL.GetLastError());
  assert ouResult <= uBufferSize, \
      "Path is larger than MAX_PATH !?";
  oConsole.fOutput("Windows directory = %s" % oBuffer.fsGetValue());

