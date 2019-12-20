import ctypes;
from .iTypeWithNumbericValue import iTypeWithNumbericValue;

class cBufferType(iTypeWithNumbericValue):
  @property
  def value(oSelf):
    return oSelf.fuGetAddress();

  def fsGetString(oSelf, uOffset = None, uIndex = None, uSize = None, uLength = None):
    assert isinstance(oSelf, cBufferType), \
        "Cannot get buffer data for %s" % repr(oSelf);
    uCharSize = oSelf[0].fuGetSize();
    uBufferSize = oSelf.fuGetSize();
    uBufferLength = uBufferSize / uCharSize;
    if uIndex is not None:
      assert uOffset is None, \
          "Cannot provide an offset (%s) and an index (%s)" % (repr(uOffset), repr(uIndex));
      uOffset = uIndex * uCharSize;
      assert uOffset < uBufferSize, \
          "Cannot get data at index %d in a %d char buffer" % (uOffset, uBufferLength);
    elif uOffset is not None:
      assert uOffset < uBufferSize, \
          "Cannot get data at offset %d in a %d byte buffer" % (uOffset, uBufferSize);
      assert uOffset % uCharSize == 0, \
          "Cannot get data at offset %d because it is not %d byte aligned" % (uOffset, uCharSize);
      uIndex = uOffset / uCharSize;
    else:
      uOffset = uIndex = 0;
    
    if uSize is not None:
      assert uLength is None, \
          "Cannot provide a size (%s) and a length (%s)" % (repr(uSize), repr(uLength));
      assert uSize % uCharSize == 0, \
          "Cannot get %d bytes of data from a %d byte aligned buffer" % (uSize, uCharSize);
      assert uOffset + uSize <= uBufferSize, \
          "Cannot get %d bytes of data%s from a %d byte buffer" % (uSize, " at offset %d" % uOffset if uOffset else "", uBufferSize);
      uLength = uSize / uCharSize;
    elif uLength is not None:
      assert uIndex + uLength <= uBufferLength, \
          "Cannot get %d chars of data%s from a %d char buffer" % (uLength, " at index %d" % uIndex if uIndex else "", uBufferLength);
    else:
      uLength = uBufferLength;
    
    uAddress = oSelf.fuGetAddress() + uOffset;
    fsStringAt = ctypes.wstring_at if oSelf[0].fuGetSize() == 2 else ctypes.string_at;
    return fsStringAt(uAddress, uLength);
  
  def __repr__(oSelf):
    return "<%s:%d @ 0x%X>" % (
      oSelf.sName,
      oSelf.fuGetSize(),
      oSelf.fuGetAddress(),
    );
