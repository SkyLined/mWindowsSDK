import ctypes;

from .iSignedIntegerBaseType import iSignedIntegerBaseType;
from .uProcessBits import uProcessBits;

cSignedInteger8        = iSignedIntegerBaseType.fcCreateClass("cSignedInteger8", ctypes.c_byte);
cSignedInteger16       = iSignedIntegerBaseType.fcCreateClass("cSignedInteger16", ctypes.c_short);
cSignedInteger32       = iSignedIntegerBaseType.fcCreateClass("cSignedInteger32", ctypes.c_long);
cSignedInteger64       = iSignedIntegerBaseType.fcCreateClass("cSignedInteger64", ctypes.c_longlong);
cSignedInteger         = {32: cSignedInteger32, 64: cSignedInteger64}[uProcessBits];
