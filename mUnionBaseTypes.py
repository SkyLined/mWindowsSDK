import ctypes;

from .iStructureOrUnionBaseType import iStructureOrUnionBaseType;
from .uProcessBits import uProcessBits;

cCTypesUnionMetaType = type(ctypes.Union);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateType(cSelf, uIndex);

class iUnionBaseType(iStructureOrUnionBaseType, ctypes.Union):
  __metaclass__ = type("iUnionMetaType", (tCreateArrayMetaType, cCTypesUnionMetaType), {});
  bIsStructure = False;
  bIsUnion = True;

iUnionBaseType8 = type("iUnionBaseType8", (iUnionBaseType,), {"_pack_": 1, "uAlignmentInBits": 8});
iUnionBaseType16 = type("iUnionBaseType16", (iUnionBaseType,), {"_pack_": 2, "uAlignmentInBits": 16});
iUnionBaseType32 = type("iUnionBaseType32", (iUnionBaseType,), {"_pack_": 4, "uAlignmentInBits": 32});
iUnionBaseType64 = type("iUnionBaseType64", (iUnionBaseType,), {"_pack_": 8, "uAlignmentInBits": 64});
iUnionBaseTypeDefault = {32: iUnionBaseType32, 64: iUnionBaseType64}[uProcessBits];

 
from .iArrayBaseType import iArrayBaseType;
