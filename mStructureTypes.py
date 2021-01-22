import ctypes, platform;
from .fcCreatePointerType import fcCreatePointerType;
from .fcTypeDefStructure import fcTypeDefStructure;
from .fcTypeDefStructure32 import fcTypeDefStructure32;
from .fcTypeDefStructure64 import fcTypeDefStructure64;
from .fcTypeDefUnion import fcTypeDefUnion;
from .STRUCT import STRUCT;
from .UNION import UNION;
from .mWindowsDefines import *;
from .mPrimitiveTypes import *;

__all__ = [];

# Export the structure and various types of pointers under common names.
def fExportStructureOrUnion(fcTypeDef, sName, *atxFields):
  cType = fcTypeDef(sName, *atxFields);
  for (sName, cType) in {
              sName: cType,
       "LP" + sName: fcCreatePointerType(cType),
        "P" + sName: fcCreatePointerType(cType),
       "PP" + sName: fcCreatePointerType(fcCreatePointerType(cType)),
      "P32" + sName: fcCreatePointerType(cType, uPointerSizeInBits = 32),
      "P64" + sName: fcCreatePointerType(cType, uPointerSizeInBits = 64),
  }.items():
    globals()[sName] = cType; # Make it available in the context of this file
    __all__.append(sName); # Make it available as an export from this module.

def fExportStructure(sName, *atxFields):
  fExportStructureOrUnion(fcTypeDefStructure, sName, *atxFields);
def fExportStructure32(sName, *atxFields):
  fExportStructureOrUnion(fcTypeDefStructure32, sName, *atxFields);
def fExportStructure64(sName, *atxFields):
  fExportStructureOrUnion(fcTypeDefStructure64, sName, *atxFields);
def fDefineUnion(sName, *atxFields):
  fExportStructureOrUnion(fcTypeDefUnion, sName, *atxFields);

def fExportAlias(sName, cType):
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.
def fExportPointer(sName, cTargetType):
  cType = fcCreatePointerType(cTargetType);
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

################################################################################
# Simple structures that contain only primitives and no other structures are   #
# defined first, strcutures that contain other structures must wait until      #
# those structures are defined and will therefore be defined in a second round #
################################################################################

