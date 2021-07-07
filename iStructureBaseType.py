import ctypes;

from .iStructureOrUnionBaseType import iStructureOrUnionBaseType;

cCTypesStructureMetaType = type(ctypes.Structure);

class tCreateArrayMetaType(object):
  _type_ = "X"; # Placeholder to satisfy ctypes
  def __getitem__(cSelf, uIndex):
    return iArrayBaseType.fcCreateClass(cSelf, uIndex);

class iStructureBaseType(iStructureOrUnionBaseType, ctypes.Structure, metaclass=type("iStructureMetaType", (tCreateArrayMetaType, cCTypesStructureMetaType), {})):
  
  bIsStructure = True;
  bIsUnion = False;

from .iArrayBaseType import iArrayBaseType;
