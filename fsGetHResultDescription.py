from .mWindowsConstants.dsHResultDefineName_by_uValue import dsHResultDefineName_by_uValue;
from .fsGetWin32ErrorCodeDescription import fsGetWin32ErrorCodeDescription;

def fsGetHResultDescription(uHResultValue):
  if uHResultValue & 0xFFFF0000 == 0x80070000:
    uWin32ErrorCodeValue = uHResultValue & 0xFFFF;
    sDetails = "Win32 error %d: %s" % (uWin32ErrorCodeValue, fsGetWin32ErrorCodeDescription(uWin32ErrorCodeValue));
  else:
    sDetails = dsHResultDefineName_by_uValue.get(uHResultValue, "unknown");
  return "HRESULT 0x%08X (%s)" % (uHResultValue, sDetails);