# This is used in enough structures to be defined first:
fExportStructure32("UNICODE_STRING32",
  (USHORT,      "Length"),
  (USHORT,      "MaximumLength"),
  (P32WSTR,     "Buffer"),
);
fExportStructure64("UNICODE_STRING64",
  (USHORT,      "Length"),
  (USHORT,      "MaximumLength"),
  (P64WSTR,     "Buffer"),
);

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
fExportStructure32("CLIENT_ID32",
  (P32VOID,     "UniqueProcess"),
  (P32VOID,     "UniqueThread"),
);
fExportStructure32("CLIENT_ID64",
  (P64VOID,     "UniqueProcess"),
  (P64VOID,     "UniqueThread"),
);
fExportStructure("COORD", 
  (SHORT,       "X"),
  (SHORT,       "Y"),
);
fExportStructure32("CURDIR32",
  (UNICODE_STRING32, "DosPath"),
  (HANDLE32,    "Handle"),
);
fExportStructure64("CURDIR64",
  (UNICODE_STRING64, "DosPath"),
  (HANDLE64,    "Handle"),
);
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
fExportStructure32("EXCEPTION_REGISTRATION_RECORD32",
  (P32VOID,     "Next"), # Should be EXCEPTION_REGISTRATION_RECORD32
  (P32VOID,     "Handler"), # Should be PEXCEPTION_ROUTINE32
);
fExportStructure64("EXCEPTION_REGISTRATION_RECORD64",
  (P64VOID,     "Next"), # Should be EXCEPTION_REGISTRATION_RECORD64
  (P64VOID,     "Handler"), # Should be PEXCEPTION_ROUTINE64
);
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
fExportStructure("FILETIME",
  (DWORD,       "dwLowDateTime"),
  (DWORD,       "dwHighDateTime"),
);
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
fExportStructure("GUID",
  (DWORD,       "Data1"),
  (WORD,        "Data2"),
  (WORD,        "Data3"),
  (BYTE * 8,    "Data4"),
);
fExportPointer("REFGUID", GUID);
fExportAlias("CLSID", GUID);
fExportPointer("REFCLSID", CLSID);
fExportAlias("IID", GUID);
fExportPointer("REFIID", IID);
#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
fExportStructure("IMAGE_DATA_DIRECTORY",
  (DWORD,       "VirtualAddress"),
  (DWORD,       "Size"),
);
fExportStructure("IMAGE_DOS_HEADER",
  (BYTE * 2,    "e_magic_byte"),  # Magic number
  (UINT16,      "e_cblp"),        # Bytes on last page of file
  (UINT16,      "e_cp"),          # Pages in file
  (UINT16,      "e_crlc"),        # Relocations
  (UINT16,      "e_cparhdr"),     # Size of header in paragraphs
  (UINT16,      "e_minalloc"),    # Minimum extra paragraphs needed
  (UINT16,      "e_maxalloc"),    # Maximum extra paragraphs needed
  (UINT16,      "e_ss"),          # Initial (relative) SS value
  (UINT16,      "e_sp"),          # Initial SP value
  (UINT16,      "e_csum"),        # Checksum
  (UINT16,      "e_ip"),          # Initial IP value
  (UINT16,      "e_cs"),          # Initial (relative) CS value
  (UINT16,      "e_lfarlc"),      # File address of relocation table
  (UINT16,      "e_ovno"),        # Overlay number
  (UINT16 * 4,  "e_res1"),        # Reserved words
  (UINT16,      "e_oemid"),       # OEM identifier (for e_oeminfo)
  (UINT16,      "e_oeminfo"),     # OEM information; e_oemid specific
  (UINT16 * 10, "e_res2"),        # Reserved words
  (INT32,       "e_lfanew"),      # File address of new exe header
);
fExportStructure("IMAGE_FILE_HEADER",
  (WORD,        "Machine"),
  (WORD,        "NumberOfSections"),
  (DWORD,       "TimeDateStamp"),
  (DWORD,       "PointerToSymbolTable"),
  (DWORD,       "NumberOfSymbols"),
  (WORD,        "SizeOfOptionalHeader"),
  (WORD,        "Characteristics"),
);
fExportStructure("IMAGE_OPTIONAL_HEADER32",
  (WORD,        "Magic"),
  (BYTE,        "MajorLinkerVersion"),
  (BYTE,        "MinorLinkerVersion"),
  (DWORD,       "SizeOfCode"),
  (DWORD,       "SizeOfInitializedData"),
  (DWORD,       "SizeOfUninitializedData"),
  (DWORD,       "AddressOfEntryPoint"),
  (DWORD,       "BaseOfCode"),
  (DWORD,       "BaseOfData"),
  (DWORD,       "ImageBase"),
  (DWORD,       "SectionAlignment"),
  (DWORD,       "FileAlignment"),
  (WORD,        "MajorOperatingSystemVersion"),
  (WORD,        "MinorOperatingSystemVersion"),
  (WORD,        "MajorImageVersion"),
  (WORD,        "MinorImageVersion"),
  (WORD,        "MajorSubsystemVersion"),
  (WORD,        "MinorSubsystemVersion"),
  (DWORD,       "Win32VersionValue"),
  (DWORD,       "SizeOfImage"),
  (DWORD,       "SizeOfHeaders"),
  (DWORD,       "CheckSum"),
  (WORD,        "Subsystem"),
  (WORD,        "DllCharacteristics"),
  (DWORD,       "SizeOfStackReserve"),
  (DWORD,       "SizeOfStackCommit"),
  (DWORD,       "SizeOfHeapReserve"),
  (DWORD,       "SizeOfHeapCommit"),
  (DWORD,       "LoaderFlags"),
  (DWORD,       "NumberOfRvaAndSizes"),
  (IMAGE_DATA_DIRECTORY, "ExportTable"),
  (IMAGE_DATA_DIRECTORY, "ImportTable"),
  (IMAGE_DATA_DIRECTORY, "ResourceTable"),
  (IMAGE_DATA_DIRECTORY, "ExceptionTable"),
  (IMAGE_DATA_DIRECTORY, "CertificateTable"),
  (IMAGE_DATA_DIRECTORY, "BaseRelocationTable"),
  (IMAGE_DATA_DIRECTORY, "DebugInformation"),
  (IMAGE_DATA_DIRECTORY, "ArchitectureSpecificData"),
  (IMAGE_DATA_DIRECTORY, "GlobalPointerRegister"),
  (IMAGE_DATA_DIRECTORY, "TLSTable"),
  (IMAGE_DATA_DIRECTORY, "LoadConfigurationTable"),
  (IMAGE_DATA_DIRECTORY, "BoundImportTable"),
  (IMAGE_DATA_DIRECTORY, "ImportAddressTable"),
  (IMAGE_DATA_DIRECTORY, "DelayImportDescriptor"),
  (IMAGE_DATA_DIRECTORY, "CLRHeader"),
  (IMAGE_DATA_DIRECTORY, "ReservedDataDirectory"),
);
fExportStructure("IMAGE_OPTIONAL_HEADER64",
  (WORD,        "Magic"),
  (BYTE,        "MajorLinkerVersion"),
  (BYTE,        "MinorLinkerVersion"),
  (DWORD,       "SizeOfCode"),
  (DWORD,       "SizeOfInitializedData"),
  (DWORD,       "SizeOfUninitializedData"),
  (DWORD,       "AddressOfEntryPoint"),
  (DWORD,       "BaseOfCode"),
  (DWORD,       "BaseOfData"),
  (ULONGLONG,   "ImageBase"),
  (DWORD,       "SectionAlignment"),
  (DWORD,       "FileAlignment"),
  (WORD,        "MajorOperatingSystemVersion"),
  (WORD,        "MinorOperatingSystemVersion"),
  (WORD,        "MajorImageVersion"),
  (WORD,        "MinorImageVersion"),
  (WORD,        "MajorSubsystemVersion"),
  (WORD,        "MinorSubsystemVersion"),
  (DWORD,       "Win32VersionValue"),
  (DWORD,       "SizeOfImage"),
  (DWORD,       "SizeOfHeaders"),
  (DWORD,       "CheckSum"),
  (WORD,        "Subsystem"),
  (WORD,        "DllCharacteristics"),
  (ULONGLONG,   "SizeOfStackReserve"),
  (ULONGLONG,   "SizeOfStackCommit"),
  (ULONGLONG,   "SizeOfHeapReserve"),
  (ULONGLONG,   "SizeOfHeapCommit"),
  (DWORD,       "LoaderFlags"),
  (DWORD,       "NumberOfRvaAndSizes"),
  (IMAGE_DATA_DIRECTORY, "DataDirectory"),
);
fExportStructure32("IO_COUNTERS32",
  (ULONGLONG,   "ReadOperationCount"),
  (ULONGLONG,   "WriteOperationCount"),
  (ULONGLONG,   "OtherOperationCount"),
  (ULONGLONG,   "ReadTransferCount"),
  (ULONGLONG,   "WriteTransferCount"),
  (ULONGLONG,   "OtherTransferCount"),
);
fExportStructure64("IO_COUNTERS64",
  (ULONGLONG,   "ReadOperationCount"),
  (ULONGLONG,   "WriteOperationCount"),
  (ULONGLONG,   "OtherOperationCount"),
  (ULONGLONG,   "ReadTransferCount"),
  (ULONGLONG,   "WriteTransferCount"),
  (ULONGLONG,   "OtherTransferCount"),
);
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
fDefineUnion("LARGE_INTEGER",
  STRUCT(
    (DWORD,     "LowPart"),
    (LONG,      "HighPart"),
  ),
  (STRUCT(
    (DWORD,     "LowPart"),
    (LONG,      "HighPart"),
  ),            "u"),
  (LONGLONG,    "QuadPart"),
);
fExportStructure("LIST_ENTRY",
  (PVOID,       "Flink"), # Should be PLIST_ENTRY but circular references are not implemented.
  (PVOID,       "Blink"), # Should be PLIST_ENTRY but circular references are not implemented.
);
fExportStructure32("LIST_ENTRY32",
  (P32VOID,    "Flink"), # Should be PLIST_ENTRY32 but circular references are not implemented.
  (P32VOID,    "Blink"), # Should be PLIST_ENTRY32 but circular references are not implemented.
);
fExportStructure64("LIST_ENTRY64",
  (P64VOID,    "Flink"), # Should be PLIST_ENTRY64 but circular references are not implemented.
  (P64VOID,    "Blink"), # Should be PLIST_ENTRY64 but circular references are not implemented.
);
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
fExportStructure("M128A",
  (ULONGLONG,    "Low"),
  (LONGLONG,     "High"),
);
fExportStructure("MEMORY_BASIC_INFORMATION", 
  (PVOID,       "BaseAddress"),
  (PVOID,       "AllocationBase"),
  (DWORD,       "AllocationProtect"),
  (SIZE_T,      "RegionSize"),
  (DWORD,       "State"),
  (DWORD,       "Protect"),
  (DWORD,       "Type"),
);
fExportStructure("MEMORY_BASIC_INFORMATION32", 
  (DWORD,       "BaseAddress"),
  (DWORD,       "AllocationBase"),
  (DWORD,       "AllocationProtect"),
  (DWORD,       "RegionSize"),
  (DWORD,       "State"),
  (DWORD,       "Protect"),
  (DWORD,       "Type"),
);
fExportStructure("MEMORY_BASIC_INFORMATION64", 
  (ULONGLONG,   "BaseAddress"),
  (ULONGLONG,   "AllocationBase"),
  (DWORD,       "AllocationProtect"),
  (DWORD,       "__alignment1"),
  (ULONGLONG,   "RegionSize"),
  (DWORD,       "State"),
  (DWORD,       "Protect"),
  (DWORD,       "Type"),
  (DWORD,       "__alignment2"),
);

