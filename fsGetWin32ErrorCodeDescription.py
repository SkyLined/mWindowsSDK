from .mWindowsConstants.dsWin32ErrorCodeDefineName_by_uValue import dsWin32ErrorCodeDefineName_by_uValue;

def fsGetWin32ErrorCodeDescription(uWin32ErrorCode):
  assert isinstance(uWin32ErrorCode, int), \
      "uWin32ErrorCode muts be 'int', not %s (%s)" % (type(uWin32ErrorCode), repr(uWin32ErrorCode));
  sDetails = dsWin32ErrorCodeDefineName_by_uValue.get(uWin32ErrorCode, "unknown") if uWin32ErrorCode < 0x10000 else "invalid";
  return "Win32 error 0x%X (%s)" % (uWin32ErrorCode, sDetails);
