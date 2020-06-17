from fTestDependencies import fTestDependencies;
fTestDependencies();

try:
  import mDebugOutput;
except:
  mDebugOutput = None;
try:
  try:
    from oConsole import oConsole;
  except:
    import sys, threading;
    oConsoleLock = threading.Lock();
    class oConsole(object):
      @staticmethod
      def fOutput(*txArguments, **dxArguments):
        sOutput = "";
        for x in txArguments:
          if isinstance(x, (str, unicode)):
            sOutput += x;
        sPadding = dxArguments.get("sPadding");
        if sPadding:
          sOutput.ljust(120, sPadding);
        oConsoleLock.acquire();
        print sOutput;
        sys.stdout.flush();
        oConsoleLock.release();
      fPrint = fOutput;
      @staticmethod
      def fStatus(*txArguments, **dxArguments):
        pass;
  
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
  oConsole.fOutput("Windows directory = %s" % oBuffer.fsGetString());
  
  oConsole.fOutput("+ Done.");
  
except Exception as oException:
  if mDebugOutput:
    mDebugOutput.fTerminateWithException(oException, bShowStacksForAllThread = True);
  raise;
