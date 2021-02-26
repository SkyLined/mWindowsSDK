import ctypes;
from .mCharacterBaseTypes import iCharacterBaseTypeA, iCharacterBaseTypeW;
from .mIntegerBaseTypes import \
    iIntegerBaseTypeB, iIntegerBaseTypeI, iIntegerBaseTypeU, \
    iIntegerBaseTypeB8, iIntegerBaseTypeB16, iIntegerBaseTypeB32, iIntegerBaseTypeB64, iIntegerBaseTypeBDefault, \
    iIntegerBaseTypeI8, iIntegerBaseTypeI16, iIntegerBaseTypeI32, iIntegerBaseTypeI64, iIntegerBaseTypeIDefault, \
    iIntegerBaseTypeU8, iIntegerBaseTypeU16, iIntegerBaseTypeU32, iIntegerBaseTypeU64, iIntegerBaseTypeUDefault;
from .mFloatingPointBaseTypes import iFloatingPointBaseType32, iFloatingPointBaseType64;
from .mPointerBaseTypes import \
    iPointerBaseType, iPointerBaseType32, iPointerBaseType64, iPointerBaseTypeDefault, \
    iVoidPointerType32, iVoidPointerType64, iVoidPointerTypeDefault, \
    iVoidPointerPointerType32, iVoidPointerPointerType64, iVoidPointerPointerTypeDefault;
from .uProcessBits import uProcessBits;

di0BaseType_by_sName = {
  #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
  "ASTR":     iCharacterBaseTypeA, # Used to create LPASTR etc.
  #BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
  "BOOL":     iIntegerBaseTypeB32,
  "BOOLEAN":  iIntegerBaseTypeB8,
  "BYTE":     iIntegerBaseTypeU8,
  #CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
  "CHAR":     iCharacterBaseTypeA,
  "COLESTR":  iCharacterBaseTypeW, # Used to create LPCOLESTR etc.
  "CSTR":     iCharacterBaseTypeA, # Used to create LPCSTR etc.
  "CVOID":    None, # Used to create LPCVOID etc.
  "CWSTR":    iCharacterBaseTypeW, # Used to create LPCWSTR etc.
  #DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
  "DWORD":    iIntegerBaseTypeU32,
  "DWORD_PTR": iIntegerBaseTypeIDefault,
  "DWORD64":  iIntegerBaseTypeU64,
  #FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
  "FLOAT":    iFloatingPointBaseType32,
  #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
  "HACCEL":   iVoidPointerTypeDefault,
  "HANDLE":   iVoidPointerTypeDefault,
  "HBITMAP":  iVoidPointerTypeDefault,
  "HBRUSH":   iVoidPointerTypeDefault,
  "HCOLORSPACE": iVoidPointerTypeDefault,
  "HDESK":    iVoidPointerTypeDefault,
  "HDWP":     iVoidPointerTypeDefault,
  "HENHMETAFILE": iVoidPointerTypeDefault,
  "HFONT":    iVoidPointerTypeDefault,
  "HGDIOBJ":  iVoidPointerTypeDefault,
  "HGLOBAL":  iVoidPointerTypeDefault,
  "HHOOK":    iVoidPointerTypeDefault,
  "HICON":    iVoidPointerTypeDefault,
  "HINSTANCE": iVoidPointerTypeDefault,
  "HINTERNET": iVoidPointerTypeDefault,
  "HKEY":     iVoidPointerTypeDefault,
  "HKL":      iVoidPointerTypeDefault,
  "HLOCAL":   iVoidPointerTypeDefault,
  "HMENU":    iVoidPointerTypeDefault,
  "HMETAFILE": iVoidPointerTypeDefault,
  "HMODULE":  iVoidPointerTypeDefault,
  "HMONITOR": iVoidPointerTypeDefault,
  "HPALETTE": iVoidPointerTypeDefault,
  "HPEN":     iVoidPointerTypeDefault,
  "HRESULT":  iIntegerBaseTypeU32, # Officially "LONG" but effectively unsigned
  "HRGN":     iVoidPointerTypeDefault,
  "HRSRC":    iVoidPointerTypeDefault,
  "HSTR":     iVoidPointerTypeDefault,
  "HTASK":    iVoidPointerTypeDefault,
  "HWINSTA":  iVoidPointerTypeDefault,
  "HWND":     iVoidPointerTypeDefault,
  #IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
  "INT":      iIntegerBaseTypeI32,
  "INT_PTR":  iIntegerBaseTypeIDefault,
  "INT8":     iIntegerBaseTypeI8,
  "INT16":    iIntegerBaseTypeI16,
  "INT32":    iIntegerBaseTypeI32,
  "INT64":    iIntegerBaseTypeI64,
  #JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
  "JOBOBJECTINFOCLASS": iIntegerBaseTypeUDefault, # defined as an enum, so I'm guessing its size depends on the architecture.
  #LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
  "LONG":     iIntegerBaseTypeI32,
  "LONG_PTR": iIntegerBaseTypeIDefault,
  "LONGLONG": iIntegerBaseTypeI64,
  "THREAD_START_ROUTINE": None, # Used to create LPTHREAD_START_ROUTINE etc.
  #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  "NTSTATUS": iIntegerBaseTypeI32,
  #OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
  "OLESTR":   iCharacterBaseTypeW, # Used to create LPOLESTR etc.
  #PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
  "PROCESSINFOCLASS": iIntegerBaseTypeUDefault, # defined as an enum, so I'm guessing its size depends on the architecture.
  "POINTER_32": iVoidPointerType32,
  "POINTER_64": iVoidPointerType64,
  #SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
  "SHORT":    iIntegerBaseTypeI16,
  "SIZE_T":   iIntegerBaseTypeUDefault,
  "SIZE_T32": iIntegerBaseTypeU32,
  "SIZE_T64": iIntegerBaseTypeU64,
  "STR":      iCharacterBaseTypeA, # Used to create LPSTR etc.
  #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
  "THREADINFOCLASS": iIntegerBaseTypeUDefault, # defined as an enum, so I'm guessing its size depends on the architecture.
  "TOKEN_INFORMATION_CLASS": iIntegerBaseTypeU32,
  #UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
  "UCHAR":    iIntegerBaseTypeU8,
  "UINT":     iIntegerBaseTypeU32,
  "UINT8":    iIntegerBaseTypeU8,
  "UINT16":   iIntegerBaseTypeU16,
  "UINT32":   iIntegerBaseTypeU32,
  "UINT64":   iIntegerBaseTypeU64,
  "ULONG":    iIntegerBaseTypeU32,
  "ULONGLONG": iIntegerBaseTypeU64,
  "UNKNOWN":  None, # Used to create LPUNKNOWN (Which should be IUknown*)
  "USHORT":   iIntegerBaseTypeU16,
  #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
  "VOID":     None, # Used to create PVOID etc.
  #WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
  "WCHAR":    iCharacterBaseTypeW,
  "WORD":     iIntegerBaseTypeU16,
  "WSTR":     iCharacterBaseTypeW, # Used to create LPWSTR etc.
  #QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
  "QWORD":    iIntegerBaseTypeU64,
};

