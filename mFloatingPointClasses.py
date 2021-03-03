import ctypes;

from .iFloatingPointBaseType import iFloatingPointBaseType;

cFloatingPoint32  = iFloatingPointBaseType.fcCreateClass(
  "iFloatingPointBaseType32",
  ctypes.c_float
);
cFloatingPoint64  = iFloatingPointBaseType.fcCreateClass(
  "iFloatingPointBaseType64",
  ctypes.c_double
);
