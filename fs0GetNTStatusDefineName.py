from .mWindowsConstants.dsNTStatusDefineName_by_uValue import dsNTStatusDefineName_by_uValue;

def fs0GetNTStatusDefineName(uNTStatusValue):
  return dsNTStatusDefineName_by_uValue.get(uNTStatusValue);
