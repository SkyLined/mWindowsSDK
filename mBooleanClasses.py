import ctypes;

from .iBooleanBaseType import iBooleanBaseType;
from .uProcessBits import uProcessBits;

cBoolean8        = iBooleanBaseType.fcCreateClass("cBoolean8",  ctypes.c_byte);
cBoolean16       = iBooleanBaseType.fcCreateClass("cBoolean16", ctypes.c_short);
cBoolean32       = iBooleanBaseType.fcCreateClass("cBoolean32", ctypes.c_long);
cBoolean64       = iBooleanBaseType.fcCreateClass("cBoolean64", ctypes.c_longlong);
cBoolean         = {32: cBoolean32, 64: cBoolean64}[uProcessBits];
