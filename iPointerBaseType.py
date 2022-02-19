import ctypes, inspect, re;

from .fsDumpInteger import fsDumpInteger;
from .iUnsignedIntegerBaseType import iUnsignedIntegerBaseType;
from .uProcessBits import uProcessBits;

gddcPointerType_by_uPointerSizeInBits_by_c0TargetClass = {};

class iPointerBaseType(iUnsignedIntegerBaseType):
  o0HardLinkedTarget = None;
  
  @classmethod
  def fcCreateSubClassForTargetType(cPointerBaseType, c0TargetClass):
    mDebugOutput_HideInCallStack = True;
    global gddcPointerType_by_uPointerSizeInBits_by_c0TargetClass;
    assert c0TargetClass is None or (inspect.isclass(c0TargetClass) and issubclass(c0TargetClass, iBaseType)), \
        "c0TargetClass is not a type but %s" % repr(c0TargetClass);
    # For a pointer to an array, we create a pointer to the first element in the array. This means we have to adjust
    # the class of the target:
    if c0TargetClass and issubclass(c0TargetClass, iArrayBaseType):
      c0TargetClass = c0TargetClass.cElementClass;
    uPointerSizeInBits = cPointerBaseType.fuGetSize() * 8;
    dcPointerType_by_uPointerSizeInBits = gddcPointerType_by_uPointerSizeInBits_by_c0TargetClass.setdefault(c0TargetClass, {});
    cPointerType = dcPointerType_by_uPointerSizeInBits.get(uPointerSizeInBits);
    
    if cPointerType is None:
      # Pointer name starts with "P" if the size of the pointer is default, "P32"/"P64" if it is not.
      sName = "P%s%s" % (
        "" if uPointerSizeInBits == uProcessBits else str(uPointerSizeInBits),
        c0TargetClass.sName if c0TargetClass is not None else "VOID"
      );
      cPointerType = type(
        sName,
        (cPointerBaseType,),
        {
          "sName": sName,
          # We want the module of the resulting pointer class to be the same as the class it points to.
          "__module__": c0TargetClass.__module__ if c0TargetClass is not None else cPointerBaseType.__module__,
          "uPointerSizeInBits": uPointerSizeInBits,
          "c0TargetClass": c0TargetClass,
        },
      );
      dcPointerType_by_uPointerSizeInBits[uPointerSizeInBits] = cPointerType;
    def fsClassToString(cClass):
      return "%s:%s" % (cClass.__module__, cClass.__name__) if cClass is not None else "VOID";
