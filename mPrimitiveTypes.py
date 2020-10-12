import ctypes, platform;
from .cCharacterType import cCharacterType;
from .cIntegerType import cIntegerType;
from .cFloatType import cFloatType;
from .fcCreatePointerType import fcCreatePointerType;

uDefaultWordSizeInBits = {"32bit": 32, "64bit": 64}[platform.architecture()[0]];

class cI8(cIntegerType, ctypes.c_byte):
  pass;
class cI16(cIntegerType, ctypes.c_short):
  pass;
class cI32(cIntegerType, ctypes.c_long):
  pass;
class cI64(cIntegerType, ctypes.c_longlong):
  pass;
cI = {32: cI32, 64: cI64}[uDefaultWordSizeInBits];

class cU8(cIntegerType, ctypes.c_ubyte):
  pass;
class cU16(cIntegerType, ctypes.c_ushort):
  pass;
class cU32(cIntegerType, ctypes.c_ulong):
  pass;
class cU64(cIntegerType, ctypes.c_ulonglong):
  pass;
cU = {32: cU32, 64: cU64}[uDefaultWordSizeInBits];

class cF32(cFloatType, ctypes.c_float):
  pass;
class cF64(cFloatType, ctypes.c_double):
  pass;

class cChar(cCharacterType, ctypes.c_char):
  bUnicode = False;
class cWChar(cCharacterType, ctypes.c_wchar):
  bUnicode = True;

cPV = fcCreatePointerType();
cP32V = fcCreatePointerType(uPointerSizeInBits = 32);
cP64V = fcCreatePointerType(uPointerSizeInBits = 64);
cPPV = fcCreatePointerType(cPV);
cPP32V = fcCreatePointerType(cP32V, uPointerSizeInBits = 32);
cPP64V = fcCreatePointerType(cP64V, uPointerSizeInBits = 64);

# We want a list of the names of the primitive types defined below so we can
# automatically generate pointer-to-types for them. We will do this by getting
# a list of the names of all globals now and after they have been defined, so
# we can determine what globals were added.
asGlobalsBeforeTypeDefinitions = globals().keys() + ["asGlobalsBeforeTypeDefinitions"];

dcType_by_sName = {
  #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
  "ASTR": cChar, # Used to create LPASTR etc.
  #BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
  "BOOL": cU32,
  "BOOLEAN": cU8,
  "BYTE": cU8,
  #CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
  "CHAR": cChar,
  "COLESTR": cWChar, # Used to create LPCOLESTR etc.
  "CSTR": cChar, # Used to create LPCSTR etc.
  "CVOID": None, # Used to create LPCVOID etc.
  "CWSTR": cWChar, # Used to create LPCWSTR etc.
  #DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
  "DWORD": cU32,
  "DWORD64": cU64,
  #FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
  "FLOAT": cF32,
  #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
  "HACCEL": cPV,
  "HANDLE": cPV,
  "HBITMAP": cPV,
  "HBRUSH": cPV,
  "HCOLORSPACE": cPV,
  "HDC": cPV,
  "HDESK": cPV,
  "HDWP": cPV,
  "HENHMETAFILE": cPV,
  "HFONT": cPV,
  "HGDIOBJ": cPV,
  "HGLOBAL": cPV,
  "HHOOK": cPV,
  "HICON": cPV,
  "HINSTANCE": cPV,
  "HINTERNET": cPV,
  "HKEY": cPV,
  "HKL": cPV,
  "HLOCAL": cPV,
  "HMENU": cPV,
  "HMETAFILE": cPV,
  "HMODULE": cPV,
  "HMONITOR": cPV,
  "HPALETTE": cPV,
  "HPEN": cPV,
  "HRESULT": cU32, # Officially "LONG" but effectively unsigned
  "HRGN": cPV,
  "HRSRC": cPV,
  "HSTR": cPV,
  "HTASK": cPV,
  "HWINSTA": cPV,
  "HWND": cPV,
  #IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
  "INT": cI32,
  "INT8": cI8,
  "INT16": cI16,
  "INT32": cI32,
  "INT64": cI64,
  #JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
  "JOBOBJECTINFOCLASS": cU, # defined as an enum, so I'm guessing its size depends on the architecture.
  #LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
  "LONG": cI32,
  "LONGLONG": cI64,
  "THREAD_START_ROUTINE": None, # Used to create LPTHREAD_START_ROUTINE etc.
  #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  "NTSTATUS": cI32,
  #OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
  "OLESTR": cWChar, # Used to create LPOLESTR etc.
  #PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
  "PROCESSINFOCLASS": cU, # defined as an enum, so I'm guessing its size depends on the architecture.
  #SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
  "SHORT": cI16,
  "SIZE_T": cU,
  "SIZE_T32": cU32,
  "SIZE_T64": cU64,
  "STR": cChar, # Used to create LPSTR etc.
  #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
  "THREADINFOCLASS": cU, # defined as an enum, so I'm guessing its size depends on the architecture.
  "TOKEN_INFORMATION_CLASS": cU32,
  #UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
  "UCHAR": cU8,
  "UINT": cU32,
  "UINT8": cU8,
  "UINT16": cU16,
  "UINT32": cU32,
  "UINT64": cU64,
  "ULONG": cU32,
  "ULONGLONG": cU64,
  "UNKNOWN": None, # Used to create LPUNKNOWN (Which should be IUknown*)
  "USHORT": cU16,
  #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
  "VOID": None,
  #WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
  "WCHAR": cWChar,
  "WORD": cU16,
  "WSTR": cWChar, # Used to create LPWSTR etc.
  #QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
  "QWORD": cU64,
};

