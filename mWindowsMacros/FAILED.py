from ..mWindowsPrimitives import HRESULT;

def FAILED(oHResult):
  assert isinstance(oHResult, HRESULT), \
      "oHResult %s is not an HRESULT" % repr(oHResult);
  return oHResult.value >= 0x80000000;
