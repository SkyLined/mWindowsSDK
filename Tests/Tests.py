from fTestDependencies import fTestDependencies;
fTestDependencies();

try: # mDebugOutput use is Optional
  import mDebugOutput as m0DebugOutput;
except ModuleNotFoundError as oException:
  if oException.args[0] != "No module named 'mDebugOutput'":
    raise;
  m0DebugOutput = None;

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
  fTestUser32GDIDLL(oConsole);
  oConsole.fOutput("+ Done.");
  
except Exception as oException:
  if m0DebugOutput:
    m0DebugOutput.fTerminateWithException(oException, bShowStacksForAllThread = True);
  raise;
