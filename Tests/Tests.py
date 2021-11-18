import os, sys;
sModulePath = os.path.dirname(__file__);
sys.path = [sModulePath] + [sPath for sPath in sys.path if sPath.lower() != sModulePath.lower()];

from fTestDependencies import fTestDependencies;
fTestDependencies();

try: # mDebugOutput use is Optional
  import mDebugOutput as m0DebugOutput;
except ModuleNotFoundError as oException:
  if oException.args[0] != "No module named 'mDebugOutput'":
    raise;
  m0DebugOutput = None;

guExitCodeInternalError = 1; # Use standard value;
try:
  from mConsole import oConsole;
except:
  import sys, threading;
  oConsoleLock = threading.Lock();
  class oConsole(object):
    @staticmethod
    def fOutput(*txArguments, **dxArguments):
      sOutput = "";
      for x in txArguments:
        if isinstance(x, str):
          sOutput += x;
      sPadding = dxArguments.get("sPadding");
      if sPadding:
        sOutput.ljust(120, sPadding);
      oConsoleLock.acquire();
      print(sOutput);
      sys.stdout.flush();
      oConsoleLock.release();
    @staticmethod
    def fStatus(*txArguments, **dxArguments):
      pass;

try:
  from mWindowsSDK import *;
  from fTestCharacterTypes import fTestCharacterTypes;
  from fTestIntegerTypes import fTestIntegerTypes;
  from fTestGdi32 import fTestGdi32;
  from fTestKernel32DLL import fTestKernel32DLL;
  from fTestOle32 import fTestOle32;
  from fTestUser32DLL import fTestUser32DLL;
  from fTestWinHTTP import fTestWinHTTP;
  from mWindowsSDK.fsDumpInteger import fsDumpInteger;
  
  for (uValue, sValue) in {
    1000: "1,000 / 0x3E8",
    1000000: "1,000,000 / 0xF4240",
  }.items():
    assert fsDumpInteger(uValue) == sValue, \
        "Expected fsDumpInteger(%d) to be %s, but got %s" % \
        (uValue, repr(sValue), repr(fsDumpInteger(uValue)));
  
  assert NT_SUCCESS(STATUS_SUCCESS), \
      "NT_SUCCESS(STATUS_SUCCESS) => %s instead of True" % repr(NT_SUCCESS(STATUS_SUCCESS));
  assert not NT_ERROR(STATUS_SUCCESS), \
      "NT_ERROR(STATUS_SUCCESS) => %s instead of False" % repr(NT_ERROR(STATUS_SUCCESS));
  
  fTestCharacterTypes(oConsole);
  fTestIntegerTypes(oConsole);
  fTestGdi32(oConsole);
  fTestKernel32DLL(oConsole);
  fTestOle32(oConsole);
  fTestUser32DLL(oConsole);
  fTestWinHTTP(oConsole);
  oConsole.fOutput("+ Done.");
  
except Exception as oException:
  if m0DebugOutput:
    m0DebugOutput.fTerminateWithException(oException, guExitCodeInternalError, bShowStacksForAllThread = True);
  raise;
