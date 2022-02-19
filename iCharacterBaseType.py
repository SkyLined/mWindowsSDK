import math;

from .fsDumpInteger import fsDumpInteger;
from .iUnsignedIntegerBaseType import iUnsignedIntegerBaseType;

class iCharacterBaseType(iUnsignedIntegerBaseType):
  s0UnicodeEncoding = None; # Default
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
  def foCreateString(cCharacterType, sxData):
    if isinstance(sxData, bytes):
      assert cCharacterType.fuGetSize() == 1, \
          "Cannot create a %s string using bytes: %s" % (cCharacterType.__name__, sxData);
      sbData = sxData + b"\0"; # Add '\0' terminator
    else:
      assert isinstance(sxData, str), \
          "sxData must be bytes or str, not %s" % repr(sxData);
      sData = sxData + "\0"; # Add '\0' terminator
      if cCharacterType.s0UnicodeEncoding is None:
        sbData = bytes(ord(sChar) for sChar in sData);
      else:
        sbData = sData.encode(cCharacterType.s0UnicodeEncoding, "strict");
    uLength = int(math.ceil(len(sbData) / cCharacterType.fuGetSize()));
    oArray = cCharacterType[uLength]();
    oArray.fSetBytes(sbData);
    return oArray;
  
  def fxGetValue(oSelf):
    return oSelf.fsGetValue();
  
  def fsGetValue(oSelf):
    return chr(oSelf.fuGetValue());
  
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
      "'\\u%04X'" % uCharCode if uCharCode < 0x10000 else
      "'\\U%08X'" % uCharCode
    );
    sCharCode = "%%0%dX" % (2 * oSelf.fuGetSize()) % uCharCode;
    return "%s (%s)" % (sChar, sCharCode);
  
  def __repr__(oSelf):
    return "<character %s (%d-bit @ %s) = %s>" % (
                       #   #        #     #
                       oSelf.__class__.sName,
                           oSelf.__class__.fuGetSize() * 8,
                                    fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
                                          oSelf.fsDumpValue(),
    );
