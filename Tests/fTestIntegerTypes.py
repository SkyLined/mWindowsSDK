from mWindowsSDK import iIntegerBaseTypeI8, iIntegerBaseTypeU8, iIntegerBaseTypeU32;

def fTestIntegerTypes(oConsole):
  INT8 = iIntegerBaseTypeI8;
  UINT8 = iIntegerBaseTypeU8;
  cUINT8x4 = UINT8[4];
  oUINT8x4 = cUINT8x4(1,2,3,4);
  assert iIntegerBaseTypeU32.foFromAddress(oUINT8x4.fuGetAddress()) == 0x04030201, "FAILED!";
  assert UINT8(1)+UINT8(2) == 3, "FAILED!";
  assert UINT8(1)+UINT8(2) == 3, "FAILED!";
  assert 1+UINT8(2) == 3, "FAILED!";
  assert UINT8(1)+2 == 3, "FAILED!";
  assert UINT8(1)+2 == INT8(3), "FAILED!";

  assert UINT8(1)-UINT8(2) == -1, "FAILED!";
  assert 1-UINT8(2) == -1, "FAILED!";
  assert UINT8(1)-2 == -1, "FAILED!";

  assert UINT8(1)-2 == INT8(-1), "FAILED!";
