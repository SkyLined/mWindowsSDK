import ctypes, inspect;

from .fsDumpInteger import fsDumpInteger;
from .iBaseType import iBaseType;

guNamelessStructureOrUnionsCounter = 0;

class iStructureOrUnionBaseType(iBaseType):
  @classmethod
  def fcCreateClass(iStructureOrUnionType, s0Name, *axFields):
    global guNamelessStructureOrUnionsCounter;
    bUnnamed = s0Name is None;
    if bUnnamed:
      guNamelessStructureOrUnionsCounter += 1;
      sTypeName = "unnamed_%d" % guNamelessStructureOrUnionsCounter;
    else:
      sTypeName = s0Name;
    asAnonymousFieldNames = [];
    atxFields = [];
    for xField in axFields:
      if isinstance(xField, tuple):
        if len(xField) > 2:
          # (TYPE, NAME, SIZE IN BITS[, NAME, SIZE IN BITS[, ...]])
          cFieldClass = xField[0];
          assert issubclass(cFieldClass, iBaseType), \
              "FieldType for %s must be a type, not %s" % (sTypeName, repr(cFieldClass));
          for uIndex in range(1, len(xField), 2):
            s0FieldName = xField[uIndex];
            if s0FieldName is None:
              sFieldName = "_anonymous_field_%d_" % len(asAnonymousFieldNames);
              asAnonymousFieldNames.append(sFieldName);
            else:
              sFieldName = s0FieldName;
            uFieldSizeInBits = xField[uIndex + 1];
            assert isinstance(sFieldName, str), \
                "FieldName for %s must be a string, not %s" % (sTypeName, repr(sFieldName));
            assert isinstance(uFieldSizeInBits, int) and uFieldSizeInBits > 0, \
                "uFieldSizeInBits for %s must be a positive integer larger than zero, not %s" % (sTypeName, repr(uFieldSizeInBits));
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
          "FieldName for %s must be a string, not %s (in %s)" % (sTypeName, repr(sFieldName), repr(xField));
      assert inspect.isclass(cFieldClass) and issubclass(cFieldClass, iBaseType), \
          "FieldType for %s.%s must be derived from iBaseType but %s is %s (in %s)" % \
          (sTypeName, sFieldName, repr(cFieldClass), repr(type(cFieldClass)), repr(xField));
      atxFields.append((sFieldName, cFieldClass));
    
    cStructureOrUnion = type(sTypeName, (iStructureOrUnionType,), {
      "_anonymous_": asAnonymousFieldNames,
      "_fields_": atxFields,
      "sName": sTypeName,
      "bUnnamed": bUnnamed,
    });
    
    return cStructureOrUnion;
  
  @classmethod
  def fuGetOffsetOfMember(cSelf, sFieldName):
    return getattr(cSelf, sFieldName).offset;
  
  def fasDump(oSelf,
    s0Name = None,
    uOffset = 0,
    sPadding = "",
    sPaddingLastLine = "",
    bOutputHeader = True,
  ):
    sName = s0Name if s0Name is not None else "@ 0x%X" % (oSelf.fuGetAddress(),);
    if oSelf.bUnnamed:
      sTypeName = "STRUCT" if oSelf.bIsStructure else "UNION";
    else:
      sTypeName = oSelf.__class__.sName;
    return  (
      (_fasGetDumpHeader() if bOutputHeader else []) +
      [_fsFormatDumpLine(
        uOffset = uOffset,
        u0Size = oSelf.__class__.fuGetSize(),
        sPadding = sPadding,
        sType = sTypeName,
        sName = sName,
        sComment =  "// %d bits aligned" % oSelf.__class__.uAlignmentInBits,
      )] +
      oSelf.fasDumpContent(
        uOffset = uOffset,
        sPadding = sPadding,
        sPaddingLastLine = sPaddingLastLine,
      ) +
      (_fasGetDumpFooter() if bOutputHeader else [])
    );
  
  def fasDumpContent(oSelf,
    uOffset = 0,
    sPadding = "",
    sPaddingLastLine = "",
  ):
    asDumpData = [];
    for uMemberIndex in range(len(oSelf._fields_)):
      xMember = oSelf._fields_[uMemberIndex];
      bIsLastMember = uMemberIndex == len(oSelf._fields_) - 1;
      sIndentedPadding = sPadding + "╵ ";
      sIndentedPaddingLastLine = (sPaddingLastLine + "└ ") if bIsLastMember else sIndentedPadding;
      if len(xMember) == 2:
        (sMemberName, cMemberType) = xMember;
        oMember = getattr(oSelf, sMemberName);
        uMemberOffset = uOffset + oSelf.__class__.fuGetOffsetOfMember(sMemberName);
        asDumpData += oMember.fasDump(
          s0Name = "" if sMemberName in oSelf._anonymous_ else sMemberName,
          uOffset = uMemberOffset,
          sPadding = sIndentedPadding,
          sPaddingLastLine = sIndentedPaddingLastLine,
          bOutputHeader = False,
        );
      else:
        (sMemberName, cMemberType, uMemberBits) = xMember;
        cBitFieldType = getattr(oSelf.__class__, sMemberName);
        uMemberBitsOffset = cBitFieldType.size & 0xFFFF;
        oMember = getattr(oSelf, sMemberName);
        asDumpData.append(_fsFormatDumpLine(
          uOffset = uOffset + oSelf.fuGetOffsetOfMember(sMemberName),
          u0BitsOffset = uMemberBitsOffset,
          u0BitsSize = uMemberBits,
          sPadding = sIndentedPaddingLastLine,
          sType = "bitfield",
          sName = "" if sMemberName in oSelf._anonymous_ else sMemberName,
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