fExportStructure("MODULEENTRY32A",
  (DWORD,       "dwSize"),
  (DWORD,       "th32ModuleID"),
  (DWORD,       "th32ProcessID"),
  (DWORD,       "GlblcntUsage"),
  (DWORD,       "ProccntUsage"),
  (PBYTE,       "modBaseAddr"),
  (DWORD,       "modBaseSize"),
  (HMODULE,     "hModule"),
  (CHAR * (MAX_MODULE_NAME32 + 1), "szModule"),
  (CHAR * MAX_PATH, "szExePath"),
);
fExportStructure("MODULEENTRY32W",
  (DWORD,       "dwSize"),
  (DWORD,       "th32ModuleID"),
  (DWORD,       "th32ProcessID"),
  (DWORD,       "GlblcntUsage"),
  (DWORD,       "ProccntUsage"),
  (PBYTE,       "modBaseAddr"),
  (DWORD,       "modBaseSize"),
  (HMODULE,     "hModule"),
  (WCHAR * (MAX_MODULE_NAME32 + 1), "szModule"),
  (WCHAR * MAX_PATH, "szExePath"),
);
#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
fExportStructure32("NT_TIB32",
  (PEXCEPTION_REGISTRATION_RECORD32, "ExceptionList"),
  (P32VOID,    "StackBase"),
  (P32VOID,    "StackLimit"),
  (P32VOID,    "SubSystemTib"),
  UNION(
    (P32VOID,  "FiberData"),
    (ULONG,    "Version"),
  ),
  (P32VOID,    "ArbitraryUserPointer"),
  (P32VOID,    "Self"), # Should be P32NT_TIB32 but circular references are not implemented
);
fExportStructure64("NT_TIB64",
  (PEXCEPTION_REGISTRATION_RECORD64, "ExceptionList"),
  (P64VOID,    "StackBase"),
  (P64VOID,    "StackLimit"),
  (P64VOID,    "SubSystemTib"),
  UNION(
    (P64VOID,  "FiberData"),
    (ULONG,    "Version"),
  ),
  (P64VOID,    "ArbitraryUserPointer"),
  (P64VOID,    "Self"), # Should be P64NT_TIB64 but circular references are not implemented
);
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
fExportStructure("OVERLAPPED",
  (PULONG,      "Internal"),
  (PULONG,      "InternalHigh"),
  UNION(
    STRUCT(
      (DWORD,   "Offset"),
      (DWORD,   "OffsetHigh"),
    ),
    (PVOID,     "Pointer"),
  ),
  (HANDLE,      "hEvent"),
);
#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
fExportStructure("POINT",
  (LONG,        "x"),
  (LONG,        "y"),
);
fExportStructure32("PEB_LDR_DATA32", 
  (BYTE * 8,    "Reserved1"),
  (P32VOID * 3, "Reserved2"),
  (LIST_ENTRY32, "InMemoryOrderModuleList"),
);
fExportStructure64("PEB_LDR_DATA64", 
  (BYTE * 8,    "Reserved1"),
  (P64VOID * 3, "Reserved2"),
  (LIST_ENTRY64, "InMemoryOrderModuleList"),
);
fExportStructure("PROCESS_INFORMATION",
  (HANDLE,      "hProcess"),
  (HANDLE,      "hThread"),
  (DWORD,       "dwProcessId"),
  (DWORD,       "dwThreadId"),
);
fExportStructure("PROCESS_MEMORY_COUNTERS",
  (DWORD,       "cb"),
  (DWORD,       "PageFaultCount"),
  (SIZE_T,      "PeakWorkingSetSize"),
  (SIZE_T,      "WorkingSetSize"),
  (SIZE_T,      "QuotaPeakPagedPoolUsage"),
  (SIZE_T,      "QuotaPagedPoolUsage"),
  (SIZE_T,      "QuotaPeakNonPagedPoolUsage"),
  (SIZE_T,      "QuotaNonPagedPoolUsage"),
  (SIZE_T,      "PagefileUsage"),
  (SIZE_T,      "PeakPagefileUsage"),
);
fExportStructure("PROCESS_MEMORY_COUNTERS_EX",
  (DWORD,       "cb"),
  (DWORD,       "PageFaultCount"),
  (SIZE_T,      "PeakWorkingSetSize"),
  (SIZE_T,      "WorkingSetSize"),
  (SIZE_T,      "QuotaPeakPagedPoolUsage"),
  (SIZE_T,      "QuotaPagedPoolUsage"),
  (SIZE_T,      "QuotaPeakNonPagedPoolUsage"),
  (SIZE_T,      "QuotaNonPagedPoolUsage"),
  (SIZE_T,      "PagefileUsage"),
  (SIZE_T,      "PeakPagefileUsage"),
  (SIZE_T,      "PrivateUsage"),
);
fExportStructure("PROCESSENTRY32A",
  (DWORD,       "dwSize"),
  (DWORD,       "cntUsage"),
  (DWORD,       "th32ProcessID"),
  (PULONG,      "th32DefaultHeapID"),
  (DWORD,       "th32ModuleID"),
  (DWORD,       "cntThreads"),
  (DWORD,       "th32ParentProcessID"),
  (LONG,        "pcPriClassBase"),
  (DWORD,       "dwFlags"),
  (CHAR * MAX_PATH, "szExeFile"),
);
fExportStructure("PROCESSENTRY32W",
  (DWORD,       "dwSize"),
  (DWORD,       "cntUsage"),
  (DWORD,       "th32ProcessID"),
  (PULONG,      "th32DefaultHeapID"),
  (DWORD,       "th32ModuleID"),
  (DWORD,       "cntThreads"),
  (DWORD,       "th32ParentProcessID"),
  (LONG,        "pcPriClassBase"),
  (DWORD,       "dwFlags"),
  (WCHAR * MAX_PATH, "szExeFile"),
);
#RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
fExportStructure("RECT",
  (LONG,        "left"),
  (LONG,        "top"),
  (LONG,        "right"),
  (LONG,        "bottom"),
);
#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
fExportStructure("SECURITY_ATTRIBUTES",
  (DWORD,       "nLength"),
  (LPVOID,      "lpSecurityDescriptor"),
  (BOOL,        "bInheritHandle"),
);
fExportStructure("SID");
fExportStructure("SIZE",
  (LONG,        "cx"),
  (LONG,        "cy"),
);
fExportStructure("SMALL_RECT",
  (SHORT,       "Left"),
  (SHORT,       "Top"),
  (SHORT,       "Right"),
  (SHORT,       "Bottom"),
);
fExportStructure("STARTUPINFOA",
  (DWORD,       "cb"),
  (LPSTR,       "lpReserved"),
  (LPSTR,       "lpDesktop"),
  (LPSTR,       "lpTitle"),
  (DWORD,       "dwX"),
  (DWORD,       "dwY"),
  (DWORD,       "dwXSize"),
  (DWORD,       "dwYSize"),
  (DWORD,       "dwXCountChars"),
  (DWORD,       "dwYCountChars"),
  (DWORD,       "dwFillAttribute"),
  (DWORD,       "dwFlags"),
  (WORD,        "wShowWindow"),
  (WORD,        "cbReserved2"),
  (LPBYTE,      "lpReserved2"),
  (HANDLE,      "hStdInput"),
  (HANDLE,      "hStdOutput"),
  (HANDLE,      "hStdError"),
);
fExportStructure("STARTUPINFOW",
  (DWORD,       "cb"),
  (LPWSTR,      "lpReserved"),
  (LPWSTR,      "lpDesktop"),
  (LPWSTR,      "lpTitle"),
  (DWORD,       "dwX"),
  (DWORD,       "dwY"),
  (DWORD,       "dwXSize"),
  (DWORD,       "dwYSize"),
  (DWORD,       "dwXCountChars"),
  (DWORD,       "dwYCountChars"),
  (DWORD,       "dwFillAttribute"),
  (DWORD,       "dwFlags"),
  (WORD,        "wShowWindow"),
  (WORD,        "cbReserved2"),
  (LPBYTE,      "lpReserved2"),
  (HANDLE,      "hStdInput"),
  (HANDLE,      "hStdOutput"),
  (HANDLE,      "hStdError"),
);
fExportStructure("STOWED_EXCEPTION_INFORMATION_HEADER",
  (ULONG,       "Size"),
  (ULONG,       "Signature"),
);
fExportStructure32("STOWED_EXCEPTION_INFORMATION_V132",
  (STOWED_EXCEPTION_INFORMATION_HEADER, "Header"),
  (HRESULT,     "ResultCode"),
  (DWORD,       "ExceptionForm_ThreadId"),
  UNION(
    STRUCT(
      (P32VOID, "ExceptionAddress"),
      (ULONG,   "StackTraceWordSize"),
      (ULONG,   "StackTraceWords"),
      (P32VOID, "StackTrace"),
    ),
    STRUCT(
      (P32WSTR, "ErrorText"),
    ),
  ),
);
fExportStructure64("STOWED_EXCEPTION_INFORMATION_V164",
  (STOWED_EXCEPTION_INFORMATION_HEADER, "Header"),
  (HRESULT,     "ResultCode"),
  (DWORD,       "ExceptionForm_ThreadId"),
  UNION(
    STRUCT(
      (P64VOID, "ExceptionAddress"),
      (ULONG,   "StackTraceWordSize"),
      (ULONG,   "StackTraceWords"),
      (P64VOID, "StackTrace"),
    ),
    STRUCT(
      (P64WSTR, "ErrorText"),
    ),
  ),
);
fExportStructure32("STOWED_EXCEPTION_INFORMATION_V232",
  (STOWED_EXCEPTION_INFORMATION_HEADER, "Header"),
  (HRESULT,     "ResultCode"),
  (DWORD,       "ExceptionForm_ThreadId"),
  UNION(
    STRUCT(
      (P32VOID, "ExceptionAddress"),
      (ULONG,   "StackTraceWordSize"),
      (ULONG,   "StackTraceWords"),
      (P32VOID, "StackTrace"),
    ),
    STRUCT(
      (P32WSTR, "ErrorText"),
    ),
  ),
  (ULONG,       "NestedExceptionType"),
  (P32VOID,     "NestedException"),
);
fExportStructure64("STOWED_EXCEPTION_INFORMATION_V264",
  (STOWED_EXCEPTION_INFORMATION_HEADER, "Header"),
  (HRESULT,     "ResultCode"),
  (DWORD,       "ExceptionForm_ThreadId"),
  UNION(
    STRUCT(
      (P64VOID, "ExceptionAddress"),
      (ULONG,   "StackTraceWordSize"),
      (ULONG,   "StackTraceWords"),
      (P64VOID, "StackTrace"),
    ),
    STRUCT(
      (P64WSTR, "ErrorText"),
    ),
  ),
  (ULONG,       "NestedExceptionType"),
  (P64VOID,     "NestedException"),
);
fExportStructure("SYSTEM_INFO",
  UNION(
    (DWORD,     "dwOemId"),
    STRUCT(
      (WORD,    "wProcessorArchitecture"),
      (WORD,    "wReserved"),
    ),
  ),
  (DWORD,       "dwPageSize"),
  (LPVOID,      "lpMinimumApplicationAddress"),
  (LPVOID,      "lpMaximumApplicationAddress"),
  (DWORD_PTR,   "dwActiveProcessorMask"),
  (DWORD,       "dwNumberOfProcessors"),
  (DWORD,       "dwProcessorType"),
  (DWORD,       "dwAllocationGranularity"),
  (WORD,        "wProcessorLevel"),
  (WORD,        "wProcessorRevision"),
);

