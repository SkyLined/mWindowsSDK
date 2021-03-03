from .mWindowsConstants.dsNTStatusDefineName_by_uValue import dsNTStatusDefineName_by_uValue;

def fsGetNTStatusDescription(uNTStatusValue):
  sDetails = dsNTStatusDefineName_by_uValue.get(uNTStatusValue, "unknown");
  return "NTSTATUS 0x%08X (%s)" % (uNTStatusValue, sDetails);
