from ..mStructureTypes import iStructureType;
from ..STRUCT import STRUCT;
from ..UNION import UNION;
from .mConstants import *;
from .mPrimitives import *;

from ..mWindowsStructures import __all__ as asWindowsStructureNames;
from ..mWindowsStructures import *;
__all__ = asWindowsStructureNames[:];

def fExportStructure(sName, *atxFields):
  cStructure = iStructureType.fcCreateClass(sName, *atxFields);
  cStructurePointer = cStructure.fcCreatePointer();
  globals()[sName] = cStructure; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.
  # Also create "P" + name as a pointer to this type:
  globals()["P" + sName] = cStructurePointer; # Make it available in the context of this file
  __all__.append("P" + sName); # Make it available as an export from this module.

# Add additional structures here using fExportStructure:
