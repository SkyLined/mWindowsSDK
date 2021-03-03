import ctypes;

from .iUnsignedIntegerBaseType import iUnsignedIntegerBaseType;
from .uProcessBits import uProcessBits;

cUnsignedInteger8        = iUnsignedIntegerBaseType.fcCreateClass("cUnsignedInteger8", ctypes.c_ubyte);
cUnsignedInteger16       = iUnsignedIntegerBaseType.fcCreateClass("cUnsignedInteger16", ctypes.c_ushort);
cUnsignedInteger32       = iUnsignedIntegerBaseType.fcCreateClass("cUnsignedInteger32", ctypes.c_ulong);
cUnsignedInteger64       = iUnsignedIntegerBaseType.fcCreateClass("cUnsignedInteger64", ctypes.c_ulonglong);
cUnsignedInteger         = {32: cUnsignedInteger32, 64: cUnsignedInteger64}[uProcessBits];
