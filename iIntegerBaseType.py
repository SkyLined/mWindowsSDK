import ctypes;

from .iPrimitiveBaseType import iPrimitiveBaseType;

class iIntegerBaseType(iPrimitiveBaseType):
  def __init__(oSelf, *txArguments, **dxArguments):
    super(iIntegerBaseType, oSelf).__init__(*txArguments, **dxArguments);
    if len(txArguments) > 0:
      oSelf.__fCheckValue(txArguments[0]);
  def __fCheckValue(oSelf, iValue):
    # The user can provide a value but if it is too large or small to store
    # in this type of integer, the value may get truncated. This is not
    # accepted: we check the resulting value matches the provided value and
    # throw an exception if it does not match so the caller is aware that
    # they are providing invalid values.
    uBitSize = oSelf.fuGetSize() * 8;
    uMaxValue = (1 << uBitSize) - 1;
    if iValue < 0:
      iMinValue = -(uMaxValue >> 1) - 1;
      assert iValue >= iMinValue, \
          "Value -0x%X is too small to store in a %d-bit %s: the minimum is -0x%X" % (-iValue, uBitSize, oSelf.__class__.__name__, -iMinValue);
    else:
      assert iValue <= uMaxValue, \
          "Value 0x%X is too large to store in a %d-bit %s: the maximum is 0x%X" % (iValue, uBitSize, oSelf.__class__.__name__, uMaxValue);
  
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
    oSelf.__fCheckValue(iValue);

