import ctypes;

def fsGetStringAtAddress(uAddress, bUnicode = False):
  cCharPointer = ctypes.c_wchar_p if bUnicode else ctypes.c_char_p;
  oString = cCharPointer(uAddress);
  return oString.value[:];