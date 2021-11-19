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
  def foCreateBufferFromString(cCharacterType, sxData, u0Length = None):
    mDebugOutput_HideInCallStack = True;
    uLength = u0Length if u0Length is not None else len(sxData) + 1;
    assert uLength <= len(sxData) + 1, \
        "You cannot create a buffer of %d characters to store a string of %d characters (%s)" % \
        (uLength, len(sxData), repr(sxData));
    return cCharacterType.foCreateBufferForLength(uLength, sxData);
  
  @classmethod
  def foCreateBufferForLength(cCharacterType, uLength, sxData = b""):
    mDebugOutput_HideInCallStack = True;
    return cCharacterType[uLength](sxData);
  
  def fxGetValue(oSelf):
    return oSelf.fsGetValue();
  
  def fsGetValue(oSelf):
    return chr(oSelf.fuGetValue());
  
  def fsbGetValue(oSelf):
    return bytes((oSelf.fuGetValue()),);
  
  def fSetValue(oSelf, xValue):
    mDebugOutput_HideInCallStack = True;
    if isinstance(xValue, str):
      assert len(xValue) == 1, \
          "Cannot set a char to a multi-char string!";
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
