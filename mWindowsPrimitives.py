import ctypes;
from .mCharacterClasses import \
  cCharacterA, cCharacterW;
from .mBooleanClasses import \
    cBoolean8, cBoolean16, cBoolean32, cBoolean64, cBoolean;
from .mSignedIntegerClasses import \
    cSignedInteger8, cSignedInteger16, cSignedInteger32, cSignedInteger64, cSignedInteger;
from .mUnsignedIntegerClasses import \
    cUnsignedInteger8, cUnsignedInteger16, cUnsignedInteger32, cUnsignedInteger64, cUnsignedInteger;
from .mFloatingPointClasses import \
    cFloatingPoint32, cFloatingPoint64;
from .mPointerTypes import \
    iPointerType32, iPointerType64, iPointerType;
from .mPointerClasses import \
    cVoidPointer32, cVoidPointer64, cVoidPointer;
from .uProcessBits import uProcessBits;

dx0BaseType_by_sName = {
  #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
  "ASTR":     cCharacterA, # Used to create LPASTR etc.
  #BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
  "BOOL":     cBoolean32,
  "BOOLEAN":  cBoolean8,
  "BYTE":     cUnsignedInteger8,
  #CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
  "CHAR":     cCharacterA,
  "CSTR":     cCharacterA, # Used to create LPCSTR etc.
  "CVOID":    None, # Used to create LPCVOID etc.
  "CWSTR":    cCharacterW, # Used to create LPCWSTR etc.
  #DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
  "DWORD":    cUnsignedInteger32,
  "DWORD_PTR": cSignedInteger,
  "DWORD64":  cUnsignedInteger64,
  #FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
  "FLOAT":    cFloatingPoint32,
  #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
  "HACCEL":   cVoidPointer,
  "HANDLE":   cVoidPointer,
  "HBITMAP":  cVoidPointer,
  "HBRUSH":   cVoidPointer,
  "HCOLORSPACE": cVoidPointer,
  "HDESK":    cVoidPointer,
  "HDWP":     cVoidPointer,
  "HENHMETAFILE": cVoidPointer,
  "HFONT":    cVoidPointer,
  "HGDIOBJ":  cVoidPointer,
  "HGLOBAL":  cVoidPointer,
  "HHOOK":    cVoidPointer,
  "HICON":    cVoidPointer,
  "HINSTANCE": cVoidPointer,
  "HKEY":     cVoidPointer,
  "HKL":      cVoidPointer,
  "HLOCAL":   cVoidPointer,
  "HMENU":    cVoidPointer,
  "HMETAFILE": cVoidPointer,
  "HMODULE":  "HANDLE", # Sub-type
  "HMONITOR": cVoidPointer,
  "HPALETTE": cVoidPointer,
  "HPEN":     cVoidPointer,
  "HRESULT":  cUnsignedInteger32, # Officially "LONG" but effectively unsigned
  "HRGN":     cVoidPointer,
  "HRSRC":    cVoidPointer,
  "HSTR":     cVoidPointer,
  "HTASK":    cVoidPointer,
  "HWINSTA":  cVoidPointer,
  "HWND":     "HANDLE", # Sub-type
  #IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
  "INT":      cSignedInteger32,
  "INT_PTR":  cSignedInteger,
  "INT8":     cSignedInteger8,
  "INT16":    cSignedInteger16,
  "INT32":    cSignedInteger32,
  "INT64":    cSignedInteger64,
  #JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
  "JOBOBJECTINFOCLASS": cUnsignedInteger, # defined as an enum, so I'm guessing its size depends on the architecture.
  #LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
  "LONG":     cSignedInteger32,
  "LONG_PTR": cSignedInteger,
  "LONGLONG": cSignedInteger64,
  "THREAD_START_ROUTINE": None, # Used to create LPTHREAD_START_ROUTINE etc.
  #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  "NTSTATUS": cSignedInteger32,
  #OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
  #PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
  "PROCESSINFOCLASS": cUnsignedInteger, # defined as an enum, so I'm guessing its size depends on the architecture.
  "POINTER_32": cVoidPointer32,
  "POINTER_64": cVoidPointer64,
  #SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
  "SHORT":    cSignedInteger16,
  "SIZE_T":   cUnsignedInteger,
  "SIZE_T32": cUnsignedInteger32,
  "SIZE_T64": cUnsignedInteger64,
  "STR":      cCharacterA, # Used to create LPSTR etc.
  #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
  "THREADINFOCLASS": cUnsignedInteger, # defined as an enum, so I'm guessing its size depends on the architecture.
  "TOKEN_INFORMATION_CLASS": cUnsignedInteger32,
  #UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
  "UCHAR":    cUnsignedInteger8,
  "UINT":     cUnsignedInteger32,
  "UINT8":    cUnsignedInteger8,
  "UINT16":   cUnsignedInteger16,
  "UINT32":   cUnsignedInteger32,
  "UINT64":   cUnsignedInteger64,
  "ULONG":    cUnsignedInteger32,
  "ULONGLONG": cUnsignedInteger64,
  "USHORT":   cUnsignedInteger16,
  #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
  "VOID":     None, # Used to create PVOID etc.
  #WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
  "WCHAR":    cCharacterW,
  "WORD":     cUnsignedInteger16,
  "WSTR":     cCharacterW, # Used to create LPWSTR etc.
  #QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
  "QWORD":    cUnsignedInteger64,
};

