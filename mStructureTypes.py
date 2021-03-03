from .iStructureBaseType import iStructureBaseType;
from .uProcessBits import uProcessBits;

iStructureType8  = type("iStructureBaseType8",  (iStructureBaseType,), {"_pack_": 1, "uAlignmentInBits": 8});
iStructureType16 = type("iStructureBaseType16", (iStructureBaseType,), {"_pack_": 2, "uAlignmentInBits": 16});
iStructureType32 = type("iStructureBaseType32", (iStructureBaseType,), {"_pack_": 4, "uAlignmentInBits": 32});
iStructureType64 = type("iStructureBaseType64", (iStructureBaseType,), {"_pack_": 8, "uAlignmentInBits": 64});
iStructureType   = {32: iStructureType32, 64: iStructureType64}[uProcessBits];