__all__ = [];

def fExportPrimitive(sName, iBaseType):
  cType = type(sName, (iBaseType,), {"sName": sName});
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

def fExportPointers(sName, iTargetBaseType):
  iPointerBaseType = iPointerBaseTypeDefault.fcCreateType(iTargetBaseType);
  fExportPrimitive("P%s" % sName, iPointerBaseType);
  fExportPrimitive("LP%s" % sName, iPointerBaseType);
  # We also explicitly define 32-bit and 64-bit pointer-to-types
  fExportPrimitive("P32%s" % sName, iPointerBaseType32.fcCreateType(iTargetBaseType));
  fExportPrimitive("P64%s" % sName, iPointerBaseType64.fcCreateType(iTargetBaseType));
  # We also define pointer-to-pointer-to-type
  fExportPrimitive("PP%s" % sName, iPointerBaseTypeDefault.fcCreateType(iPointerBaseType));

for (sName, i0BaseType) in di0BaseType_by_sName.items():
  if i0BaseType is not None:
    # For LPVOID and such we do not export "VOID", for the rest we do:
    fExportPrimitive(sName, i0BaseType);
  fExportPointers(sName, i0BaseType);
  # For types based on a pointer, we explicitly export 32- and 64-bit versions.
  if i0BaseType is iVoidPointerTypeDefault:
    fExportPrimitive(sName + "32", iVoidPointerType32);
    fExportPrimitive(sName + "64", iVoidPointerType64);
