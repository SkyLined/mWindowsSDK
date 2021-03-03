from ..mWindowsPrimitives import HRESULT;

def HRESULT_FROM_WIN32(uWin32):
  if uWin32 == 0: return HRESULT(0);
  assert uWin32 & 0xFFFF0000 == 0, \
      "Invalid WIN32 value 0x%X" % uWin32;
  return HRESULT(0x80070000 + uWin32);
