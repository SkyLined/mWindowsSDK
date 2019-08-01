from cPrimitiveType import cPrimitiveType;

class cIntegerType(cPrimitiveType):
  def __repr__(oSelf):
    return "<integer %s:%d(%s) @ 0x%X>" % (
      oSelf.__class__.__name__,
      oSelf.fuGetSize(),
      "%d" % oSelf.value if oSelf.value >= 0 and oSelf.value < 10 else "%d / 0x%X" % (
        oSelf.value,
        oSelf.value + ((1 << oSelf.fuGetSize() * 8) if oSelf.value < 0 else 0),
      ),
      oSelf.fuGetAddress(),
    );
