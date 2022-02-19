import ctypes, json;

from .fsDumpInteger import fsDumpInteger;
from .iBaseType import iBaseType;

gddcArrayType_by_uElementCount_by_uElementType = {};

cCTypesArrayMetaType = type(ctypes.Array);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    mDebugOutput_HideInCallStack = True;
    return iArrayBaseType.fcCreateClass(cSelf, uIndex);

class iArrayBaseType(iBaseType, ctypes.Array, metaclass=type("iArrayMetaType", (tCreateArrayMetaType, cCTypesArrayMetaType), {})):
  _type_ = ctypes.c_bool; # Placeholder to satisfy ctypes
  _length_ = 1; # Placeholder to satisfy ctypes
  
  
  @staticmethod
  def fcCreateClass(cElementClass, uElementCount):
    global gddcArrayType_by_uElementCount_by_uElementType;
    assert issubclass(cElementClass, iBaseType), \
        "cElementClass is not a type but %s" % repr(cElementClass);
    assert isinstance(uElementCount, int) and uElementCount > 0, \
        "uElementCount is not a positive integer larger than zero but %s" % repr(uElementCount);
    dcArrayType_by_uElementCount = gddcArrayType_by_uElementCount_by_uElementType.setdefault(cElementClass, {});
    cArrayType = dcArrayType_by_uElementCount.get(uElementCount);
    if cArrayType is None:
      sArrayTypeName = "%s[%d]" % (cElementClass.sName, uElementCount);
      cArrayType = type(sArrayTypeName, (iArrayBaseType,), {
        "_type_": cElementClass,
        "_length_": uElementCount,
        "sName": sArrayTypeName,
        "cElementClass": cElementClass,
        "uElementCount": uElementCount,
      });
      dcArrayType_by_uElementCount[uElementCount] = cArrayType;
    return cArrayType;
  
  @classmethod
  def fuGetLength(cArrayType):
    return cArrayType.uElementCount;
  
  def __init__(oSelf, *txInitialValues):
    super(iArrayBaseType, oSelf).__init__();
    if len(txInitialValues) == 0:
      pass; # do not initialize
    elif len(txInitialValues) == 1 and isinstance(txInitialValues[0], (bytes, str)):
      # Initialize with string. set any elements beyond the end of the string to 0.
      oSelf.fSetValue(txInitialValues[0], bZeroPadding = True);
    else:
      oSelf.fSetValues(*txInitialValues);
  
  def faxGetValues(oSelf):
    assert issubclass(oSelf.__class__.cElementClass, iPrimitiveBaseType), \
        "Cannot get values of %s: it is not an array of primitives, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    return [
      oSelf[uIndex].fxGetValue()
      for uIndex in range(0, oSelf.__class__.uElementCount)
    ];
        
  def fs0GetNullTerminatedString(oSelf, u0StartIndex = None):
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sb0StringValue = oSelf.fsb0GetNullTerminatedString(u0StartIndex);
    if sb0StringValue is None:
      return None; # There is no NULL terminator!
    s0Encoding = oSelf.__class__.cElementClass.s0UnicodeEncoding;
    if s0Encoding is None:
      return "".join(chr(uByte) for uByte in sb0StringValue);
    else:
      return sb0StringValue.decode(s0Encoding, "strict");
  
  def fsb0GetNullTerminatedString(oSelf, u0StartIndex = None):
    # Look for a NULL terminated string.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot get '\\0' terminated string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = 0 if u0StartIndex is None else u0StartIndex;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get '\\0' terminated bytes string from index %d in a buffer of only %d characters" % \
        (uStartIndex, oSelf.__class__.uElementCount);
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sbStringValue = b"";
    for uIndex in range(uStartIndex, oSelf.__class__.uElementCount):
      sbElementValue = oSelf[uIndex].fsbGetValue();
      if all(uByte == 0 for uByte in sbElementValue):
        return sbStringValue;
      sbStringValue += sbElementValue;
    return None; # There is no NULL terminator!
  
  def fsGetValue(oSelf, u0StartIndex = None, u0Length = None):
    # Read exactly as many characters as requested.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot get string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    sbValue = oSelf.fsbGetValue(u0StartIndex, u0Length);
    s0Encoding = oSelf.__class__.cElementClass.s0UnicodeEncoding;
    if s0Encoding is None:
      return "".join(chr(uByte) for uByte in sbValue);
    else:
      return sbValue.decode(s0Encoding, "strict");
  
  def fsbGetValue(oSelf, u0StartIndex = None, u0Length = None):
    # Read exactly as many characters as requested.
    uElementCount = oSelf.__class__.uElementCount;
    uElementSize = oSelf.__class__.cElementClass.fuGetSize();
    uStartIndex = u0StartIndex if u0StartIndex is not None else 0;
    uEndIndex = uStartIndex + u0Length if u0Length is not None else uElementCount;
    assert (
      0 <= uStartIndex < uElementCount
      and uStartIndex <= uEndIndex <= uElementCount
    ), \
        "Cannot get bytes %s%s of a %s" % (
          ("from index %d " % u0StartIndex) if u0StartIndex is not None else "",
          ("with length %d " % u0Length) if u0Length is not None else "",
          oSelf.__class__.__name__,
        );
    uNumberOfBytes = (uEndIndex - uStartIndex) * uElementSize;
    cBufferType = ctypes.c_ubyte * uNumberOfBytes;
    return bytes(cBufferType.from_buffer(oSelf, uStartIndex * uElementSize));
  
  def fSetValue(oSelf, sxValue, bZeroPadding = False):
    # Write bytes or str to array of characters, using the character class'
    # s0UnicodeEncoding property to convert a str to bytes. A single '\0'
    # terminator character is always added. bZeroPadding can be used to set any
    # characters in the array after the '\0' terminator to '\0' as well.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot initialize a %s with a string: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    s0Encoding = oSelf.__class__.cElementClass.s0UnicodeEncoding;
    if s0Encoding is None:
      assert isinstance(sxValue, bytes), \
          "A %s has no Unicode encoding and can only be set with 'bytes', not %s" % (
            oSelf.__class__.__name__,
            repr(sxValue),
          )
      sbValue = sxValue + b"\0";
    else:
      assert isinstance(sxValue, str), \
        "A %s encodes Unicode characters and can only be set with 'str', not %s" % (
          oSelf.__class__.__name__,
          repr(sxValue),
        );
      sbValue = (sxValue + "\0").encode(s0Encoding, "strict");
    uSize = oSelf.fuGetSize();
    assert len(sbValue) <= uSize, \
        "A %s can only store %d bytes, not %d (%s)" % (
          oSelf.__class__.__name__,
          uSize,
          len(sbValue),
          repr(sbValue),
        );
    aoBYTEs = (ctypes.c_ubyte * uSize).from_address(oSelf.fuGetAddress());
    for uOffset in range(len(sbValue)):
      aoBYTEs[uOffset] = sbValue[uOffset];
    if bZeroPadding:
      for uOffset in range(len(sbValue), uSize):
        aoBYTEs[uOffset] = 0;
  
  def fSetValues(oSelf, *txValues):
    # Write values to the elements in the array. The number of values must match
    # the number of elements.
    assert len(txValues) == oSelf.__class__.uElementCount, \
        "Cannot initialize an array containing %d elements with %d values" % \
        (oSelf.__class__.uElementCount, len(txInitialValues));
    for uIndex in range(len(txValues)):
      oSelf[uIndex].fSetValue(txValues[uIndex]);
  
  def fsDumpValue(oSelf, bNullTerminated = True):
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "This is only implemented for character arrays";
    sEscapedValue = "";
    uLength = None;
    uMaxCharacterCount = oSelf.__class__.uElementCount;
    for uElementIndex in range(uMaxCharacterCount):
      oChar = oSelf[uElementIndex];
      uCharCode = oChar.fuGetValue();
      if bNullTerminated and uCharCode == 0:
        uLength = uElementIndex;
        break;
      sEscapedValue += (
        "\\0" if uCharCode == 0 else
        "\\t" if uCharCode == ord('\t') else
        "\\r" if uCharCode == ord('\r') else
        "\\n" if uCharCode == ord('\n') else
        "\\n" if uCharCode == ord('\n') else
        "\\\\" if uCharCode == ord('\\') else
        "\\\"" if uCharCode == ord('\"') else
        ("\\x%02X" % uCharCode) if uCharCode < 0x20 else
        chr(uCharCode) if uCharCode < 0x100 else
        ("\\u%04X" % uCharCode)
      );
    return '"%s" (%s)' % (
             #    #
             sEscapedValue,
                  "%d/%d chars + null" % (uLength, uMaxCharacterCount)
                      if uLength is not None else
                  "%d chars (not terminated)" % uMaxCharacterCount
    );
  
  def fasDump(oSelf, s0Name = None, uOffset = 0, sPadding = "", bOutputHeader = True):
    sName = s0Name if s0Name is not None else "%s @ 0x%X" % (oSelf.__class__.sName, oSelf.fuGetAddress());
    cElementClass = oSelf.__class__.cElementClass;
    sElementTypeName = cElementClass.sName;
    uElementCount = oSelf.__class__.uElementCount;
    sElementCount = "%d" % uElementCount if uElementCount < 10 else "%d / 0x%X" % (uElementCount, uElementCount);
    if issubclass(cElementClass, iCharacterBaseType):
      sComment = oSelf.fsDumpValue();
    else:
      sComment = "";
    return  (
      (_fasGetDumpHeader() if bOutputHeader else []) +
      [_fsFormatDumpLine(
        uOffset = uOffset,
        u0Size = oSelf.__class__.fuGetSize(),
        sPadding = sPadding,
        sType = oSelf.__class__.sName,
        sName = sName,
        sComment = sComment,
      )] +
      oSelf.fasDumpValues(sName, uOffset, sPadding) +
      (_fasGetDumpFooter() if bOutputHeader else [])
    );
  
  def fasDumpValues(oSelf, sName, uOffset = 0, sPadding = ""):
    cElementClass = oSelf.__class__.cElementClass;
    sElementTypeName = cElementClass.sName;
    uElementCount = oSelf.__class__.uElementCount;
    uElementSize = cElementClass.fuGetSize();
    asDumpLines = [];
    if issubclass(cElementClass, iCharacterBaseType):
      # array of chars can be dumped in blocks
      uBlockLength = int(16 / uElementSize);
      for uBlockIndex in range(0, uElementCount, uBlockLength):
        auBlockBytes = [];
        sBlockChars = "";
        for uElementIndex in range(uBlockIndex, uBlockIndex + uBlockLength):
          if uElementIndex == uElementCount:
            break;
          oElement = oSelf[uElementIndex];
          auBlockBytes += oElement.fauGetBytes();
          uCharCode = oElement.fuGetValue();
          sBlockChars += chr(uCharCode) if 0x20 <= uCharCode < 0x100 else "."
        asDumpLines.append(_fsFormatDumpLine(
          uOffset = uOffset + (uBlockIndex * uElementSize),
          a0uBytes = auBlockBytes,
          sPadding = sPadding + ("╵ " if uBlockIndex < uElementCount - uBlockLength else "╰ "),
          sType = sElementTypeName,
          sName = "%s[%d ... %s]" % (sName, uBlockIndex, uBlockIndex + len(sBlockChars)),
          sComment = sBlockChars,
        ));
    else:
      for uElementIndex in range(uElementCount):
        oElement = oSelf[uElementIndex];
        sElementsIndex = "%d" % uElementIndex if uElementIndex < 10 else "%d / 0x%X" % (uElementIndex, uElementIndex);
        sElementName = "%s[%s]" % (sName, sElementsIndex);
        asDumpLines += oElement.fasDump(sElementName, uOffset, sPadding + "╵ ", bOutputHeader = False);
        uOffset += uElementSize;
    return asDumpLines;
  
  def __repr__(oSelf):
    if issubclass(oSelf.__class__.cElementClass, iCharacterBaseType):
      # Show (part of the) value of character array types (i.e. strings)
      sValue = repr(oSelf.fsGetValue(u0Length = min(30, oSelf.__class__.uElementCount)));
      if len(sValue) > 32:
        sValue = sValue[:28] + "…" + sValue[-3];
      sValueNotes = " " + sValue;
    else:
      sValueNotes = "";
    return "<array %s (%s bytes @ %s) = %s[%s]%s>" % (
                   #   #          #     #  #  #
                   oSelf.__class__.sName,
                       fsDumpInteger(oSelf.fuGetSize()),
                                  fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
                                        oSelf.__class__.cElementClass.sName,
                                           fsDumpInteger(oSelf.__class__.uElementCount),
                                              sValueNotes,
    );
  

from ._mDump import _fasGetDumpHeader, _fsFormatDumpLine, _fasGetDumpFooter;
from .iPrimitiveBaseType import iPrimitiveBaseType;
from .iCharacterBaseType import iCharacterBaseType;
