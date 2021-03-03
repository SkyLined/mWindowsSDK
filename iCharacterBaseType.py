from .fsDumpInteger import fsDumpInteger;
from .iUnsignedIntegerBaseType import iUnsignedIntegerBaseType;

class iCharacterBaseType(iUnsignedIntegerBaseType):
  def __repr__(oSelf):
    sChar = chr(oSelf.value) if oSelf.value >= 0x20 and oSelf.value < 0x7F else None;
    return "<char %s:%d(%s%s%s) @ 0x%X>" % (
      oSelf.__class__.__name__,
      oSelf.fuGetSize(),
      "%%0%dX" % (2 * oSelf.fuGetSize()) % oSelf.value,
      "" if sChar is None else ", '%s%s'" % ("\\" if sChar in "'\\" else "", sChar),
      oSelf.fuGetAddress(),
    );
  
  @classmethod
  def foCreateBufferFromString(cCharacterType, sData, u0Length = None):
    uLength = u0Length if u0Length is not None else len(sData) + 1;
    assert uLength <= len(sData) + 1, \
        "You cannot create a buffer of %d characters to store a string of %d characters (%s)" % \
        (uLength, len(sData), repr(sData));
    return cCharacterType.foCreateBufferForLength(uLength, sData);
  
  @classmethod
  def foCreateBufferForLength(cCharacterType, uLength, sData = ""):
    return cCharacterType[uLength](sData);
  
  def fxGetValue(oSelf):
    return oSelf.fsGetValue();
  
  def fsGetValue(oSelf):
    return oSelf.__class__.fsValueFromCharCode(oSelf.fuGetValue());
  
  def fSetValue(oSelf, xValue):
    if isinstance(xValue, (str, unicode)):
      xValue = ord(xValue);
    super(iCharacterBaseType, oSelf).fSetValue(xValue);
  
  def fsDumpValue(oSelf):
    uCharCode = oSelf.fuGetValue();
    s0Char = {0: "'\\0'", 0x9: "'\\t'", 0xA: "'\\r'", 0xD: "'\\n'", 0x27: "'\\''"}.get(uCharCode);
    sChar = (
      s0Char if s0Char is not None else
      "'\\x%02X'" % uCharCode if uCharCode < 0x20 else
      "'%s'" % chr(uCharCode) if uCharCode < 0x100 else
      "'\\u%04X'" % uCharCode
    );
    sCharCode = {1:"%02X", 2:"%04X"}[oSelf.__class__.uCharSize] % uCharCode;
    return "%s (%s)" % (sChar, sCharCode);
  
  def __repr__(oSelf):
    return "<character %s (%d-bit @ %s) = %s>" % (
                       #   #        #     #
                       oSelf.__class__.sName,
                           oSelf.__class__.fuGetSize() * 8,
                                    fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
                                          oSelf.fsDumpValue(),
    );
