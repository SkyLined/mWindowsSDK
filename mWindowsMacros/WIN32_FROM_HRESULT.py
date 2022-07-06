from ..mWindowsPrimitiveTypes import HRESULT;

def WIN32_FROM_HRESULT(ohResult):
  assert isinstance(ohResult, HRESULT), \
      "%s is not an HRESULT" % repr(ohResult);
  assert ohResult.value & 0xFFFF0000 == 0x80070000, \
      "Invalid hResult value 0x%08X" % ohResult.value;
  return ohResult.value & 0xFFFF;
