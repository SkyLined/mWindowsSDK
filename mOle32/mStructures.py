from ..mStructureTypes import iStructureType;
from ..STRUCT import STRUCT;
from ..UNION import UNION;
from .mConstants import *;
from .mPrimitives import *;

from ..mWindowsStructures import __all__ as asWindowsStructureNames;
from ..mWindowsStructures import *;
__all__ = asWindowsStructureNames[:];

def fExport(sName, cType):
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

def fExportWithPointers(sName, cType):
  fExport(sName, cType);
  # Also create "P" + name as a pointer to this type:
  fExport("P" + sName, cType.fcCreatePointer());
  fExport("LP" + sName, cType.fcCreatePointer());
  fExport("PP" + sName, cType.fcCreatePointer().fcCreatePointer());

def fExportStructure(sName, *atxFields):
  cStructure = iStructureType.fcCreateClass(sName, *atxFields);
  fExportWithPointers(sName, cStructure);

def fExportAlias(sName, cBaseType):
  cType = type(sName, (cBaseType,), {
    "sName": sName,
    "__module__": cBaseType.__module__,
  });
  fExportWithPointers(sName, cType);

# Add additional structures here using fExportStructure:

#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
fExportStructure("GUID",
  (DWORD,       "Data1"),
  (WORD,        "Data2"),
  (WORD,        "Data3"),
  (BYTE[8],     "Data4"),
);
fExportAlias("REFGUID", PGUID);
fExportAlias("CLSID", GUID);
fExportAlias("REFCLSID", PCLSID);
fExportAlias("IID", GUID);
fExportAlias("IID_ISpVoice", IID);
fExportAlias("REFIID", PIID);

fExportStructure("VFTABLE_IUnknown", # The most basic Virtual Function Table
  (PVOID,   "pQueryInterface"),
  (PVOID,   "pAddRef"),
  (PVOID,   "pRelease"),
);

fExportStructure("IUnknown",
  (PVFTABLE_IUnknown, "pVFTable"),
);
fExportAlias("LPUNKNOWN", PIUnknown);
