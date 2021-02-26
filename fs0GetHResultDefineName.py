from .dsHResultDefineName_by_uValue import dsHResultDefineName_by_uValue;

def fs0GetHResultDefineName(uHResult):
  return dsHResultDefineName_by_uValue.get(uHResult);
