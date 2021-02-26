import ctypes, json;

from .mIntegerBaseTypes import iIntegerBaseType;

gddcBufferType_by_uLength_by_cCharacterType = {};

class iCharacterBaseType(iIntegerBaseType):
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
  def fcCreateBufferType(cCharacterType, uLength):
    global gddcBufferType_by_uLength_by_cCharacterType;
    assert isinstance(uLength, (int, long)) and uLength >= 0, \
        "uLength must be a positive integer, not %s" % repr(uLength);
    dcBufferType_by_uLength = gddcBufferType_by_uLength_by_cCharacterType.setdefault(cCharacterType, {})
    cBufferType = dcBufferType_by_uLength.get(uLength);
    if cBufferType is None:
      cBufferType = cCharacterType[uLength];
      dcBufferType_by_uLength[uLength] = cBufferType;
    return cBufferType;
  
  @classmethod
  def foCreateBufferFromString(cCharacterType, sData, u0Length = None):
    uLength = u0Length if u0Length is not None else len(sData) + 1;
    assert uLength <= len(sData) + 1, \
        "You cannot create a buffer of %d characters to store a string of %d characters (%s)" % \
        (uLength, len(sData), repr(sData));
    return cCharacterType.foCreateBufferForLength(uLength, sData);
  
  @classmethod
  def foCreateBufferForLength(cCharacterType, uLength, sData = ""):
    cBufferType = cCharacterType.fcCreateBufferType(uLength);
    return cBufferType(sData);
  
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
    return "code=%s, char=%s" % (
      {1:"%02X", 2:"%04X"}[oSelf.__class__.uCharSize] % uCharCode,
      sChar
    );
  
iCharacterBaseTypeA = iCharacterBaseType.fcCreateType("iCharacterBaseTypeA", ctypes.c_ubyte, 
  bUnicode = False, sEmptyString = "",  fsValueFromCharCode = chr,    uCharSize = 1,
);
iCharacterBaseTypeW = iCharacterBaseType.fcCreateType("iCharacterBaseTypeW", ctypes.c_ushort,
  bUnicode = True,  sEmptyString = u"", fsValueFromCharCode = unichr, uCharSize = 2,
);