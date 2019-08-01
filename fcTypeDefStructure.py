import ctypes;
from ._fcTypeDefStructureOrUnion import _fcTypeDefStructureOrUnion;

def fcTypeDefStructure(sName, *axFields, **dxOption_by_sName):
  return _fcTypeDefStructureOrUnion(ctypes.Structure, sName, axFields, **dxOption_by_sName);
