import ctypes, inspect;

from .iDataBaseType import iDataBaseType;

guNamelessStructureOrUnionsCounter = 0;

class iStructureOrUnionBaseType(iDataBaseType):
  @classmethod
  def fcCreateType(iStructureOrUnionBaseType, s0Name, *axFields):
    global guNamelessStructureOrUnionsCounter;
    if s0Name:
      sName = s0Name;
    else:
      guNamelessStructureOrUnionsCounter += 1;
      sName = "unnamed_%d" % guNamelessStructureOrUnionsCounter;
    asAnonymousFieldNames = [];
    atxFields = [];
    for xField in axFields:
      if isinstance(xField, tuple):
        if len(xField) > 2:
          # (TYPE, NAME, SIZE IN BITS[, NAME, SIZE IN BITS[, ...]])
          cFieldType = xField[0];
          assert issubclass(cFieldType, iDataBaseType), \
              "FieldType for %s must be a type, not %s" % (sName, repr(cFieldType));
          for uIndex in xrange(1, len(xField), 2):
            s0FieldName = xField[uIndex];
            if s0FieldName is None:
              sFieldName = "_anonymous_field_%d_" % len(asAnonymousFieldNames);
              asAnonymousFieldNames.append(sFieldName);
            else:
              sFieldName = s0FieldName;
            uFieldSizeInBits = xField[uIndex + 1];
            assert isinstance(sFieldName, str), \
                "FieldName for %s must be a string, not %s" % (sName, repr(sFieldName));
            assert isinstance(uFieldSizeInBits, (int, long)) and uFieldSizeInBits > 0, \
                "uFieldSizeInBits for %s must be a positive integer larger than zero, not %s" % (sName, repr(uFieldSizeInBits));
            atxFields.append((sFieldName, cFieldType, uFieldSizeInBits));
          continue;
        cFieldType, sFieldName = xField;
      else:
        cFieldType = xField;
        sFieldName = "_anonymous_field_%d_" % len(asAnonymousFieldNames);
        asAnonymousFieldNames.append(sFieldName);
      from .STRUCT import STRUCT;
      from .UNION import UNION;
      from mStructureBaseTypes import iStructureBaseType32, iStructureBaseType64;
      from mUnionBaseTypes import iUnionBaseType32, iUnionBaseType64;
      if cFieldType.__class__ in (STRUCT, UNION):
        iFieldBaseType = {
          STRUCT: {32: iStructureBaseType32, 64: iStructureBaseType64},
          UNION:  {32: iUnionBaseType32, 64: iUnionBaseType64}
        }[cFieldType.__class__][iStructureOrUnionBaseType.uAlignmentInBits];
        cFieldType = iFieldBaseType.fcCreateType(None, *cFieldType.axFields);
      assert isinstance(sFieldName, str), \
          "FieldName for %s must be a string, not %s (in %s)" % (sName, repr(sFieldName), repr(xField));
      assert inspect.isclass(cFieldType) and issubclass(cFieldType, iDataBaseType), \
          "FieldType for %s.%s must be derived from iDataBaseType but %s is not %s(in %s)" % \
          (sName, sFieldName, repr(cFieldType), repr(xField));
      atxFields.append((sFieldName, cFieldType));
    
    cStructureOrUnion = type(sName, (iStructureOrUnionBaseType,), {
      "_anonymous_": asAnonymousFieldNames,
      "_fields_": atxFields,
      "sName": sName,
    });
    
    return cStructureOrUnion;
  
  @classmethod
  def fuGetOffsetOfMember(cSelf, sFieldName):
    return getattr(cSelf, sFieldName).offset;
  
  def fasDump(oSelf, s0Name = None, uOffset = 0, sPadding = "", bOutputHeader = True):
    sName = s0Name if s0Name is not None else "%s @ 0x%X" % (oSelf.__class__.sName, oSelf.fuGetAddress());
    return  (
      (_fasGetDumpHeader() if bOutputHeader else []) +
      [_fsFormatDumpLine(
        uOffset = uOffset,
        u0Size = oSelf.__class__.fuGetSize(),
        sPadding = sPadding,
        sType = oSelf.__class__.sName,
        sName = sName,
        sComment =  "%d bits aligned" % oSelf.__class__.uAlignmentInBits,
      )] +
      oSelf.fasDumpContent(uOffset, sPadding) +
      (_fasGetDumpFooter() if bOutputHeader else [])
    );
  
  def fasDumpContent(oSelf, uOffset = 0, sPadding = ""):
    asDumpData = [];
    for uMemberIndex in xrange(len(oSelf._fields_)):
      xMember = oSelf._fields_[uMemberIndex];
      if len(xMember) == 2:
        (sMemberName, cMemberType) = xMember;
        oMember = getattr(oSelf, sMemberName);
        uMemberOffset = uOffset + oSelf.__class__.fuGetOffsetOfMember(sMemberName);
        asDumpData += oMember.fasDump(sMemberName, uMemberOffset, sPadding + ": ", bOutputHeader = False);
      else:
        (sMemberName, cMemberType, uMemberBits) = xMember;
        cBitFieldType = getattr(oSelf.__class__, sMemberName);
        uMemberBitsOffset = cBitFieldType.size & 0xFFFF;
        oMember = getattr(oSelf, sMemberName);
        asDumpData.append(_fsFormatDumpLine(
          uOffset = uOffset + oSelf.fuGetOffsetOfMember(sMemberName),
          u0BitsOffset = uMemberBitsOffset,
          u0BitsSize = uMemberBits,
          sPadding = sPadding + ": ",
          sType = "bitfield",
          sName = sMemberName,
          sValue = oMember.fsDumpValue()
        ));
    return asDumpData;
  
  def __repr__(oSelf):
    return "<%s %s:%d @ 0x%X>" % (
      "struct" if oSelf.bIsStructure else "union",
      oSelf.__class__.sName,
      oSelf.fuGetSize(),
      oSelf.fuGetAddress(),
    );

from ._mDump import _fasGetDumpHeader, _fsFormatDumpLine, _fasGetDumpFooter;