#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
fExportStructure("THREADENTRY32",
  (DWORD,       "dwSize"),
  (DWORD,       "cntUsage"),
  (DWORD,       "th32ThreadID"),
  (DWORD,       "th32OwnerProcessID"),
  (LONG,        "tpBasePri"),
  (LONG,        "tpDeltaPri"),
  (DWORD,       "dwFlags"),
);
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
fExportStructure("WINHTTP_AUTOPROXY_OPTIONS",
  (DWORD,       "dwFlags"),
  (DWORD,       "dwAutoDetectFlags"),
  (LPCWSTR,     "lpszAutoConfigUrl"),
  (LPVOID,      "lpvReserved"),
  (DWORD,       "dwReserved"),
  (BOOL,        "fAutoLogonIfChallenged"),
);
fExportStructure("WINHTTP_PROXY_INFO",
  (DWORD,       "dwAccessType"),
  (LPWSTR,      "lpszProxy"),
  (LPWSTR,      "lpszProxyBypass"),
);
################################################################################
# Structures that contain or refer to other structures                         #
################################################################################

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
fExportStructure("CONSOLE_SCREEN_BUFFER_INFO", 
  (COORD,       "dwSize"),
  (COORD,       "dwCursorPosition"),
  (WORD,        "wAttributes"),
  (SMALL_RECT,  "srWindow"),
  (COORD,       "dwMaximumWindowSize"),
);
#JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
fExportStructure32("JOBOBJECT_BASIC_LIMIT_INFORMATION32",
  (LARGE_INTEGER, "PerProcessUserTimeLimit"),
  (LARGE_INTEGER, "PerJobUserTimeLimit"),
  (DWORD,       "LimitFlags"),
  (SIZE_T32,    "MinimumWorkingSetSize"),
  (SIZE_T32,    "MaximumWorkingSetSize"),
  (DWORD,       "ActiveProcessLimit"),
  (P32ULONG,    "Affinity"),
  (DWORD,       "PriorityClass"),
  (DWORD,       "SchedulingClass"),
);
fExportStructure64("JOBOBJECT_BASIC_LIMIT_INFORMATION64",
  (LARGE_INTEGER, "PerProcessUserTimeLimit"),
  (LARGE_INTEGER, "PerJobUserTimeLimit"),
  (DWORD,       "LimitFlags"),
  (SIZE_T64,    "MinimumWorkingSetSize"),
  (SIZE_T64,    "MaximumWorkingSetSize"),
  (DWORD,       "ActiveProcessLimit"),
  (P64ULONG,    "Affinity"),
  (DWORD,       "PriorityClass"),
  (DWORD,       "SchedulingClass"),
);
fExportStructure32("JOBOBJECT_EXTENDED_LIMIT_INFORMATION32",
  (JOBOBJECT_BASIC_LIMIT_INFORMATION32, "BasicLimitInformation"),
  (DWORD,       "Padding0"), # Apparently... but this is not documented anywhere.
  (IO_COUNTERS32, "IoInfo"),
  (SIZE_T32,    "ProcessMemoryLimit"),
  (SIZE_T32,    "JobMemoryLimit"),
  (SIZE_T32,    "PeakProcessMemoryUsed"),
  (SIZE_T32,    "PeakJobMemoryUsed"),
);
fExportStructure64("JOBOBJECT_EXTENDED_LIMIT_INFORMATION64",
  (JOBOBJECT_BASIC_LIMIT_INFORMATION64, "BasicLimitInformation"),
  (IO_COUNTERS64, "IoInfo"),
  (SIZE_T64,    "ProcessMemoryLimit"),
  (SIZE_T64,    "JobMemoryLimit"),
  (SIZE_T64,    "PeakProcessMemoryUsed"),
  (SIZE_T64,    "PeakJobMemoryUsed"),
);
#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
fExportStructure("IMAGE_NT_HEADERS32",
  (DWORD,       "Signature"),
  (IMAGE_FILE_HEADER, "FileHeader"),
  (IMAGE_OPTIONAL_HEADER32, "OptionalHeader"),
);
fExportStructure("IMAGE_NT_HEADERS64",
  (DWORD,       "Signature"),
  (IMAGE_FILE_HEADER, "FileHeader"),
  (IMAGE_OPTIONAL_HEADER64, "OptionalHeader"),
);
#RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
fExportStructure32("RTL_USER_PROCESS_PARAMETERS32",
  (UINT32,      "MaximumLength"),
  (UINT32,      "Length"),
  (UINT32,      "Flags"),
  (UINT32,      "DebugFlags"),
  (HANDLE32,    "ConsoleHandle"),
  (UINT32,      "ConsoleFlags"),
  (HANDLE32,    "StandardInput"),
  (HANDLE32,    "StandardOutput"),
  (HANDLE32,    "StandardError"),
  (CURDIR32,    "CurrentDirectory"),
  (UNICODE_STRING32, "DllPath"),
  (UNICODE_STRING32, "ImagePathName"),
  (UNICODE_STRING32, "CommandLine"),
  (P32VOID,    "Environment"),
  # There's more, but I don't need it
);
fExportStructure64("RTL_USER_PROCESS_PARAMETERS64",
  (UINT32,      "MaximumLength"),
  (UINT32,      "Length"),
  (UINT32,      "Flags"),
  (UINT32,      "DebugFlags"),
  (HANDLE64,    "ConsoleHandle"),
  (UINT32,      "ConsoleFlags"),
  (HANDLE64,    "StandardInput"),
  (HANDLE64,    "StandardOutput"),
  (HANDLE64,    "StandardError"),
  (CURDIR64,    "CurrentDirectory"),
  (UNICODE_STRING64, "DllPath"),
  (UNICODE_STRING64, "ImagePathName"),
  (UNICODE_STRING64, "CommandLine"),
);
#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
fExportStructure("SID_AND_ATTRIBUTES",
  (PSID,        "Sid"),
  (DWORD,       "Attributes"),
);
#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
fExportStructure("TOKEN_MANDATORY_LABEL",
  (SID_AND_ATTRIBUTES, "Label"),
);

