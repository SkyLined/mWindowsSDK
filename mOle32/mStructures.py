from ..mStructureTypes import iStructureType;
from ..STRUCT import STRUCT;
from ..UNION import UNION;
from ..mWindowsStructures import *;
from .mConstants import *;
from .mPrimitives import *;

__all__ = [];

def fExportStructure(sName, *atxFields):
  cStructure = iStructureType.fcCreateClass(sName, *atxFields);
  cStructurePointer = cStructure.fcCreatePointer();
  globals()[sName] = cStructure; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.
  # Also create "P" + name as a pointer to this type:
  globals()["P" + sName] = cStructurePointer; # Make it available in the context of this file
  __all__.append("P" + sName); # Make it available as an export from this module.

#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
fExportStructure("GUID",
  (DWORD,       "Data1"),
  (WORD,        "Data2"),
  (WORD,        "Data3"),
  (BYTE[8],     "Data4"),
);
fExportPointer("REFGUID", GUID);
fExportAlias("CLSID", GUID);
fExportPointer("REFCLSID", CLSID);
fExportAlias("IID", GUID);
fExportAlias("IID_ISpVoice", IID);
fExportPointer("REFIID", IID);

fExportStructure("VFTABLE_IUnknown", # The most basic Virtual Function Table
  (PVOID, pQueryInterface),
  (PVOID, pAddRef),
  (PVOID, pRelease),
);

fExportStructure("IUnknown",
  (PVFTABLE_IUnknown, pVFTable),
);
fExportAlias("LPUNKNOWN", PIUnknown);
