from .dsWin32ErrorCodeDefineName_by_uValue import dsWin32ErrorCodeDefineName_by_uValue;

def fsGetWin32ErrorCodeDescription(uWin32ErrorCode):
  sDetails = dsWin32ErrorCodeDefineName_by_uValue.get(uWin32ErrorCode, "unknown") if uWin32ErrorCode < 0x10000 else "invalid";
  return "Win32 error 0x%X (%s)" % (uWin32ErrorCode, sDetails);
