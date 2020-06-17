from fTestDependencies import fTestDependencies;
fTestDependencies();

from mDebugOutput import fEnableDebugOutputForClass, fEnableDebugOutputForModule, fTerminateWithException;
try:
  # Testing is currently extremely rudimentary.
  from mWindowsSDK import *;
  
  oKernel32 = cDLL("kernel32.dll", {
    "GetLastError": {
      "xReturnType": DWORD,
    },
    "GetWindowsDirectoryW": {
      "xReturnType": UINT,
      "txArgumentTypes": (LPWSTR, UINT),
    },
  });

  uBufferSize = MAX_PATH;
  oBuffer = foCreateBuffer(uBufferSize, bUnicode = True);
  ouResult = oKernel32.GetWindowsDirectoryW(
    oBuffer.foCreatePointer(LPWSTR), # lpBuffer
    uBufferSize, # uSize
  );
  assert ouResult.value != 0, \
      "oKernel32.GetWindowsDirectoryW(lpBuffer=0x%X, uSize=0x%X) => 0x%X" % \
      (oBuffer.fuGetAddress(), uBufferSize, oKernel32.GetLastError().value);
  assert ouResult.value <= uBufferSize, \
      "Path is larger than MAX_PATH !?";
  print "Windows directory = %s" % oBuffer.fsGetString();

except Exception as oException:
  fTerminateWithException(oException, bShowStacksForAllThread = True);
