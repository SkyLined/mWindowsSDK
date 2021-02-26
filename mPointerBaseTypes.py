import ctypes, inspect;

from .mIntegerBaseTypes import iIntegerBaseType;
from .uProcessBits import uProcessBits;

gddcPointerType_by_uPointerSizeInBits_by_c0TargetType = {};

class iPointerBaseType(iIntegerBaseType):
  o0HardLinkedTarget = None;
  
  @classmethod
  def fcCreateType(iPointerBaseType, c0TargetType = None):
    global gddcPointerType_by_uPointerSizeInBits_by_c0TargetType;
    assert c0TargetType is None or (inspect.isclass(c0TargetType) and issubclass(c0TargetType, iDataBaseType)), \
        "c0TargetType is not a type but %s" % repr(c0TargetType);
    uPointerSizeInBits = iPointerBaseType.fuGetSize() * 8;
    dcPointerType_by_uPointerSizeInBits = gddcPointerType_by_uPointerSizeInBits_by_c0TargetType.setdefault(c0TargetType, {});
    cPointerType = dcPointerType_by_uPointerSizeInBits.get(uPointerSizeInBits);
    
    if cPointerType is None:
      # Pointer name starts with "P" if the size of the pointer is default, "P32"/"P64" if it is not.
      sPointerPrefix = "" if iPointerBaseType == iPointerBaseTypeDefault else str(uPointerSizeInBits);
      cPointerType = type(
        "P%s%s" % (sPointerPrefix, c0TargetType.sName if c0TargetType is not None else "VOID"),
        (iPointerBaseType,),
        {},
      );
      dcPointerType_by_uPointerSizeInBits[uPointerSizeInBits] = cPointerType;
      cPointerType.sName = cPointerType.__name__;
      cPointerType.uPointerSizeInBits = uPointerSizeInBits;
      cPointerType.c0TargetType = c0TargetType;
    
    return cPointerType;
  
  @classmethod
  def foCreate(iPointerBaseType, oTarget):
    assert isinstance(oTarget, iDataBaseType), \
        "oTarget is not a valid type but %s" % repr(oTarget);
    cPointerType = iPointerBaseType.fcCreateType(oTarget.__class__);
    return cPointerType(oTarget);
  
  def __init__(oSelf, oTarget_sString_or_u0Address = None, bCast = False):
    # oTarget_sString_or_u0Address can be:
    # 1) None, which creates a NULL pointer
    # 2) A number, representing an address, which creates a pointer to that address.
    # 3) A string, which creates a array of chars and initializes it with the string (zero terminated) and then creates
    #    a pointer to that array. The type of char is based on the type of the pointer and the array is stored in the
    #    `o0HardLinkedTarget property to avoid it being freed while the pointer exists.
    # 4) Any instance of a class derived from `iDataBaseType`, which creates a pointer to the address at which this
    #    instance is stored in memory. The instance is also stored in the `o0HardLinkedTarget` property to avoid it being
    #    freed while the pointer exists.
    if oTarget_sString_or_u0Address is None or isinstance(oTarget_sString_or_u0Address, (int, long)):
      uAddress = oTarget_sString_or_u0Address or 0;
    else:
      if isinstance(oTarget_sString_or_u0Address, (str, unicode)):
        # Create a copy of the string as a buffer (an array of characters), including a 0 terminator. Then use that
        # buffer as if it was provided as the target: save it in the `o0HardLinkedTarget` property and use its address
        # for the pointer.
        cCharacterType = oSelf.__class__.c0TargetType;
        assert issubclass(cCharacterType, iCharacterBaseType), \
            "Cannot create a %s from %s, as it does not a pointer to a character type." % \
            (oSelf.__class__.sName, repr(oTarget_sString_or_u0Address));
        oSelf.o0HardLinkedTarget = cCharacterType.foCreateBufferFromString(oTarget_sString_or_u0Address);
      else:
        assert isinstance(oTarget_sString_or_u0Address, iDataBaseType), \
            "Cannot create a pointer from %s." % (repr(oTarget_sString_or_u0Address),)
        oSelf.o0HardLinkedTarget = oTarget_sString_or_u0Address;
      # Do some sanity checks, only we are explicitly casting.
      if not bCast: # If we are not casting, we will do type checks
        c0PointerTargetType = oSelf.__class__.c0TargetType;
        if isinstance(oSelf.o0HardLinkedTarget, iArrayBaseType):
          cArrayElementType = oSelf.o0HardLinkedTarget.__class__.cElementType;
          if issubclass(cArrayElementType, iCharacterBaseType):
            # For pointers to characters, we do very lax type checking: as long as they are both Unicode or not, we're good.
            assert c0PointerTargetType.bUnicode == cArrayElementType.bUnicode, \
                "Cannot creata a %s from %s without bCast = True: the pointer target type (%s) does not match the array element type (%s)" % \
                (oSelf.__class__.sName, repr(oSelf.o0HardLinkedTarget), c0PointerTargetType.sName if c0PointerTargetType else "VOID", cArrayElementType.sName);
          else:
            assert c0PointerTargetType is cArrayElementType, \
                "Cannot creata a %s from %s without bCast = True: the pointer target type (%s) does not match the array element type (%s)" % \
                (oSelf.__class__.sName, repr(oSelf.o0HardLinkedTarget), c0PointerTargetType.sName if c0PointerTargetType else "VOID", cArrayElementType.sName);
        else:
          assert c0PointerTargetType is not None and isinstance(oSelf.o0HardLinkedTarget, c0PointerTargetType), \
              "Cannot create a %s from %s without bCast = True: the pointer target type (%s) does not match the target." % \
              (oSelf.__class__.sName, repr(oSelf.o0HardLinkedTarget), c0PointerTargetType.sName if c0PointerTargetType else "VOID");
      # Use the address
      uAddress = oSelf.o0HardLinkedTarget.fuGetAddress();
    super(iPointerBaseType, oSelf).__init__(uAddress);
  
  def fbIsNULLPointer(oSelf):
    return oSelf.fuGetValue() == 0;
  
  def fo0GetTarget(oSelf):
    return (
      oSelf.__class__.c0TargetType.from_address(oSelf.value) \
          if oSelf.value != 0 and oSelf.__class__.c0TargetType is not None else \
      None
    );
  def fc0GetTargetType(oSelf):
    return oSelf.__class__.c0TargetType;
  
  def fsGetValue(oSelf, u0MaxLength = None):
    assert oSelf.__class__.c0TargetType is not None and issubclass(oSelf.__class__.c0TargetType, iCharacterBaseType), \
        "Cannot get a string for %s" % oSelf.__class__.sName;
    sData = oSelf.__class__.c0TargetType.sEmptyString;
    uAddress = oSelf.fuGetValue();
    while u0MaxLength is None or u0MaxLength > 0:
      oChar = oSelf.__class__.c0TargetType.from_address(uAddress);
      if oChar.fuGetValue() == 0:
        break;
      sData += oChar.fsGetValue();
      uAddress += oSelf.__class__.c0TargetType.uCharSize;
      if u0MaxLength is not None:
        u0MaxLength -= 1;
    return sData;
  
  def foCastTo(oSelf, cNewType):
    # Cast the pointer and copy oTarget to make the new pointer strong if needed and prevent use-after-free:
    oNew = super(iPointerBaseType, oSelf).foCastTo(cNewType);
    oNew.o0HardLinkedTarget = oSelf.o0HardLinkedTarget;
    return oNew;
  
  def fsDumpValue(oSelf):
    uTargetAddress = oSelf.fuGetValue();
    return "0x%X" % uTargetAddress if uTargetAddress != 0 else "NULL";
  
  def __repr__(oSelf):
    # Imports are done JIT to prevent import loops.
    uTargetAddress = oSelf.value;
    if oSelf.o0HardLinkedTarget is not None:
      sPointsTo = " =strong=> %s" % repr(oSelf.o0HardLinkedTarget);
    else:
      sPointsTo = " (weak)";
    return "<pointer %s:%d(0x%X) @ 0x%X%s>" % (
      oSelf.__class__.sName,
      oSelf.fuGetSize(),
      uTargetAddress,
      oSelf.fuGetAddress(),
      sPointsTo,
    );

iPointerBaseType32 = type("iPointerBaseType32", (iPointerBaseType, ctypes.c_ulong), {});
iPointerBaseType64 = type("iPointerBaseType64", (iPointerBaseType, ctypes.c_ulonglong), {});
iPointerBaseTypeDefault = {32: iPointerBaseType32, 64: iPointerBaseType64}[uProcessBits];

from .iDataBaseType import iDataBaseType;
from .iArrayBaseType import iArrayBaseType;
from .mCharacterBaseTypes import iCharacterBaseType;

iVoidPointerType32        = iPointerBaseType32.fcCreateType();
iVoidPointerType64        = iPointerBaseType64.fcCreateType();
iVoidPointerTypeDefault   = iPointerBaseTypeDefault.fcCreateType();
iVoidPointerPointerType32 = iPointerBaseType32.fcCreateType(iVoidPointerType32);
iVoidPointerPointerType64 = iPointerBaseType64.fcCreateType(iVoidPointerType64);
iVoidPointerPointerTypeDefault = iPointerBaseTypeDefault.fcCreateType(iVoidPointerTypeDefault);