#    print("Pointer %s->%s == %s" % (fsClassToString(cPointerBaseType), fsClassToString(c0TargetClass), fsClassToString(cPointerType)));
      
    return cPointerType;
  
  @classmethod
  def foCreateForTarget(cPointerBaseClass, oTarget):
    mDebugOutput_HideInCallStack = True;
    assert isinstance(oTarget, iBaseType), \
        "oTarget is not a valid type but %s" % repr(oTarget);
    cPointerSubClass = cPointerBaseClass.fcCreateSubClassForTargetType(oTarget.__class__);
    return cPointerSubClass(oTarget);
  
  def __init__(oSelf, oTarget_sxData_or_u0Address = None, bCast = False):
    mDebugOutput_HideInCallStack = True;
    # oTarget_sxData_or_u0Address can be:
    # 1) None, which creates a NULL pointer
    # 2) 'int', representing an address, which creates a pointer to that address.
    # 3) 'str' or 'bytes', which creates a array of chars and initializes it with
    #    the str or bytes (zero terminated) and then creates a pointer to that
    #    array of chars. The type of char is based on the pointer type and the
    #    array of chars is stored in the `o0HardLinkedTarget property to avoid
    #    it being freed while the pointer exists.
    # 4) Any instance of a class derived from `iBaseType`, which creates a
    #    pointer to the address at which this instance is stored in memory. The
    #    instance is also stored in the `o0HardLinkedTarget` property to avoid
    #    it being freed while the pointer exists.
    if oTarget_sxData_or_u0Address is None or isinstance(oTarget_sxData_or_u0Address, int):
      uAddress = oTarget_sxData_or_u0Address or 0;
    else:
      if isinstance(oTarget_sxData_or_u0Address, (str, bytes)):
        sxData = oTarget_sxData_or_u0Address;
        # Create a copy of the (byte) string as a buffer (an array of bytes/characters), including a 0 terminator. Then
        # use that buffer as if it was provided as the target: save it in the `o0HardLinkedTarget` property and use its
        # address for the pointer.
        cCharacterType = oSelf.__class__.c0TargetClass;
        assert issubclass(cCharacterType, iCharacterBaseType), \
            "Cannot create a %s from %s, as it does not a pointer to a character type." % \
            (oSelf.__class__.sName, repr(sxData));
        oSelf.o0HardLinkedTarget = cCharacterType.foCreateString(sxData);
      else:
        assert isinstance(oTarget_sxData_or_u0Address, iBaseType), \
            "Cannot create a pointer from %s." % (repr(oTarget_sxData_or_u0Address),)
        oSelf.o0HardLinkedTarget = oTarget_sxData_or_u0Address;
      # Do some sanity checks, only we are explicitly casting.
      if not bCast: # If we are not casting, we will do type checks
        c0PointerTargetType = oSelf.__class__.c0TargetClass;
        if isinstance(oSelf.o0HardLinkedTarget, iArrayBaseType):
          cArrayClass = oSelf.o0HardLinkedTarget.__class__;
          cArrayElementClass = cArrayClass.cElementClass;
          if issubclass(cArrayElementClass, iCharacterBaseType):
            # For pointers to characters, we do more relaxed type checking: as long as the pointer points to the same
            # size character, we don't care about the exact type:
            assert (
              issubclass(c0PointerTargetType, iCharacterBaseType) \
              and c0PointerTargetType.fuGetSize() == cArrayElementClass.fuGetSize()
            ), \
                "Cannot creata a %s from %s without bCast = True: the pointer target type (%s) does not match the array element type (%s)" % \
                (oSelf.__class__.sName, repr(oSelf.o0HardLinkedTarget), c0PointerTargetType.sName if c0PointerTargetType else "VOID", cArrayElementClass.sName);
          else:
            assert c0PointerTargetType is cArrayElementClass, \
                "Cannot creata a %s from %s without bCast = True: the pointer target type (%s) does not match the array element type (%s)" % \
                (oSelf.__class__.sName, repr(oSelf.o0HardLinkedTarget), c0PointerTargetType.sName if c0PointerTargetType else "VOID", cArrayElementClass.sName);
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
    uTargetAddress = oSelf.fuGetTargetAddress();
    return (
      oSelf.__class__.c0TargetClass.from_address(uTargetAddress) \
          if uTargetAddress != 0 and oSelf.__class__.c0TargetClass is not None else \
      None
    );
  
  def fuGetTargetAddress(oSelf):
    return oSelf.fuGetValue();
  
  def fs0GetNullTerminatedString(oSelf, u0StartIndex = None, u0MaxSize = None):
    # Look for a NULL terminated Unicode string.
    assert oSelf.__class__.c0TargetClass is not None and issubclass(oSelf.__class__.c0TargetClass, iCharacterBaseType), \
        "Cannot get '\\0' terminated string value of %s: it is not an pointer to characters" % \
        (repr(oSelf),);
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sb0Value = oSelf.fsb0GetNullTerminatedString(u0StartIndex, u0MaxSize);
    if sb0Value is None:
      return None; # There is no NULL terminator!
    s0Encoding = oSelf.__class__.c0TargetClass.s0UnicodeEncoding;
    if s0Encoding is None:
      return "".join(chr(uByte) for uByte in sb0Value);
    else:
      return sb0Value.decode(s0Encoding, "strict");
  
  def fsb0GetNullTerminatedString(oSelf, u0StartIndex = None, u0MaxSize = None):
    # Look for a NULL terminated string.
    assert issubclass(oSelf.__class__.c0TargetClass, iCharacterBaseType), \
        "Cannot get '\\0' terminated string value of %s: it is not an array of characters, but of %s" % \
        (oSelf.__class__.sName, oSelf.__class__.c0TargetClass.sName);
    uCharSize = oSelf.__class__.c0TargetClass.fuGetSize();
    uStartIndex = 0 if u0StartIndex is None else u0StartIndex;
    # Read at most until the end of the buffer but stop if we encounter a '\0' before then.
    sbValue = b"";
    uAddress = oSelf.fuGetTargetAddress();
    while u0MaxSize is None or len(sbValue) + uCharSize <= u0MaxSize:
      oChar = oSelf.__class__.c0TargetClass.from_address(uAddress);
      sbCharValue = oChar.fsbGetValue();
      if all(uByte == 0 for uByte in sbCharValue):
        return sbValue;
      sbValue += sbCharValue;
      uAddress += uCharSize;
    return None; # No NULL terminator found.
  
  def foCastTo(oSelf, cNewType):
    mDebugOutput_HideInCallStack = True;
    # Cast the pointer and copy oTarget to make the new pointer strong if needed and prevent use-after-free:
    oNew = super(iPointerBaseType, oSelf).foCastTo(cNewType);
    oNew.o0HardLinkedTarget = oSelf.o0HardLinkedTarget;
    return oNew;
  
  def fsDumpValue(oSelf):
    uTargetAddress = oSelf.fuGetTargetAddress();
    return "NULL" if uTargetAddress == 0 else fsDumpInteger(uTargetAddress, bHexOnly = True);
  
  def __repr__(oSelf):
    return "<pointer %s (%d-bit @ %s) =%s=> %s%s @ %s>" % (
                     #   #        #    #    #    #
                     oSelf.__class__.sName,
                         oSelf.__class__.fuGetSize() * 8,
                                  fsDumpInteger(oSelf.fuGetAddress(), bHexOnly = True),
                                       "weak" if oSelf.o0HardLinkedTarget is None else "strong",
                                            oSelf.__class__.c0TargetClass.sName if oSelf.__class__.c0TargetClass else "VOID",
                                              "(%s)" % repr(oSelf.o0HardLinkedTarget) if oSelf.o0HardLinkedTarget is not None else "",
                                                   oSelf.fsDumpValue(),
    );

from .iBaseType import iBaseType;
from .iArrayBaseType import iArrayBaseType;
from .iCharacterBaseType import iCharacterBaseType;