#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
fExportStructure("WINDOWPLACEMENT",
  (UINT,  "length"),
  (UINT,  "flags"),
  (UINT,  "showCmd"),
  (POINT, "ptMinPosition"),
  (POINT, "ptMaxPosition"),
  (RECT,  "rcNormalPosition"),
  (RECT,  "rcDevice"),
);

################################################################################
# Structures that contain or refer to other structures which in turn refer to  #
# other structures as well                                                     #
################################################################################

#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
fExportStructure32("PEB32",
  (BYTE,        "InheritedAddressSpace"),
  (BYTE,        "ReadImageFileExecOptions"),
  (BYTE,        "BeingDebugged"),
  (BYTE,        "BitField"),
  (P32VOID,     "Mutant"),
  (P32VOID,     "ImageBaseAddress"),
  (P32PEB_LDR_DATA32, "Ldr"),
  (P32RTL_USER_PROCESS_PARAMETERS32, "ProcessParameters"),
  # There's lots more, but since I do not need it, I did not define it.
);
fExportStructure64("PEB64",
  (BYTE,        "InheritedAddressSpace"),
  (BYTE,        "ReadImageFileExecOptions"),
  (BYTE,        "BeingDebugged"),
  (BYTE,        "BitField"),
  (BYTE * 4,    "Padding0"),
  (P64VOID,     "Mutant"),
  (P64VOID,     "ImageBaseAddress"),
  (P64PEB_LDR_DATA64, "Ldr"),
  (P64RTL_USER_PROCESS_PARAMETERS64, "ProcessParameters"),
  # There's lots more, but since I do not need it, I did not define it.
);
fExportStructure32("PROCESS_BASIC_INFORMATION32",
  (P32VOID,     "Reserved1"),
  (P32PEB32,    "PebBaseAddress"),
  (P32VOID * 2, "Reserved2"),
  (P32ULONG,    "UniqueProcessId"),
  (P32VOID,     "Reserved3"),
);
fExportStructure64("PROCESS_BASIC_INFORMATION64",
  (P64VOID,     "Reserved1"),
  (P64PEB64,    "PebBaseAddress"),
  (P64VOID * 2, "Reserved2"),
  (P64ULONG,    "UniqueProcessId"),
  (P64VOID,     "Reserved3"),
);
#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
fExportStructure32("TEB32",
  (NT_TIB32,    "NtTib"),
  (P32VOID,     "EnvironmentPointer"),
  (CLIENT_ID32, "ClientId"),
  # There is more, but I do not need it at this point.
);
fExportStructure64("TEB64",
  (NT_TIB64,    "NtTib"),
  (P64VOID,     "EnvironmentPointer"),
  (CLIENT_ID64, "ClientId"),
  # There is more, but I do not need it at this point.
);
fExportStructure32("THREAD_BASIC_INFORMATION32",
  (NTSTATUS,    "ExitStatus"),
  (P32TEB32,    "TebBaseAddress"),
  (CLIENT_ID32, "ClientId"),
  (DWORD,       "AffinityMask"),
  (DWORD,       "Priority"),
  (DWORD,       "BasePriority"),
);
fExportStructure64("THREAD_BASIC_INFORMATION64",
  (NTSTATUS,    "ExitStatus"),
  (P64TEB64,    "TebBaseAddress"),
  (CLIENT_ID64, "ClientId"),
  (DWORD,       "AffinityMask"),
  (DWORD,       "Priority"),
  (DWORD,       "BasePriority"),
);

