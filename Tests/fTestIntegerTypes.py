from mWindowsSDK import cSignedInteger8, cUnsignedInteger8, cUnsignedInteger32;

def fTestIntegerTypes(oConsole):
  INT8 = cSignedInteger8;
  UINT8 = cUnsignedInteger8;
  cUINT8x4 = UINT8[4];
  oUINT8x4 = cUINT8x4(1,2,3,4);
  assert cUnsignedInteger32.foFromAddress(oUINT8x4.fuGetAddress()) == 0x04030201, "FAILED!";
  assert UINT8(1)+UINT8(2) == 3, "FAILED!";
  assert UINT8(1)+UINT8(2) == 3, "FAILED!";
  assert 1+UINT8(2) == 3, "FAILED!";
  assert UINT8(1)+2 == 3, "FAILED!";
  assert UINT8(1)+2 == INT8(3), "FAILED!";
  
  assert UINT8(1)-UINT8(2) == -1, "FAILED!";
  assert 1-UINT8(2) == -1, "FAILED!";
  assert UINT8(1)-2 == -1, "FAILED!";
  
  assert UINT8(1)-2 == INT8(-1), "FAILED!";
