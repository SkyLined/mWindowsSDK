import ctypes;

class iBaseType(object):
  @classmethod
  def fuGetSize(cSelf):
    return ctypes.sizeof(cSelf);
    
  @classmethod
  def foFromAddress(cSelf, uAddress):
    return cSelf.from_address(uAddress);
  
  @classmethod
  def foFromBytesString(cSelf, sData, uOffset = 0):
    return cSelf.from_buffer_copy(sData[uOffset : uOffset + cSelf.fuGetSize()]); # copy data to prevent use-after-free
  
  def fuGetAddress(oSelf):
    return ctypes.addressof(oSelf);
  
  def fClear(oSelf):
    uSize = oSelf.fuGetSize();
    aoBYTEs = (ctypes.c_ubyte * uSize).from_address(oSelf.fuGetAddress());
    for uOffset in range(uSize):
      aoBYTEs[uOffset] = 0;
  
  def fsbGetValue(oSelf):
    return bytes(ctypes.string_at(oSelf.fuGetAddress(), oSelf.fuGetSize()));
  
  def fSetBytes(oSelf, sbValue, bZeroPadding = False):
    uSize = oSelf.fuGetSize();
    if bZeroPadding:
      assert len(sbValue) <= uSize, \
          "Cannot set %s (size = %d bytes) using a bytes string of %d bytes: %s" % \
          (oSelf.__class__.__name__, uSize, len(sbValue), repr(sbValue));
    else:
      assert uSize == len(sbValue), \
          "Cannot set %s (size = %d bytes) using a bytes string of %d bytes without zero padding: %s" % \
          (oSelf.__class__.__name__, uSize, len(sbValue), repr(sbValue));
    aoBYTEs = (ctypes.c_ubyte * uSize).from_address(oSelf.fuGetAddress());
    for uOffset in range(len(sbValue)):
      aoBYTEs[uOffset] = sbValue[uOffset];
    if bZeroPadding:
      for uOffset in range(len(sbValue), uSize):
        aoBYTEs[uOffset] = 0;
  
  def fauGetBytes(oSelf):
    return ctypes.string_at(oSelf.fuGetAddress(), oSelf.fuGetSize());
  
  @classmethod
  def fcCreatePointer32(cSelf):
    from .mPointerTypes import iPointerType32;
    return iPointerType32.fcCreateSubClassForTargetType(cSelf);
  def foCreatePointer32(oSelf):
    return oSelf.__class__.fcCreatePointer32()(oSelf);
  
  @classmethod
  def fcCreatePointer64(cSelf):
    from .mPointerTypes import iPointerType64;
    return iPointerType64.fcCreateSubClassForTargetType(cSelf);
  def foCreatePointer64(oSelf):
    return oSelf.__class__.fcCreatePointer64()(oSelf);
  
  @classmethod
  def fcCreatePointer(cSelf):
    from .mPointerTypes import iPointerType;
    return iPointerType.fcCreateSubClassForTargetType(cSelf);
  def foCreatePointer(oSelf):
    return oSelf.__class__.fcCreatePointer()(oSelf);
  
  def foCastTo(oSelf, cNewType):
    # We will make a copy rather than cast the object, as we are a memory safe language. This will prevent the
    # new object from using memory allocated by oSelf, which will be freed when oSelf gets destroyed, as that could
    # lead to use-after-free bugs when using the new object after oSelf was destroyed.
    assert cNewType.fuGetSize() <= oSelf.fuGetSize(), \
        "Cannot cast %d byte %s to %d byte %s" % (oSelf.fuGetSize(), repr(oSelf), cNewType.fuGetSize(), cNewType.sName);
    sData = ctypes.string_at(oSelf.fuGetAddress(), cNewType.fuGetSize());
    return cNewType.from_buffer_copy(sData);
  
  def __repr__(oSelf):
    return "<class type %s>" % (oSelf.__class__.__name__,);