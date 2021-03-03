import ctypes, json;

from .fsDumpInteger import fsDumpInteger;
from .iBaseType import iBaseType;

gddcArrayType_by_uElementCount_by_uElementType = {};

cCTypesArrayMetaType = type(ctypes.Array);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateClass(cSelf, uIndex);

class iArrayBaseType(iBaseType, ctypes.Array):
  _type_ = ctypes.c_bool; # Placeholder to satisfy ctypes
  _length_ = 1; # Placeholder to satisfy ctypes
  __metaclass__ = type("iArrayMetaType", (tCreateArrayMetaType, cCTypesArrayMetaType), {});
  
  @staticmethod
  def fcCreateClass(cElementClass, uElementCount):
    global gddcArrayType_by_uElementCount_by_uElementType;
    assert issubclass(cElementClass, iBaseType), \
        "cElementClass is not a type but %s" % repr(cElementClass);
    assert isinstance(uElementCount, (int, long)) and uElementCount > 0, \
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
    elif len(txInitialValues) == 1 and isinstance(txInitialValues[0], (str, unicode)):
      assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
          "Cannot initialize a %s with a string: it is not an array of characters, but of %s" % \
          (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
      # Initialize with string. set any elements beyond the end of the string to 0.
      sInitialValue = txInitialValues[0];
      for uIndex in xrange(oSelf.__class__.uElementCount):
        oSelf[uIndex].fSetValue(sInitialValue[uIndex] if uIndex < len(sInitialValue) else 0);
    else:
      assert len(txInitialValues) == oSelf.__class__.uElementCount, \
          "Cannot initialize an array containing %d elements with %d values" % \
          (oSelf.__class__.uElementCount, len(txInitialValues));
      for uIndex in xrange(len(txInitialValues)):
        oSelf[uIndex].fSetValue(txInitialValues[uIndex]);
  
  def faxGetValues(oSelf):
    assert issubclass(oSelf.__class__.cElementClass, iPrimitiveBaseType), \
        "Cannot get values of %s: it is not an array of primitives, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    return [
      oSelf[uIndex].fxGetValue()
      for uIndex in xrange(0, oSelf.__class__.uElementCount)
    ];
        
  def fsGetNullTerminatedString(oSelf, u0StartIndex = None):
    # Look for a NULL terminated string.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot get string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = 0 if u0StartIndex is None else u0StartIndex;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get string from index %d in a buffer of %d characters" % (uStartIndex, oSelf.__class__.uElementCount);
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sString = oSelf.cElementClass.sEmptyString;
    for uIndex in xrange(uStartIndex, oSelf.__class__.uElementCount):
      uCharCode = oSelf[uIndex].fuGetValue();
      if uCharCode == 0:
        return sString;
      sString += oSelf[uIndex].fsGetValue();
    return None; # There is no NULL terminator!
  
  def fsGetValue(oSelf, u0StartIndex = None, u0Length = None):
    # Read exactly as many characters as requested.
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "Cannot get string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.cElementClass.sName);
    uStartIndex = u0StartIndex if u0StartIndex is not None else 0;
    uEndIndex = uStartIndex + u0Length if u0Length is not None else oSelf.__class__.uElementCount;
    assert uStartIndex < oSelf.__class__.uElementCount, \
        "Cannot get string value from index %d in a buffer of %d characters" % (uStartIndex, oSelf.__class__.uElementCount);
    assert uEndIndex <= oSelf.__class__.uElementCount, \
        "Cannot get string from index %d with length %d in a buffer of %d characters" % (uStartIndex, u0Length, oSelf.__class__.uElementCount);
    sValue = oSelf.cElementClass.sEmptyString.join([
      oSelf[uIndex].fsGetValue()
      for uIndex in xrange(uStartIndex, uEndIndex)
    ]);
    return sValue;
  
  def fsDumpValue(oSelf, bNullTerminated = True):
    assert issubclass(oSelf.__class__.cElementClass, iCharacterBaseType), \
        "This is only implemented for character arrays";
    sEscapedValue = "";
    uLength = None;
    uMaxCharacterCount = oSelf.__class__.uElementCount;
    for uElementIndex in xrange(uMaxCharacterCount):
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
      uBlockLength = 16 / uElementSize;
      for uBlockIndex in xrange(0, uElementCount, uBlockLength):
        auBlockBytes = [];
        sBlockChars = cElementClass.sEmptyString;
        for uElementIndex in xrange(uBlockIndex, uBlockIndex + uBlockLength):
          if uElementIndex == uElementCount:
            break;
          oElement = oSelf[uElementIndex];
          auBlockBytes += oElement.fauGetBytes();
          uCharCode = oElement.fuGetValue();
          sBlockChars += chr(uCharCode) if 0x20 <= uCharCode < 0x100 else "."
        asDumpLines.append(_fsFormatDumpLine(
          uOffset = uOffset + (uBlockIndex * uElementSize),
          a0uBytes = auBlockBytes,
          sPadding = sPadding + ("| " if uBlockIndex < uElementCount - uBlockLength else "`-"),
          sType = sElementTypeName,
          sName = "%s[%d ... %s]" % (sName, uBlockIndex, uBlockIndex + len(sBlockChars)),
          sComment = sBlockChars,
        ));
    else:
      for uElementIndex in xrange(uElementCount):
        oElement = oSelf[uElementIndex];
        sElementsIndex = "%d" % uElementIndex if uElementIndex < 10 else "%d / 0x%X" % (uElementIndex, uElementIndex);
        sElementName = "%s[%s]" % (sName, sElementsIndex);
        asDumpLines += oElement.fasDump(sElementName, uOffset, sPadding + ": ", bOutputHeader = False);
        uOffset += uElementSize;
    return asDumpLines;
  
  def __repr__(oSelf):
    if issubclass(oSelf.__class__.cElementClass, iCharacterBaseType):
      # Show (part of the) value of character array types (i.e. strings)
      sValue = repr(oSelf.fsGetValue(u0Length = min(30, oSelf.__class__.uElementCount)));
      if len(sValue) > 32:
        sValue = sValue[:28] + "..." + sValue[-1];
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
