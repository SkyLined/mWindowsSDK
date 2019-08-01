import ctypes, platform;
from .STRUCT import STRUCT;
from .UNION import UNION;
from .cStructureType import cStructureType;
from .cUnionType import cUnionType;

guDefaultAlignmentBits = {"32bit": 32, "64bit": 64}[platform.architecture()[0]];
guNamelessStructureOrUnionsCounter = 0;

def _fcTypeDefStructureOrUnion(cBaseType, sName, axFields, uAlignmentInBits = None):
  if uAlignmentInBits == None:
    uAlignmentInBits = guDefaultAlignmentBits;
  else:
    assert uAlignmentInBits in [8, 16, 32, 64], \
        "Invalid uAlignmentInBits value %s" % repr(uAlignmentInBits);
  global guNamelessStructureOrUnionsCounter;
  sClassName = "%s_%s" % (
    cBaseType.__name__.lower(),
    sName or "unnamed_%d" % guNamelessStructureOrUnionsCounter,
  );
  if not sName:
    guNamelessStructureOrUnionsCounter += 1;
  asAnonymousFieldNames = [];
  atxFields = [];
  for xField in axFields:
    if isinstance(xField, tuple):
      cFieldType, sFieldName = xField;
    else:
      cFieldType = xField;
      sFieldName = "_anonymous_field_%d_" % len(asAnonymousFieldNames);
      asAnonymousFieldNames.append(sFieldName);
    if cFieldType.__class__ is STRUCT:
      cFieldType = _fcTypeDefStructureOrUnion(ctypes.Structure, None, cFieldType.axFields, uAlignmentInBits);
    if cFieldType.__class__ is UNION:
      cFieldType = _fcTypeDefStructureOrUnion(ctypes.Union, None, cFieldType.axFields, uAlignmentInBits);
    atxFields.append((sFieldName, cFieldType));
  
  cStructureOrUnionType = cStructureType if cBaseType == ctypes.Structure else cUnionType;
  
  cStructureOrUnion = type(sClassName, (cBaseType, cStructureOrUnionType), {});
  cStructureOrUnion._pack_ = uAlignmentInBits / 8;
  cStructureOrUnion._anonymous_ = asAnonymousFieldNames;
  cStructureOrUnion._fields_ = atxFields;
  
  cStructureOrUnion.sName = sName;
  cStructureOrUnion.uAlignmentInBits = uAlignmentInBits;
  
  return cStructureOrUnion;
