import ctypes;

from .iPrimitiveBaseType import iPrimitiveBaseType;
from .uProcessBits import uProcessBits;

class iIntegerBaseType(iPrimitiveBaseType):
  def __repr__(oSelf):
    return "<integer %s(%s) %d-bit @ 0x%X>" % (
      oSelf.__class__.__name__,
      "%d" % oSelf.value if oSelf.value >= 0 and oSelf.value < 10 else "%d / 0x%X" % (
        oSelf.value,
        oSelf.value + ((1 << oSelf.fuGetSize() * 8) if oSelf.value < 0 else 0),
      ),
      oSelf.fuGetSize() * 8,
      oSelf.fuGetAddress(),
    );
  
  def fbGetValue(oSelf):
    return oSelf.value != 0;
  
  def fuGetValue(oSelf):
    if oSelf.value >= 0:
      return oSelf.value;
    uMaxValue = (1 << (oSelf.fuGetSize() * 8)) - 1
    return oSelf.value & uMaxValue;
  
  def fiGetValue(oSelf):
    return oSelf.value;
  
  def fSetValue(oSelf, iValue):
    oSelf.value = iValue;
  
class iIntegerBaseTypeB(iIntegerBaseType):
  def fxGetValue(oSelf):
    return oSelf.fbGetValue();
  def fsDumpValue(oSelf):
    return "value = %s" % ("TRUE" if oSelf.fbGetValue() else "FALSE");

class iIntegerBaseTypeI(iIntegerBaseType):
  def fxGetValue(oSelf):
    return oSelf.fiGetValue();
  def fsDumpValue(oSelf):
    iValue = oSelf.fiGetValue();
    return "value = %%d / %%s0x%%0%dX" % (oSelf.fuGetSize() * 2) % (iValue, "-" if iValue < 0 else "", abs(iValue));

class iIntegerBaseTypeU(iIntegerBaseType):
  def fxGetValue(oSelf):
    return oSelf.fuGetValue();
  def fsDumpValue(oSelf):
    uValue = oSelf.fuGetValue();
    return "value = %%d / 0x%%0%dX" % (oSelf.fuGetSize() * 2) % (uValue, uValue);

iIntegerBaseTypeB8        = iIntegerBaseTypeB.fcCreateType("iIntegerBaseTypeB8", ctypes.c_byte);
iIntegerBaseTypeB8        = iIntegerBaseTypeB.fcCreateType("iIntegerBaseTypeB8", ctypes.c_byte);
iIntegerBaseTypeB16       = iIntegerBaseTypeB.fcCreateType("iIntegerBaseTypeB16", ctypes.c_short);
iIntegerBaseTypeB32       = iIntegerBaseTypeB.fcCreateType("iIntegerBaseTypeB32", ctypes.c_long);
iIntegerBaseTypeB64       = iIntegerBaseTypeB.fcCreateType("iIntegerBaseTypeB64", ctypes.c_longlong);
iIntegerBaseTypeBDefault  = {32: iIntegerBaseTypeB32, 64: iIntegerBaseTypeB64}[uProcessBits];

iIntegerBaseTypeI8        = iIntegerBaseTypeI.fcCreateType("iIntegerBaseTypeI8", ctypes.c_byte);
iIntegerBaseTypeI8        = iIntegerBaseTypeI.fcCreateType("iIntegerBaseTypeI8", ctypes.c_byte);
iIntegerBaseTypeI16       = iIntegerBaseTypeI.fcCreateType("iIntegerBaseTypeI16", ctypes.c_short);
iIntegerBaseTypeI32       = iIntegerBaseTypeI.fcCreateType("iIntegerBaseTypeI32", ctypes.c_long);
iIntegerBaseTypeI64       = iIntegerBaseTypeI.fcCreateType("iIntegerBaseTypeI64", ctypes.c_longlong);
iIntegerBaseTypeIDefault  = {32: iIntegerBaseTypeI32, 64: iIntegerBaseTypeI64}[uProcessBits];

iIntegerBaseTypeU8        = iIntegerBaseTypeU.fcCreateType("iIntegerBaseTypeU8", ctypes.c_ubyte);
iIntegerBaseTypeU16       = iIntegerBaseTypeU.fcCreateType("iIntegerBaseTypeU16", ctypes.c_ushort);
iIntegerBaseTypeU32       = iIntegerBaseTypeU.fcCreateType("iIntegerBaseTypeU32", ctypes.c_ulong);
iIntegerBaseTypeU64       = iIntegerBaseTypeU.fcCreateType("iIntegerBaseTypeU64", ctypes.c_ulonglong);
iIntegerBaseTypeUDefault  = {32: iIntegerBaseTypeU32, 64: iIntegerBaseTypeU64}[uProcessBits];
