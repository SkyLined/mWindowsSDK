from .iType import iType;
from .cBufferType import cBufferType;
from .cIntegerType import cIntegerType;
from .cCharacterType import cCharacterType;

class cPointerType(cIntegerType):
  oObjectThatMustNotBeFreed = None;
  def __init__(oSelf, oTarget_or_uAddress = None, bCast = False):
    if isinstance(oTarget_or_uAddress, iType):
      if isinstance(oTarget_or_uAddress, cBufferType):
        if not bCast:
          assert issubclass(oSelf.__class__.cTargetType, cCharacterType), \
              "Cannot create a pointer to %s from %s" % (oSelf.__class__.cTargetType.sName, repr(oTarget_or_uAddress));
          assert oSelf.__class__.cTargetType.fuGetSize() >= oTarget_or_uAddress[0].fuGetSize(), \
              "Cannot create a pointer to %s from %s" % (oSelf.__class__.cTargetType.sName, repr(oTarget_or_uAddress));
        oSelf.oObjectThatMustNotBeFreed = oTarget_or_uAddress;
        uAddress = oTarget_or_uAddress[0].fuGetAddress();
      else:
        if not bCast:
          assert isinstance(oTarget_or_uAddress, oSelf.__class__.cTargetType), \
              "Cannot create a pointer to %s from %s" % (oSelf.__class__.cTargetType.sName, repr(oTarget_or_uAddress));
        oSelf.oObjectThatMustNotBeFreed = oTarget_or_uAddress;
        uAddress = oTarget_or_uAddress.fuGetAddress();
      oSelf.__bStrong = True;
    else:
      assert oTarget_or_uAddress is None or isinstance(oTarget_or_uAddress, (int, long)), \
            "Cannot create a pointer to %s from %s" % (oSelf.__class__.cTargetType.sName, repr(oTarget_or_uAddress));
      uAddress = oTarget_or_uAddress or 0;
    super(cPointerType, oSelf).__init__(uAddress);
  
  def fbIsNULLPointer(oSelf):
    return oSelf.value == 0;
  
  def foGetTarget(oSelf):
    return (
      oSelf.__class__.cTargetType.from_address(oSelf.value) if oSelf.__class__.cTargetType is not None else \
      None
    );
  def fcGetTargetType(oSelf):
    return oSelf.__class__.cTargetType;

  def foCastTo(oSelf, cNewType):
    # Cast the pointer and copy oTarget to make the new pointer strong if needed and prevent use-after-free:
    oNew = super(cPointerType, oSelf).foCastTo(cNewType);
    oNew.oObjectThatMustNotBeFreed = oSelf.oObjectThatMustNotBeFreed;
    return oNew;
  
  def __repr__(oSelf):
    # Imports are done JIT to prevent import loops.
    uTargetAddress = oSelf.value;
    if oSelf.oObjectThatMustNotBeFreed is not None:
      sPointsTo = " =strong=> %s" % repr(oSelf.oObjectThatMustNotBeFreed);
    else:
      sPointsTo = " (weak)";
    return "<pointer %s:%d(0x%X) @ 0x%X%s>" % (
      oSelf.__class__.sName,
      oSelf.fuGetSize(),
      uTargetAddress,
      oSelf.fuGetAddress(),
      sPointsTo,
    );
