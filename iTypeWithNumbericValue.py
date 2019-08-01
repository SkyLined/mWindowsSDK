from iType import iType;

class iTypeWithNumbericValue(iType):
  def __lt__(oSelf, xOther):
    return oSelf.value < (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __le__(oSelf, xOther):
    return oSelf.value <= (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __eq__(oSelf, xOther):
    return oSelf.value == (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __ne__(oSelf, xOther):
    return oSelf.value != (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __gt__(oSelf, xOther):
    return oSelf.value > (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __ge__(oSelf, xOther):
    return oSelf.value >= (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __hash__(oSelf):
    return hash(oSelf.value);
  def __nonzero__(oSelf):
    return oSelf.value != 0;
  def __add__(oSelf, xOther):
    return oSelf.value + (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __sub__(oSelf, xOther):
    return oSelf.value - (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __mul__(oSelf, xOther):
    return oSelf.value * (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __div__(oSelf, xOther):
    return oSelf.value / (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __floordiv__(oSelf, xOther):
    return oSelf.value // (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __mod__(oSelf, xOther):
    return oSelf.value % (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __divmod__(oSelf, xOther):
    return divmod(oSelf.value, (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther));
  def __pow__(oSelf, xOther, xModulo):
    return pow(oSelf.value, (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther), (xModulo.value if isinstance(xModulo, iTypeWithNumbericValue) else xModulo));
  def __lshift__(oSelf, xOther):
    return oSelf.value << (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rshift__(oSelf, xOther):
    return oSelf.value >> (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __and__(oSelf, xOther):
    return oSelf.value & (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __xor__(oSelf, xOther):
    return oSelf.value ^ (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __or__(oSelf, xOther):
    return oSelf.value | (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __radd__(oSelf, xOther):
    return oSelf.value + (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rsub__(oSelf, xOther):
    return oSelf.value - (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rmul__(oSelf, xOther):
    return oSelf.value * (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rdiv__(oSelf, xOther):
    return oSelf.value / (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rfloordiv__(oSelf, xOther):
    return oSelf.value // (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rmod__(oSelf, xOther):
    return oSelf.value % (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rdivmod__(oSelf, xOther):
    return divmod(oSelf.value, (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther));
  def __rpow__(oSelf, xOther, xModulo):
    return pow(oSelf.value, (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther), (xModulo.value if isinstance(xModulo, iTypeWithNumbericValue) else xModulo));
  def __rlshift__(oSelf, xOther):
    return oSelf.value << (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rrshift__(oSelf, xOther):
    return oSelf.value >> (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rand__(oSelf, xOther):
    return oSelf.value & (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __rxor__(oSelf, xOther):
    return oSelf.value ^ (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __ror__(oSelf, xOther):
    return oSelf.value | (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
  def __iadd__(oSelf, xOther):
    oSelf.value = oSelf.value + (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __isub__(oSelf, xOther):
    oSelf.value = oSelf.value - (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __imul__(oSelf, xOther):
    oSelf.value = oSelf.value * (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __idiv__(oSelf, xOther):
    oSelf.value = oSelf.value / (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __ifloordiv__(oSelf, xOther):
    oSelf.value = oSelf.value // (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __imod__(oSelf, xOther):
    oSelf.value = oSelf.value % (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __ipow__(oSelf, xOther):
    oSelf.value = oSelf.value ** (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __ilshift__(oSelf, xOther):
    oSelf.value = oSelf.value << (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __irshift__(oSelf, xOther):
    oSelf.value = oSelf.value >> (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __iand__(oSelf, xOther):
    oSelf.value = oSelf.value & (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __ixor__(oSelf, xOther):
    oSelf.value = oSelf.value ^ (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __ior__(oSelf, xOther):
    oSelf.value = oSelf.value | (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther);
    return oSelf.value;
  def __neg__(oSelf):
    return -oSelf.value;
  def __abs__(oSelf):
    return abs(oSelf.value);
  def __invert__(oSelf):
    return ~oSelf.value;
  def __int__(oSelf):
    return int(oSelf.value);
  def __long__(oSelf):
    return long(oSelf.value);
  def __float__(oSelf):
    return float(oSelf.value);
  def __coerce__(oSelf, xOther):
    return (oSelf.value, (xOther.value if isinstance(xOther, iTypeWithNumbericValue) else xOther));

