from fTestDependencies import fTestDependencies;
fTestDependencies();

try:
  import mDebugOutput;
except:
  mDebugOutput = None;

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

try:
  from mWindowsSDK import *;
  from fTestGdi32 import fTestGdi32;
  from fTestKernel32DLL import fTestKernel32DLL;
  from fTestUser32GDIDLL import fTestUser32GDIDLL;
  from fTestCharacterTypes import fTestCharacterTypes;
  from fTestIntegerTypes import fTestIntegerTypes;
  
  assert NT_SUCCESS(STATUS_SUCCESS), \
      "NT_SUCCESS(STATUS_SUCCESS) => %s instead of True" % repr(NT_SUCCESS(STATUS_SUCCESS));
  assert not NT_ERROR(STATUS_SUCCESS), \
      "NT_ERROR(STATUS_SUCCESS) => %s instead of False" % repr(NT_ERROR(STATUS_SUCCESS));
  
  fTestCharacterTypes(oConsole);
  fTestIntegerTypes(oConsole);
  fTestGdi32(oConsole);
  fTestKernel32DLL(oConsole);
  fTestUser32GDIDLL(oConsole);
  oConsole.fOutput("+ Done.");
  
except Exception as oException:
  if mDebugOutput:
    mDebugOutput.fTerminateWithException(oException, bShowStacksForAllThread = True);
  raise;
