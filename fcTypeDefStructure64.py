import ctypes;
from ._fcTypeDefStructureOrUnion import _fcTypeDefStructureOrUnion;

def fcTypeDefStructure64(sName, *axFields):
  return _fcTypeDefStructureOrUnion(ctypes.Structure, sName, axFields, uAlignmentInBits = 64);

