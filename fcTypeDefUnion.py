import ctypes;
from ._fcTypeDefStructureOrUnion import _fcTypeDefStructureOrUnion;

def fcTypeDefUnion(sName, *axFields, **dxOption_by_sName):
  return _fcTypeDefStructureOrUnion(ctypes.Union, sName, axFields, **dxOption_by_sName);

