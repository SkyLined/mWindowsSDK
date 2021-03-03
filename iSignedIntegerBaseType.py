from .fsDumpInteger import fsDumpInteger;
from .iIntegerBaseType import iIntegerBaseType;

class iSignedIntegerBaseType(iIntegerBaseType):
  def fxGetValue(oSelf):
    return oSelf.fiGetValue();
  
  def fsDumpValue(oSelf):
    return fsDumpInteger(oSelf.fiGetValue());
  
  def __repr__(oSelf):
    return "<signed integer %s (%d-bit @ %s) = %s>" % (
                            #   #        #     #
                            oSelf.__class__.sName,
                                oSelf.__class__.fuGetSize() * 8,
                                         fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
                                               oSelf.fsDumpValue(),
    );
