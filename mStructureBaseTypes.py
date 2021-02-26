import ctypes;

from .iStructureOrUnionBaseType import iStructureOrUnionBaseType;
from .uProcessBits import uProcessBits;

cCTypesStructureMetaType = type(ctypes.Structure);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateType(cSelf, uIndex);

class iStructureBaseType(iStructureOrUnionBaseType, ctypes.Structure):
  __metaclass__ = type("iStructureMetaType", (tCreateArrayMetaType, cCTypesStructureMetaType), {});
  bIsStructure = True;
  bIsUnion = False;

iStructureBaseType8 = type("iStructureBaseType8", (iStructureBaseType,), {"_pack_": 1, "uAlignmentInBits": 8});
iStructureBaseType16 = type("iStructureBaseType16", (iStructureBaseType,), {"_pack_": 2, "uAlignmentInBits": 16});
iStructureBaseType32 = type("iStructureBaseType32", (iStructureBaseType,), {"_pack_": 4, "uAlignmentInBits": 32});
iStructureBaseType64 = type("iStructureBaseType64", (iStructureBaseType,), {"_pack_": 8, "uAlignmentInBits": 64});
iStructureBaseTypeDefault = {32: iStructureBaseType32, 64: iStructureBaseType64}[uProcessBits];

from .iArrayBaseType import iArrayBaseType;
