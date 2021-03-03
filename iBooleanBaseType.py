from .fsDumpInteger import fsDumpInteger;
from .iIntegerBaseType import iIntegerBaseType;

class iBooleanBaseType(iIntegerBaseType):
  def fxGetValue(oSelf):
    return oSelf.fbGetValue();
  
  def fsDumpValue(oSelf):
    uValue = oSelf.fuGetValue();
    return "%s (%s)" % (fsDumpInteger(uValue), "TRUE" if uValue != 0 else "FALSE");
  
  def __repr__(oSelf):
    return "<boolean %s (%d-bit @ %s) = %s>" % (
                     #   #        #     #
                     oSelf.__class__.sName,
                         oSelf.__class__.fuGetSize() * 8,
                                  fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
                                        oSelf.fsDumpValue(),
    );
