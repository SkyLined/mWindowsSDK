from .dsExceptionDefineName_by_uValue import dsExceptionDefineName_by_uValue;

def fs0GetExceptionDefineName(uExceptionCode):
  return dsExceptionDefineName_by_uValue.get(uExceptionCode);
