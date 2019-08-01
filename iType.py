import ctypes;

class iType(object):
  @classmethod
  def fuGetSize(cSelf):
    return ctypes.sizeof(cSelf);
  
  @classmethod
  def foFromBytesString(cSelf, sData, uOffset = 0):
    return cSelf.from_buffer_copy(sData[uOffset : uOffset + cSelf.fuGetSize()]); # copy data to prevent use-after-free
  
  def fuGetAddress(oSelf):
    return ctypes.addressof(oSelf);
  
  def fsGetByteString(oSelf):
    return ctypes.string_at(oSelf.fuGetAddress(), oSelf.fuGetSize())[:]; # return a copy
  
  def fauGetByteArray(oSelf):
    return [ord(sByte) for sByte in ctypes.string_at(oSelf.fuGetAddress(), oSelf.fuGetSize())];
  
  def foCreatePointer(oSelf, cCastToPointerType = None, uPointerSizeInBits = None):
    from .cBufferType import cBufferType;
    from .cPointerType import cPointerType;
    from .fcCreatePointerType import fcCreatePointerType;
    if cCastToPointerType is not None:
      assert issubclass(cCastToPointerType, cPointerType), \
          "Cannot create a pointer of type %s" % cCastToPointerType.sName;
      assert uPointerSizeInBits is None or uPointerSizeInBits == cCastToPointerType.uPointerSizeInBits, \
          "Canno create a %d bit %s pointer" % (uPointerSizeInBits, cCastToPointerType.sName);
      cCreatedPointerType = cCastToPointerType;
    elif isinstance(oSelf, cBufferType):
      # A pointer to a buffer is a pointer to the first element in the buffer:
      cCreatedPointerType = fcCreatePointerType(oSelf[0].__class__, uPointerSizeInBits = uPointerSizeInBits);
    else:
      cCreatedPointerType = fcCreatePointerType(oSelf.__class__, uPointerSizeInBits = uPointerSizeInBits);
    return cCreatedPointerType(oSelf, bCast = cCastToPointerType is not None);
  
  def foCastTo(oSelf, cNewType):
    # We will make a copy rather than cast the object, as we are a memory safe language. This will prevent the
    # new object from using memory allocated by oSelf, which will be freed when oSelf gets destroyed, as that could
    # lead to use-after-free bugs when using the new object after oSelf was destroyed.
    assert cNewType.fuGetSize() <= oSelf.fuGetSize(), \
        "Cannot cast %d byte %s to %d byte %s" % (oSelf.fuGetSize(), repr(oSelf), cNewType.fuGetSize(), cNewType.sName);
    sData = ctypes.string_at(oSelf.fuGetAddress(), cNewType.fuGetSize());
    return cNewType.from_buffer_copy(sData);
