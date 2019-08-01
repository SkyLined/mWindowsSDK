from cPrimitiveType import cPrimitiveType;

class cFloatType(cPrimitiveType):
  def __repr__(oSelf):
    return "<float %s:%d(%d) @ 0x%X>" % (
      oSelf.__class__.__name__,
      oSelf.fuGetSize(),
      oSelf.value,
      oSelf.fuGetAddress(),
    );
