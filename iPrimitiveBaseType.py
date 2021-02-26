import ctypes;
from .iNumericDataBaseType import iNumericDataBaseType;

cCTypesPrimitiveMetaType = type(ctypes.c_byte);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateType(cSelf, uIndex);

class iPrimitiveBaseType(iNumericDataBaseType):
  __metaclass__ = type("iPrimitiveMetaType", (tCreateArrayMetaType, cCTypesPrimitiveMetaType), {});
  
  @classmethod
  def fcCreateType(iBaseType, sName, cCTypesBaseTypeClass, *txBadArgs, **dxStaticProperties):
    assert len(txBadArgs) == 0, \
        "fcCreateType(iBaseType=%s, sName=%s, cCTypesBaseTypeClass=%s, *txBadArgs=%s, **dxStaticProperties=%s)" % \
        (iBaseType, sName, cCTypesBaseTypeClass, txBadArgs, dxStaticProperties)
#    dxStaticProperties["_type_"] = cCTypesBaseTypeClass._type_;
    dxStaticProperties["sName"] = sName;
    return type(sName, (iBaseType, cCTypesBaseTypeClass), dxStaticProperties);
  
  def __init__(oSelf, *txArguments, **dxArguments):
    super(iNumericDataBaseType, oSelf).__init__(*txArguments, **dxArguments);
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

from .iArrayBaseType import iArrayBaseType;
from ._mDump import _fasGetDumpHeader, _fsFormatDumpLine, _fasGetDumpFooter;
