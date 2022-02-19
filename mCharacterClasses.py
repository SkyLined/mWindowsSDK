import ctypes;

from .iCharacterBaseType import iCharacterBaseType;
  
cCharacterA = iCharacterBaseType.fcCreateClass(
  "iCharacterBaseTypeA", ctypes.c_ubyte, 
);
cCharacterW = iCharacterBaseType.fcCreateClass(
  "iCharacterBaseTypeW", ctypes.c_ushort,
  s0UnicodeEncoding = "UTF-16LE",
);