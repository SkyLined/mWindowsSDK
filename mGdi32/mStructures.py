from ..mStructureTypes import iStructureType;
from ..STRUCT import STRUCT;
from ..UNION import UNION;
from .mConstants import \
    CCHDEVICENAME, \
    CCHFORMNAME;
from .mPrimitiveTypes import \
    BYTE, \
    D3DDDI_VIDEO_PRESENT_SOURCE_ID, \
    D3DGPU_VIRTUAL_ADDRESS, \
    D3DKMT_HANDLE, \
    D3DKMT_CLIENTHINT, \
    DWORD, \
    HDC, \
    PVOID, \
    SHORT, \
    UINT, \
    WCHAR, WORD;
from ..mWindowsStructures import \
    POINTL;

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

fExportStructure("D3DDDI_ALLOCATIONLIST",
  (D3DKMT_HANDLE,             "hAllocation"),
  UNION(
    STRUCT(
      (UINT,                  "WriteOperation", 1,
                              "DoNotRetireInstance", 1,
                              "OfferPriority", 3,
                              "Reserved", 27),
    ),
    (UINT,                    "Value"),
  ),
);
fExportStructure("D3DDDI_CREATECONTEXTFLAGS",
  UNION(
    STRUCT(
      (UINT,                  "NullRendering", 1,
                              "InitialData", 1,
                              "DisableGpuTimeout", 1,
                              "SynchronizationOnly", 1,
                              "HwQueueSupported", 1,
                              "Reserved", 27),
    ),
    (UINT,                     "Value"),
  ),
);
fExportStructure("D3DDDI_PATCHLOCATIONLIST",
  (UINT,                      "AllocationIndex"),
  UNION(
    STRUCT(
      (UINT,                  "SlotId", 24,
                              "Reserved", 8),
    ),
    (UINT,                    "Value"),
  ),
  (UINT,                      "DriverId"),
  (UINT,                      "AllocationOffset"),
  (UINT,                      "PatchOffset"),
  (UINT,                      "SplitOffset"),
);
fExportStructure("D3DKMT_OPENADAPTERFROMHDC",
  (HDC,                            "hDc"),
  (D3DKMT_HANDLE,                  "hAdapter"),
  (LUID,                           "AdapterLuid"),
  (D3DDDI_VIDEO_PRESENT_SOURCE_ID, "VidPnSourceId"),
);
fExportStructure("D3DKMT_CREATECONTEXT",
  (D3DKMT_HANDLE,              "hDevice"),
  (UINT,                       "NodeOrdinal"),
  (UINT,                       "EngineAffinity"),
  (D3DDDI_CREATECONTEXTFLAGS,  "Flags"),
  (PVOID,                      "pPrivateDriverData"),
  (UINT,                       "PrivateDriverDataSize"),
  (D3DKMT_CLIENTHINT,          "ClientHint"),
  (D3DKMT_HANDLE,              "hContext"),
  (PVOID,                      "pCommandBuffer"),
  (UINT,                       "CommandBufferSize"),
  (PD3DDDI_ALLOCATIONLIST,     "pAllocationList"),
  (UINT,                       "AllocationListSize"),
  (PD3DDDI_PATCHLOCATIONLIST,  "pPatchLocationList"),
  (UINT,                       "PatchLocationListSize"),
  (D3DGPU_VIRTUAL_ADDRESS,     "CommandBuffer"),
);
fExportStructure("D3DKMT_CREATEDEVICEFLAGS",
  (UINT,                      "LegacyMode", 1,
                              "RequestVSync", 1,
                              "DisableGpuTimeout", 1,
                              "Reserved", 29),
);
fExportStructure("D3DKMT_CREATEDEVICE",
  UNION(
    (D3DKMT_HANDLE,           "hAdapter"),
    (PVOID,                   "pAdapter"),
  ),
  (D3DKMT_CREATEDEVICEFLAGS,  "Flags"),
  (D3DKMT_HANDLE,             "hDevice"),
  (PVOID,                     "pCommandBuffer"),
  (UINT,                      "CommandBufferSize"),
  (PD3DDDI_ALLOCATIONLIST,    "pAllocationList"),
  (UINT,                      "AllocationListSize"),
  (PD3DDDI_PATCHLOCATIONLIST, "pPatchLocationList"),
  (UINT,                      "PatchLocationListSize"),
);
fExportStructure("DEVMODEA",
  (BYTE[CCHDEVICENAME],       "dmDeviceName"),
  (WORD,                      "dmSpecVersion"),
  (WORD,                      "dmDriverVersion"),
  (WORD,                      "dmSize"),
  (WORD,                      "dmDriverExtra"),
  (DWORD,                     "dmFields"),
  UNION(
    STRUCT(
      (SHORT,                 "dmOrientation"),
      (SHORT,                 "dmPaperSize"),
      (SHORT,                 "dmPaperLength"),
      (SHORT,                 "dmPaperWidth"),
      (SHORT,                 "dmScale"),
      (SHORT,                 "dmCopies"),
      (SHORT,                 "dmDefaultSource"),
      (SHORT,                 "dmPrintQuality"),
    ),
    (POINTL,                  "dmPosition"),
    STRUCT(
      (POINTL,                "dmPosition"),
      (DWORD,                 "dmDisplayOrientation"),
      (DWORD,                 "dmDisplayFixedOutput"),
    ),
  ),
  (SHORT,                     "dmColor"),
  (SHORT,                     "dmDuplex"),
  (SHORT,                     "dmYResolution"),
  (SHORT,                     "dmTTOption"),
  (SHORT,                     "dmCollate"),
  (BYTE[CCHFORMNAME],         "dmFormName"),
  (WORD,                      "dmLogPixels"),
  (DWORD,                     "dmBitsPerPel"),
  (DWORD,                     "dmPelsWidth"),
  (DWORD,                     "dmPelsHeight"),
  UNION(
    (DWORD,                   "dmDisplayFlags"),
    (DWORD,                   "dmNup"),
  ),
  (DWORD,                     "dmDisplayFrequency"),
  (DWORD,                     "dmICMMethod"),
  (DWORD,                     "dmICMIntent"),
  (DWORD,                     "dmMediaType"),
  (DWORD,                     "dmDitherType"),
  (DWORD,                     "dmReserved1"),
  (DWORD,                     "dmReserved2"),
  (DWORD,                     "dmPanningWidth"),
  (DWORD,                     "dmPanningHeight"),
);
fExportStructure("DEVMODEW",
  (WCHAR[CCHDEVICENAME],      "dmDeviceName"),
  (WORD,                      "dmSpecVersion"),
  (WORD,                      "dmDriverVersion"),
  (WORD,                      "dmSize"),
  (WORD,                      "dmDriverExtra"),
  (DWORD,                     "dmFields"),
  UNION(
    STRUCT(
      (SHORT,                 "dmOrientation"),
      (SHORT,                 "dmPaperSize"),
      (SHORT,                 "dmPaperLength"),
      (SHORT,                 "dmPaperWidth"),
      (SHORT,                 "dmScale"),
      (SHORT,                 "dmCopies"),
      (SHORT,                 "dmDefaultSource"),
      (SHORT,                 "dmPrintQuality"),
    ),
    (POINTL,                  "dmPosition"),
    STRUCT(
      (POINTL,                "dmPosition"),
      (DWORD,                 "dmDisplayOrientation"),
      (DWORD,                 "dmDisplayFixedOutput"),
    ),
  ),
  (SHORT,                     "dmColor"),
  (SHORT,                     "dmDuplex"),
  (SHORT,                     "dmYResolution"),
  (SHORT,                     "dmTTOption"),
  (SHORT,                     "dmCollate"),
  (WCHAR[CCHFORMNAME],         "dmFormName"),
  (WORD,                      "dmLogPixels"),
  (DWORD,                     "dmBitsPerPel"),
  (DWORD,                     "dmPelsWidth"),
  (DWORD,                     "dmPelsHeight"),
  UNION(
    (DWORD,                   "dmDisplayFlags"),
    (DWORD,                   "dmNup"),
  ),
  (DWORD,                     "dmDisplayFrequency"),
  (DWORD,                     "dmICMMethod"),
  (DWORD,                     "dmICMIntent"),
  (DWORD,                     "dmMediaType"),
  (DWORD,                     "dmDitherType"),
  (DWORD,                     "dmReserved1"),
  (DWORD,                     "dmReserved2"),
  (DWORD,                     "dmPanningWidth"),
  (DWORD,                     "dmPanningHeight"),
);
