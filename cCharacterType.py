from cPrimitiveType import cPrimitiveType;

class cCharacterType(cPrimitiveType):
  def __repr__(oSelf):
    sChar = chr(oSelf.value) if oSelf.value >= 0x20 and oSelf.value < 0x7F else None;
    return "<char %s:%d(%s%s%s) @ 0x%X>" % (
      oSelf.__class__.__name__,
      oSelf.fuGetSize(),
      "%%0%dX" % (2 * oSelf.fuGetSize()) % oSelf.value,
      "" if sChar is None else ", '%s%s'" % ("\\" if sChar in "'\\" else "", sChar),
      oSelf.fuGetAddress(),
    );
