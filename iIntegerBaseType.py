import ctypes;

from .iPrimitiveBaseType import iPrimitiveBaseType;

class iIntegerBaseType(iPrimitiveBaseType):
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
  
