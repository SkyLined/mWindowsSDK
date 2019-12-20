import ctypes;
from iType import iType;

def fasDumpStructureOrUnionHelper(uOffset, uDepth, oStructureOrUnion, auBytes):
  from .cCharacterType import cCharacterType;
  from .cFloatType import cFloatType;
  from .cIntegerType import cIntegerType;
  from .cPointerType import cPointerType;
  from .cStructureType import cStructureType;
  from .cUnionType import cUnionType;
  asDumpData = [];
  for (sMemberName, cMemberType) in oStructureOrUnion._fields_:
    oMember = getattr(oStructureOrUnion, sMemberName);
    uMemberOffset = uOffset + oStructureOrUnion.fuGetOffsetOfMember(sMemberName);
    uMemberSize = ctypes.sizeof(cMemberType);
    sPadding = "  " * uDepth;
    sHeaderFormat = "  %%4X|%%4X|%-23s|%18s|%%-40s|%%s" % ("", "");
    sValueFormat = "  %4X|%4X|%-23s|%18s|%-40s|%s";
    if isinstance(oMember, (cStructureType, cUnionType)):
      sMemberType = " ".join([s for s in [
        "struct" if isinstance(oMember, cStructureType) else "union",
        cMemberType.sName,
      ] if s is not None]);
      asDumpData.extend([
        sHeaderFormat % (uMemberOffset, uMemberSize, sPadding + sMemberName, sPadding + sMemberType),
      ] + fasDumpStructureOrUnionHelper(uMemberOffset, uDepth + 1, oMember, auBytes));
    elif isinstance(oMember, ctypes.Array):
      cElementType = oMember._type_;
      uNumberOfElements = oMember._length_;
      sNumberOfElements = "%d" % uNumberOfElements if uNumberOfElements < 10 else "%d/0x%X" % (uNumberOfElements, uNumberOfElements);
      sElementTypeName = cElementType.sName;
      asDumpData.append(sHeaderFormat % (uMemberOffset, uMemberSize, sPadding + sMemberName, "%s%s [%s]" % (sPadding, sElementTypeName, sNumberOfElements)));
      uElementSize = cElementType.fuGetSize();
      for uElementIndex in xrange(uNumberOfElements):
        sElementIndex = uElementIndex < 10 and ("[%d]" % uElementIndex) or ("[%d/0x%X]" % (uElementIndex, uElementIndex));
        uElementOffset = uMemberOffset + uElementIndex * uElementSize
        sElementBytes = " ".join(["%02X" % auBytes[uByteOffset] for uByteOffset in xrange(uElementOffset, uElementOffset + uElementSize)]);
        sElementValue = "%s%X" % (oMember[uElementIndex] < 0 and "-" or "", abs(oMember[uElementIndex]));
        asDumpData.append(sValueFormat % (uElementOffset, uElementSize, sElementBytes, sElementValue, sPadding + "  " + sElementIndex, ""));
    else:
      sMemberBytes = " ".join(["%02X" % auBytes[uByteOffset] for uByteOffset in xrange(uMemberOffset, uMemberOffset + uMemberSize)]);
      if isinstance(oMember, cPointerType):
        uTargetAddress = oMember.value;
        sValue = "0x%X" % uTargetAddress if uTargetAddress != 0 else "NULL";
      elif isinstance(oMember, cCharacterType):
        sValue = "%s '%s'" % (
          {1:"%02X", 2:"%04X"}[uMemberSize] % oMember.value,
          "\\%s" % chr(oMember.value) if oMember.value in (ord("'"), ord("\\"))
              else chr(oMember.value) if oMember.value >= 0x20 and oMember.value < 0x7F
              else "."
        );
      elif isinstance(oMember, cFloatType):
        sValue = "%d" % (oMember.value);
      else:
        assert isinstance(oMember, cIntegerType), \
            "Unhandled member type %s = %s" % (sMemberName, repr(cMemberType));
        if abs(oMember.value) < 10:
          sValue = "%d" % oMember.value;
        elif abs(oMember.value) < 0x10000:
          sValue = "%d/0x%X" % (oMember.value, (oMember.value + (1 < (uMemberSize * 8) if oMember.value < 0 else 0)));
        else:
          sValue = "0x%X" % (oMember.value + (1 < (uMemberSize * 8) if oMember.value < 0 else 0));
      asDumpData.append(sValueFormat % (uMemberOffset, uMemberSize, sMemberBytes, sValue, sPadding + sMemberName, sPadding + cMemberType.sName));
  return asDumpData;

class iStructureOrUnionType(iType):
  @classmethod
  def fuGetOffsetOfMember(cSelf, sFieldName):
    return getattr(cSelf, sFieldName).offset;
  
  def fasDump(oSelf, sName = None):
    sTypeName = " ".join([s for s in [
      "struct" if isinstance(oSelf, ctypes.Structure) else "union",
      sName or oSelf.sName,
    ] if s is not None]);
    uAlignmentInBits = oSelf.uAlignmentInBits;
    uSize = oSelf.fuGetSize();
    auBytes = oSelf.fauGetByteArray();
    return [
      "%s { // %d bits aligned" % (sTypeName, uAlignmentInBits),
      "//%4s|%4s|%-23s|%18s|%-40s|%s" % ("Off.", "Size", "Bytes", "Value", "Name", "Type"),
    ] + fasDumpStructureOrUnionHelper(0, 0, oSelf, auBytes) + [
      "} // size is %s bytes" % ("%d" % uSize if uSize < 10 else "%d/0x%X" % (uSize, uSize)),
    ];

  def __repr__(oSelf):
    from cStructureType import cStructureType;
    return "<%s %s:%d @ 0x%X>" % (
      "struct" if isinstance(oSelf, cStructureType) else "union",
      oSelf.__class__.sName,
      oSelf.fuGetSize(),
      oSelf.fuGetAddress(),
    );

