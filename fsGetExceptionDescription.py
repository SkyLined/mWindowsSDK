from .mWindowsConstants.dsExceptionDefineName_by_uValue import dsExceptionDefineName_by_uValue;

def fsGetExceptionDescription(uExceptionCode):
  sDetails = dsExceptionDefineName_by_uValue.get(uExceptionCode, "unknown");
  return "Exception code 0x%08X (%s)" % (uExceptionCode, sDetails);
