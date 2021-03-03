import ctypes;

from .iPointerBaseType import iPointerBaseType;
from .uProcessBits import uProcessBits;

iPointerType32 = type("iPointerBaseType32", (iPointerBaseType, ctypes.c_ulong), {});
iPointerType64 = type("iPointerBaseType64", (iPointerBaseType, ctypes.c_ulonglong), {});
iPointerType = {32: iPointerType32, 64: iPointerType64}[uProcessBits];