# Thread context
fExportStructure32("FLOATING_SAVE_AREA32",
  (DWORD,       "ControlWord"),
  (DWORD,       "StatusWord"),
  (DWORD,       "TagWord"),
  (DWORD,       "ErrorOffset"),
  (DWORD,       "ErrorSelector"),
  (DWORD,       "DataOffset"),
  (DWORD,       "DataSelector"),
  (BYTE * 80,   "RegisterArea"),
  (DWORD,       "Cr0NpxState"),
);
fExportStructure32("CONTEXT32", 
  (DWORD,       "ContextFlags"),
  (DWORD,       "Dr0"),
  (DWORD,       "Dr1"),
  (DWORD,       "Dr2"),
  (DWORD,       "Dr3"),
  (DWORD,       "Dr6"),
  (DWORD,       "Dr7"),
  (FLOATING_SAVE_AREA32, "FloatSave"),
  (DWORD,       "SegGs"),
  (DWORD,       "SegFs"),
  (DWORD,       "SegEs"),
  (DWORD,       "SegDs"),
  (DWORD,       "Edi"),
  (DWORD,       "Esi"),
  (DWORD,       "Ebx"),
  (DWORD,       "Edx"),
  (DWORD,       "Ecx"),
  (DWORD,       "Eax"),
  (DWORD,       "Ebp"),
  (DWORD,       "Eip"),
  (DWORD,       "SegCs"),
  (DWORD,       "Eflags"),
  (DWORD,       "Esp"),
  (DWORD,       "SegSs"),
  (BYTE * 512,  "ExtendedRegisters"),
);

