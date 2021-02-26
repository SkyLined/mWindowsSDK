import ctypes;

from .iPrimitiveBaseType import iPrimitiveBaseType;
from .uProcessBits import uProcessBits;

class iFloatingPointBaseType(iPrimitiveBaseType):
  def __repr__(oSelf):
    return "<float %s:%d(%s) @ 0x%X>" % (
      oSelf.__class__.__name__,
      oSelf.fuGetSize(),
      str(oSelf.value),
      oSelf.fuGetAddress(),
    );
  
  def fsDumpValue(oSelf):
    return "value = %s" % oSelf.value;

iFloatingPointBaseType32  = iFloatingPointBaseType.fcCreateType("iFloatingPointBaseType32", ctypes.c_float);
iFloatingPointBaseType64  = iFloatingPointBaseType.fcCreateType("iFloatingPointBaseType64", ctypes.c_double);
