import ctypes, inspect;

from .fsDumpInteger import fsDumpInteger;
from .iBaseType import iBaseType;

guNamelessStructureOrUnionsCounter = 0;

class iStructureOrUnionBaseType(iBaseType):
  @classmethod
  def fcCreateClass(iStructureOrUnionType, s0Name, *axFields):
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
          cFieldClass = xField[0];
          assert issubclass(cFieldClass, iBaseType), \
              "FieldType for %s must be a type, not %s" % (sName, repr(cFieldClass));
          for uIndex in range(1, len(xField), 2):
            s0FieldName = xField[uIndex];
            if s0FieldName is None:
              sFieldName = "_anonymous_field_%d_" % len(asAnonymousFieldNames);
              asAnonymousFieldNames.append(sFieldName);
            else:
              sFieldName = s0FieldName;
            uFieldSizeInBits = xField[uIndex + 1];
            assert isinstance(sFieldName, str), \
                "FieldName for %s must be a string, not %s" % (sName, repr(sFieldName));
            assert isinstance(uFieldSizeInBits, int) and uFieldSizeInBits > 0, \
                "uFieldSizeInBits for %s must be a positive integer larger than zero, not %s" % (sName, repr(uFieldSizeInBits));
            atxFields.append((sFieldName, cFieldClass, uFieldSizeInBits));
          continue;
        cFieldClass, sFieldName = xField;
      else:
        cFieldClass = xField;
        sFieldName = "_anonymous_field_%d_" % len(asAnonymousFieldNames);
        asAnonymousFieldNames.append(sFieldName);
      from .STRUCT import STRUCT;
      from .UNION import UNION;
      from .mStructureTypes import iStructureType32, iStructureType64;
      from .mUnionTypes import iUnionType32, iUnionType64;
      if cFieldClass.__class__ in (STRUCT, UNION):
        iFieldType = {
          STRUCT: {32: iStructureType32, 64: iStructureType64},
          UNION:  {32: iUnionType32, 64: iUnionType64}
        }[cFieldClass.__class__][iStructureOrUnionType.uAlignmentInBits];
        cFieldClass = iFieldType.fcCreateClass(None, *cFieldClass.axFields);
      assert isinstance(sFieldName, str), \
          "FieldName for %s must be a string, not %s (in %s)" % (sName, repr(sFieldName), repr(xField));
      assert inspect.isclass(cFieldClass) and issubclass(cFieldClass, iBaseType), \
          "FieldType for %s.%s must be derived from iBaseType but %s is not %s(in %s)" % \
          (sName, sFieldName, repr(cFieldClass), repr(xField));
      atxFields.append((sFieldName, cFieldClass));
    
    cStructureOrUnion = type(sName, (iStructureOrUnionType,), {
      "_anonymous_": asAnonymousFieldNames,
      "_fields_": atxFields,
      "sName": sName,
    });
    
    return cStructureOrUnion;
  
  @classmethod
  def fuGetOffsetOfMember(cSelf, sFieldName):
    return getattr(cSelf, sFieldName).offset;
  
  def fasDump(oSelf, s0Name = None, uOffset = 0, sPadding = "", bOutputHeader = True):
    sName = s0Name if s0Name is not None else "@ 0x%X" % (oSelf.fuGetAddress(),);
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
    for uMemberIndex in range(len(oSelf._fields_)):
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
          sComment = "value = %s" % oMember.fsDumpValue()
        ));
    return asDumpData;
  
  def __repr__(oSelf):
    return "<%s %s (%s bytes @ %s)>" % (
             #  #   #          #
             "struct" if oSelf.bIsStructure else "union",
                oSelf.__class__.sName,
                    fsDumpInteger(oSelf.fuGetSize()),
                               fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
    );

from ._mDump import _fasGetDumpHeader, _fsFormatDumpLine, _fasGetDumpFooter;

