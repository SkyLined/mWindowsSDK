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
    mDebugOutput_HideInCallStack = True;
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
    mDebugOutput_HideInCallStack = True;
    super(iArrayBaseType, oSelf).__init__();
    if len(txInitialValues) == 0:
      pass; # do not initialize
    elif len(txInitialValues) == 1 and isinstance(txInitialValues[0], (bytes, str)):
      assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
          "Cannot initialize a %s with a string: it is not an array of characters, but of %s" % \
          (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
      # Initialize with string. set any elements beyond the end of the string to 0.
      sxInitialValue = txInitialValues[0];
      for uIndex in range(oSelf.__class__.uElementCount):
        oSelf[uIndex].fSetValue(sxInitialValue[uIndex] if uIndex < len(sxInitialValue) else 0);
    else:
      assert len(txInitialValues) == oSelf.__class__.uElementCount, \
          "Cannot initialize an array containing %d elements with %d values" % \
          (oSelf.__class__.uElementCount, len(txInitialValues));
      for uIndex in range(len(txInitialValues)):
        oSelf[uIndex].fSetValue(txInitialValues[uIndex]);
  
  def faxGetValues(oSelf):
    mDebugOutput_HideInCallStack = True;
    assert issubclass(oSelf.__class__.cElementClass, iPrimitiveBaseType), \
        "Cannot get values of %s: it is not an array of primitives, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    return [
      oSelf[uIndex].fxGetValue()
      for uIndex in range(0, oSelf.__class__.uElementCount)
    ];
        
  def fsGetNullTerminatedString(oSelf, u0StartIndex = None):
    mDebugOutput_HideInCallStack = True;
    # Look for a NULL terminated string.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot get '\\0' terminated string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = 0 if u0StartIndex is None else u0StartIndex;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get '\\0' terminated string from index %d in a buffer of only %d characters" % \
        (uStartIndex, oSelf.__class__.uElementCount);
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sString = "";
    for uIndex in range(uStartIndex, oSelf.__class__.uElementCount):
      uCharCode = oSelf[uIndex].fuGetValue();
      if uCharCode == 0:
        return sString;
      sString += oSelf[uIndex].fsGetValue();
    return None; # There is no NULL terminator!
  
  def fsbGetNullTerminatedBytesString(oSelf, u0StartIndex = None):
    mDebugOutput_HideInCallStack = True;
    # Look for a NULL terminated string.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType) and Self.__class__.cElementClass.fuGetSize() == 1, \
        "Cannot get '\\0' terminated bytes string value of %s: it is not an array of byte-sized characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = 0 if u0StartIndex is None else u0StartIndex;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get '\\0' terminated bytes string from index %d in a buffer of only %d characters" % \
        (uStartIndex, oSelf.__class__.uElementCount);
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sbString = b"";
    for uIndex in range(uStartIndex, oSelf.__class__.uElementCount):
      uCharCode = oSelf[uIndex].fuGetValue();
      if uCharCode == 0:
        return sbString;
      sbString += oSelf[uIndex].fsbGetValue();
    return None; # There is no NULL terminator!
  
  def fsGetValue(oSelf, u0StartIndex = None, u0Length = None):
    mDebugOutput_HideInCallStack = True;
    # Read exactly as many characters as requested.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot get string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = u0StartIndex if u0StartIndex is not None else 0;
    uEndIndex = uStartIndex + u0Length if u0Length is not None else oSelf.__class__.uElementCount;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get string value from index %d in a buffer of %d characters" % \
        (uStartIndex, oSelf.__class__.uElementCount);
    assert uEndIndex <= oSelf.__class__.uElementCount, \
        "Cannot get string from index %d with length %d in a buffer of %d characters" % \
        (uStartIndex, u0Length, oSelf.__class__.uElementCount);
    sValue = "".join([
      oSelf[uIndex].fsGetValue()
      for uIndex in range(uStartIndex, uEndIndex)
    ]);
    return sValue;
  
  def fsbGetValue(oSelf, u0StartIndex = None, u0Length = None):
    mDebugOutput_HideInCallStack = True;
    # Read exactly as many characters as requested.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType) and oSelf.__class__.cElementClass.fuGetSize() == 1, \
        "Cannot get bytes string value of %s: it is not an array of byte-sized characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = u0StartIndex if u0StartIndex is not None else 0;
    uEndIndex = uStartIndex + u0Length if u0Length is not None else oSelf.__class__.uElementCount;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get bytes string value from index %d in a buffer of %d characters" % \
        (uStartIndex, oSelf.__class__.uElementCount);
    assert uEndIndex <= oSelf.__class__.uElementCount, \
        "Cannot get bytes string from index %d with length %d in a buffer of %d characters" % \
        (uStartIndex, u0Length, oSelf.__class__.uElementCount);
    sbValue = bytes(
      oSelf[uIndex].fuGetValue()
      for uIndex in range(uStartIndex, uEndIndex)
    );
    return sbValue;
  
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
