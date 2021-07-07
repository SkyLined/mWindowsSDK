import ctypes;

from .iStructureOrUnionBaseType import iStructureOrUnionBaseType;

cCTypesUnionMetaType = type(ctypes.Union);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateClass(cSelf, uIndex);

class iUnionBaseType(iStructureOrUnionBaseType, ctypes.Union, metaclass=type("iUnionMetaType", (tCreateArrayMetaType, cCTypesUnionMetaType), {})):
  
  bIsStructure = False;
  bIsUnion = True;

from .iArrayBaseType import iArrayBaseType;