cVoidPointerType = cPV;
cVoidPointerType32 = cP32V;
cVoidPointerType64 = cP64V;

__all__ = [
  "cVoidPointerType",
  "cVoidPointerType32",
  "cVoidPointerType64",
];

def fExportPrimitive(sName, cType):
  globals()[sName] = cType; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.

for (sName, cBaseType) in dcType_by_sName.items():
  if cBaseType is None:
    cType = None;
  else:
    cType = type(sName, (cBaseType,), {});
    cType.sName = sName;
  
  fExportPrimitive(sName, cType);
  if cBaseType == cPV:
    # Pointer types come in 32- and 64-bit variants
    fExportPrimitive(sName + "32", cP32V);
    fExportPrimitive(sName + "64", cP64V);
    # We also export pointer to pointer and their 32- and 64-bit variants
    fExportPrimitive("P%s" % sName, cPPV);
    fExportPrimitive("LP%s" % sName, cPPV);
    fExportPrimitive("P32%s" % sName, cPP32V);    # P32SOMETHING
    fExportPrimitive("P32%s32" % sName, cPP32V);  # P32SOMETHING32
    fExportPrimitive("P64%s" % sName, cPP64V);
    fExportPrimitive("P64%s64" % sName, cPP64V);
  else:
    # Rather than manually declaring various pointer-to-primitive-types we'll
    # automatically declare all common variants. This means we are defining
    # a lot of stuff that does not actually exist in Windows headers but that 
    # should not be a problem.
    cPointerToPrimitiveType = fcCreatePointerType(cType);
    fExportPrimitive("P%s" % sName, cPointerToPrimitiveType);
    fExportPrimitive("LP%s" % sName, cPointerToPrimitiveType);
    fExportPrimitive("%s_PTR" % sName, cPointerToPrimitiveType);
    fExportPrimitive("PP%s" % sName, fcCreatePointerType(cPointerToPrimitiveType));
    # We also explicitly define 32-bit and 64-bit pointer-to-primitive-types
    fExportPrimitive("P32%s" % sName, fcCreatePointerType(cType, uPointerSizeInBits = 32));
    fExportPrimitive("P64%s" % sName, fcCreatePointerType(cType, uPointerSizeInBits = 64));


assert UINT8(1)+UINT8(2) == 3, "FAILED!";
assert 1+UINT8(2) == 3, "FAILED!";
assert UINT8(1)+2 == 3, "FAILED!";
assert UINT8(1)+2 == INT8(3), "FAILED!";

assert UINT8(1)-UINT8(2) == -1, "FAILED!";
assert 1-UINT8(2) == -1, "FAILED!";
assert UINT8(1)-2 == -1, "FAILED!";

assert UINT8(1)-2 == INT8(-1), "FAILED!";
