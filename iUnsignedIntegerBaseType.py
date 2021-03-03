from .fsDumpInteger import fsDumpInteger;
from .iIntegerBaseType import iIntegerBaseType;

class iUnsignedIntegerBaseType(iIntegerBaseType):
  def fxGetValue(oSelf):
    return oSelf.fuGetValue();
  
  def fsDumpValue(oSelf):
    return fsDumpInteger(oSelf.fuGetValue());
  
  def __repr__(oSelf):
    return "<unsigned integer %s (%d-bit @ %s) = %s>" % (
                              #   #        #     #
                              oSelf.__class__.sName,
                                  oSelf.__class__.fuGetSize() * 8,
                                           fsIntegerToHex(oSelf.fuGetAddress(), bHexOnly = True),
                                                 oSelf.fsDumpValue(),
    );
