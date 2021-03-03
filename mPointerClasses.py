from .mPointerTypes import iPointerType, iPointerType32, iPointerType64;
from .uProcessBits import uProcessBits;

cVoidPointer32        = iPointerType32.fcCreateSubClassForTargetType(None);
cVoidPointer64        = iPointerType64.fcCreateSubClassForTargetType(None);
cVoidPointer          = {32: cVoidPointer32, 64: cVoidPointer64}[uProcessBits];

cVoidPointerPointer32 = cVoidPointer.fcCreatePointer32();
cVoidPointerPointer64 = cVoidPointer.fcCreatePointer64();
cVoidPointerPointer   = cVoidPointer.fcCreatePointer();
