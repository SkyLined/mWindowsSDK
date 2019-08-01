import ctypes, platform;
from .cPointerType import cPointerType;

guDefaultPointerSizeInBits = {"32bit": 32, "64bit": 64}[platform.architecture()[0]];
gddcCachedPointerType_by_uPointerSizeInBits_by_cTargetType = {};

def fcCreatePointerType(cTargetType = None, uPointerSizeInBits = None):
  uPointerSizeInBits = uPointerSizeInBits if uPointerSizeInBits is not None else guDefaultPointerSizeInBits;
  
  global gddcCachedPointerType_by_uPointerSizeInBits_by_cTargetType;
  dcCachedPointerType_by_uPointerSizeInBits = gddcCachedPointerType_by_uPointerSizeInBits_by_cTargetType.setdefault(cTargetType, {});
  cCachedPointerType = dcCachedPointerType_by_uPointerSizeInBits.get(uPointerSizeInBits);
  if cCachedPointerType is None:
    sPointerTypeName = "P%d%s" % (uPointerSizeInBits, cTargetType.sName if cTargetType is not None else "VOID");
    cPointerAddressValueType = {32: ctypes.c_ulong, 64: ctypes.c_ulonglong}[uPointerSizeInBits];
    cCachedPointerType = type(sPointerTypeName, (cPointerType, cPointerAddressValueType), {});
    dcCachedPointerType_by_uPointerSizeInBits[uPointerSizeInBits] = cCachedPointerType;
    cCachedPointerType.sName = sPointerTypeName;
    cCachedPointerType.uPointerSizeInBits = uPointerSizeInBits;
    cCachedPointerType.cTargetType = cTargetType;
  return cCachedPointerType;