__all__ = [];

def fExport(sName, xValue):
  globals()[sName] = xValue; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

def fExportPointers(sName, c0BaseType, cPointerType, cTargetPointer32, cTargetPointer64):
  fExport("P%s" % sName,   cPointerType);
  fExport("LP%s" % sName,  cPointerType);
  fExport("PP%s" % sName,  cPointerType.fcCreatePointer());
  # We also explicitly define 32-bit and 64-bit pointer-to-types
  fExport("P32%s" % sName, cTargetPointer32);
  fExport("P64%s" % sName, cTargetPointer64);
  # For types based on a pointer, we explicitly export 32- and 64-bit versions.
  if c0BaseType is cVoidPointer:
    fExport(sName + "32", type(sName + "32", (cVoidPointer32,), {"sName": sName + "32"}));
    fExport(sName + "64", type(sName + "32", (cVoidPointer64,), {"sName": sName + "32"}));

# Some types are based on other types:
dsBaseTypeName_by_sName = {};
for (sName, x0BaseType) in dx0BaseType_by_sName.items():
  if isinstance(x0BaseType, str):
    dsBaseTypeName_by_sName[sName] = x0BaseType;
    continue;
  c0BaseType = x0BaseType;
  if x0BaseType is None:
    # The type "VOID" does not exist, but void pointers do (e.g. "PVOID")
    cPointerType = cVoidPointer;
    cTargetPointer32 = cVoidPointer32;
    cTargetPointer64 = cVoidPointer64;
  else:
    cType = type(sName, (c0BaseType,), {"sName": sName});
    fExport(sName, cType);
    cPointerType = cType.fcCreatePointer();
    cTargetPointer32 = cType.fcCreatePointer32();
    cTargetPointer64 = cType.fcCreatePointer64();
  fExportPointers(sName, c0BaseType, cPointerType, cTargetPointer32, cTargetPointer64);

while dsBaseTypeName_by_sName:
  dsUnprocessedBaseTypeName_by_sName = {};
  for (sName, sBaseName) in dsBaseTypeName_by_sName.items():
    if sBaseName not in globals():
      dsUnprocessedBaseTypeName_by_sName[sName] = sBaseName;
      continue;
    c0BaseType = globals()[sBaseName];
    cType = type(sName, (c0BaseType,), {"sName": sName});
    fExport(sName, cType);
    fExportPointers(sName, c0BaseType, cPointerType, cTargetPointer32, cTargetPointer64);
  assert len(dsUnprocessedBaseTypeName_by_sName) < len(dsBaseTypeName_by_sName), \
      "cyclic dependencies in: %s" % ", ".join(
        "%s=>%s" % (sName, sBaseName)
        for (sName, sBaseName) in dsUnprocessedBaseTypeName_by_sName.items()
      );
  dsBaseTypeName_by_sName = dsUnprocessedBaseTypeName_by_sName;