from .iUnionBaseType import iUnionBaseType;
from .uProcessBits import uProcessBits;

iUnionType8  = type("iUnionBaseType8",  (iUnionBaseType,), {"_pack_": 1, "uAlignmentInBits": 8});
iUnionType16 = type("iUnionBaseType16", (iUnionBaseType,), {"_pack_": 2, "uAlignmentInBits": 16});
iUnionType32 = type("iUnionBaseType32", (iUnionBaseType,), {"_pack_": 4, "uAlignmentInBits": 32});
iUnionType64 = type("iUnionBaseType64", (iUnionBaseType,), {"_pack_": 8, "uAlignmentInBits": 64});
iUnionType   = {32: iUnionType32, 64: iUnionType64}[uProcessBits];
