import ctypes;
from .iBaseType import iBaseType;

cCTypesPrimitiveMetaType = type(ctypes.c_byte);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateClass(cSelf, uIndex);

class iPrimitiveBaseType(iBaseType):
  __metaclass__ = type("iPrimitiveMetaType", (tCreateArrayMetaType, cCTypesPrimitiveMetaType), {});
  
  @classmethod
  def fcCreateClass(iBaseType, sName, cCTypesBaseTypeClass, *txBadArgs, **dxStaticProperties):
    assert len(txBadArgs) == 0, \
        "fcCreateClass(iBaseType=%s, sName=%s, cCTypesBaseTypeClass=%s, *txBadArgs=%s, **dxStaticProperties=%s)" % \
        (iBaseType, sName, cCTypesBaseTypeClass, txBadArgs, dxStaticProperties)
#    dxStaticProperties["_type_"] = cCTypesBaseTypeClass._type_;
    dxStaticProperties["sName"] = sName;
    return type(sName, (iBaseType, cCTypesBaseTypeClass), dxStaticProperties);
  
  def __init__(oSelf, *txArguments, **dxArguments):
    super(iPrimitiveBaseType, oSelf).__init__(*txArguments, **dxArguments);
    oSelf.sTypeName = oSelf.__class__.__name__;
  
  def fsDumpValue(oSelf):
    raise NotImplementedError("%s has not implemented fsDumpValue!" % oSelf.__class__.__name__);
  
  def fasDump(oSelf, s0Name = None, uOffset = 0, sPadding = "", bOutputHeader = True):
    sName = s0Name if s0Name is not None else "%s @ 0x%X" % (oSelf.__class__.sName, oSelf.fuGetAddress());
    return  (
      (_fasGetDumpHeader() if bOutputHeader else []) +
      [_fsFormatDumpLine(
        uOffset = uOffset,
        u0Size = oSelf.__class__.fuGetSize(),
        a0uBytes = oSelf.fauGetBytes(),
        sPadding = sPadding,
        sType = oSelf.__class__.sName,
        sName = sName,
        sComment = oSelf.fsDumpValue(),
      )] +
      (_fasGetDumpFooter() if bOutputHeader else [])
    );
  
  def __lt__(oSelf, xOther):
    return oSelf.value < (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __le__(oSelf, xOther):
    return oSelf.value <= (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __eq__(oSelf, xOther):
    return oSelf.value == (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __ne__(oSelf, xOther):
    return oSelf.value != (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __gt__(oSelf, xOther):
    return oSelf.value > (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __ge__(oSelf, xOther):
    return oSelf.value >= (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __hash__(oSelf):
    return hash(oSelf.value);
  def __nonzero__(oSelf):
    return oSelf.value != 0;
  def __add__(oSelf, xOther):
    return oSelf.value + (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __sub__(oSelf, xOther):
    return oSelf.value - (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __mul__(oSelf, xOther):
    return oSelf.value * (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __div__(oSelf, xOther):
    return oSelf.value / (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __floordiv__(oSelf, xOther):
    return oSelf.value // (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __mod__(oSelf, xOther):
    return oSelf.value % (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __divmod__(oSelf, xOther):
    return divmod(oSelf.value, (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther));
  def __pow__(oSelf, xOther, xModulo = None):
    return pow(
      oSelf.value,
      (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther),
      (xModulo.value if isinstance(xModulo, iPrimitiveBaseType) else xModulo)
    );
  def __lshift__(oSelf, xOther):
    return oSelf.value << (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rshift__(oSelf, xOther):
    return oSelf.value >> (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __and__(oSelf, xOther):
    return oSelf.value & (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __xor__(oSelf, xOther):
    return oSelf.value ^ (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __or__(oSelf, xOther):
    return oSelf.value | (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __radd__(oSelf, xOther):
    return oSelf.value + (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rsub__(oSelf, xOther):
    return oSelf.value - (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rmul__(oSelf, xOther):
    return oSelf.value * (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rdiv__(oSelf, xOther):
    return oSelf.value / (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rfloordiv__(oSelf, xOther):
    return oSelf.value // (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rmod__(oSelf, xOther):
    return oSelf.value % (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rdivmod__(oSelf, xOther):
    return divmod(oSelf.value, (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther));
  def __rpow__(oSelf, xOther):
    return pow(oSelf.value, (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther));
  def __rlshift__(oSelf, xOther):
    return oSelf.value << (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rrshift__(oSelf, xOther):
    return oSelf.value >> (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rand__(oSelf, xOther):
    return oSelf.value & (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __rxor__(oSelf, xOther):
    return oSelf.value ^ (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __ror__(oSelf, xOther):
    return oSelf.value | (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
  def __iadd__(oSelf, xOther):
    oSelf.value = oSelf.value + (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __isub__(oSelf, xOther):
    oSelf.value = oSelf.value - (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __imul__(oSelf, xOther):
    oSelf.value = oSelf.value * (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __idiv__(oSelf, xOther):
    oSelf.value = oSelf.value / (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __ifloordiv__(oSelf, xOther):
    oSelf.value = oSelf.value // (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __imod__(oSelf, xOther):
    oSelf.value = oSelf.value % (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __ipow__(oSelf, xOther):
    oSelf.value = oSelf.value ** (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __ilshift__(oSelf, xOther):
    oSelf.value = oSelf.value << (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __irshift__(oSelf, xOther):
    oSelf.value = oSelf.value >> (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __iand__(oSelf, xOther):
    oSelf.value = oSelf.value & (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __ixor__(oSelf, xOther):
    oSelf.value = oSelf.value ^ (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
    return oSelf.value;
  def __ior__(oSelf, xOther):
    oSelf.value = oSelf.value | (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther);
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
    return (oSelf.value, (xOther.value if isinstance(xOther, iPrimitiveBaseType) else xOther));

from .iArrayBaseType import iArrayBaseType;
from ._mDump import _fasGetDumpHeader, _fsFormatDumpLine, _fasGetDumpFooter;