fExportStructure64("XMM_SAVE_AREA32",
  (WORD,        "ControlWord"),
  (WORD,        "StatusWord"),
  (BYTE,        "TagWord"),
  (BYTE,        "Reserved1"),
  (WORD,        "ErrorOpcode"),
  (DWORD,       "ErrorOffset"),
  (WORD,        "ErrorSelector"),
  (WORD,        "Reserved2"),
  (DWORD,       "DataOffset"),
  (WORD,        "DataSelector"),
  (WORD,        "Reserved3"),
  (DWORD,       "MxCsr"),
  (DWORD,       "MxCsr_Mask"),
  (M128A * 8,   "FloatRegisters"),
  (M128A * 16,  "XmmRegisters"),
  (BYTE * 96,   "Reserved4"),
);

fExportStructure64("CONTEXT64", 
  (DWORD64,     "P1Home"),
  (DWORD64,     "P2Home"),
  (DWORD64,     "P3Home"),
  (DWORD64,     "P4Home"),
  (DWORD64,     "P5Home"),
  (DWORD64,     "P6Home"),
  (DWORD,       "ContextFlags"),
  (DWORD,       "MxCsr"),
  (WORD,        "SegCs"),
  (WORD,        "SegDs"),
  (WORD,        "SegEs"),
  (WORD,        "SegFs"),
  (WORD,        "SegGs"),
  (WORD,        "SegSs"),
  (DWORD,       "EFlags"),
  (DWORD64,     "Dr0"),
  (DWORD64,     "Dr1"),
  (DWORD64,     "Dr2"),
  (DWORD64,     "Dr3"),
  (DWORD64,     "Dr6"),
  (DWORD64,     "Dr7"),
  (DWORD64,     "Rax"),
  (DWORD64,     "Rcx"),
  (DWORD64,     "Rdx"),
  (DWORD64,     "Rbx"),
  (DWORD64,     "Rsp"),
  (DWORD64,     "Rbp"),
  (DWORD64,     "Rsi"),
  (DWORD64,     "Rdi"),
  (DWORD64,     "R8"),
  (DWORD64,     "R9"),
  (DWORD64,     "R10"),
  (DWORD64,     "R11"),
  (DWORD64,     "R12"),
  (DWORD64,     "R13"),
  (DWORD64,     "R14"),
  (DWORD64,     "R15"),
  (DWORD64,     "Rip"),
  UNION( 
    (XMM_SAVE_AREA32, "FltSave"),
    STRUCT(
      (M128A * 2,       "Header"),
      UNION(
        (M128A * 8,       "Legacy"),
        (M128A,           "St0"),
        (M128A,           "St1"),
        (M128A,           "St2"),
        (M128A,           "St3"),
        (M128A,           "St4"),
        (M128A,           "St5"),
        (M128A,           "St6"),
        (M128A,           "St7"),
      ),
      (M128A,           "Xmm0"),
      (M128A,           "Xmm1"),
      (M128A,           "Xmm2"),
      (M128A,           "Xmm3"),
      (M128A,           "Xmm4"),
      (M128A,           "Xmm5"),
      (M128A,           "Xmm6"),
      (M128A,           "Xmm7"),
      (M128A,           "Xmm8"),
      (M128A,           "Xmm9"),
      (M128A,           "Xmm10"),
      (M128A,           "Xmm11"),
      (M128A,           "Xmm12"),
      (M128A,           "Xmm13"),
      (M128A,           "Xmm14"),
      (M128A,           "Xmm15"),
    ),
  ),
  (M128A * 26,  "VectorRegister"),
  (DWORD64,     "VectorControl"),
  (DWORD64,     "DebugControl"),
  (DWORD64,     "LastBranchToRip"),
  (DWORD64,     "LastBranchFromRip"),
  (DWORD64,     "LastExceptionToRip"),
  (DWORD64,     "LastExceptionFromRip"),
);
