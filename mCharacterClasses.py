import ctypes;

from .iCharacterBaseType import iCharacterBaseType;
  
cCharacterA = iCharacterBaseType.fcCreateClass(
  "iCharacterBaseTypeA", ctypes.c_ubyte, 
  bUnicode = False, uCharSize = 1,
);
cCharacterW = iCharacterBaseType.fcCreateClass(
  "iCharacterBaseTypeW", ctypes.c_ushort,
  bUnicode = True,  uCharSize = 2,
);