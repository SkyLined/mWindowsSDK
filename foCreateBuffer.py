import ctypes;
from .mPrimitiveTypes import CHAR, WCHAR;
from .cBufferType import cBufferType;

gddcBufferType_by_uSize_by_cElementType = {};

def foCreateBuffer(sData_or_uSize, uSize = None, bUnicode = False):
  cElementType = WCHAR if bUnicode else CHAR;
  uElementSize = cElementType.fuGetSize();
  if isinstance(sData_or_uSize, (str, unicode)):
    sData = sData_or_uSize;
    if uSize is None:
      uSize = (len(sData) + 1) * uElementSize;
    else:
      assert isinstance(uSize, (int, long)), \
          "Cannot create a buffer with size %s" % repr(uSize);
      assert uSize >= len(sData) * uElementSize, \
          "Cannot create a buffer with size %s and to store %s%s (%d bytes)" % \
          (repr(uSize), "unicode " if bUnicode else "", repr(sData), len(sData) * uElementSize);
  else:
    assert isinstance(sData_or_uSize, (int, long)), \
        "Cannot create a buffer from %s" % repr(sData_or_uSize);
    sData = "";
    uSize = sData_or_uSize;
  
  assert uSize % uElementSize == 0, \
      "Cannot create a buffer with size %s to store elements of size %s" % (repr(uSize), repr(uElementSize));
  # Optionally add padding to data to initialize entire buffer.
  uLength = (uSize / uElementSize);
  sData += "\0" * (uLength - len(sData));
  dcBufferType_by_uSize = gddcBufferType_by_uSize_by_cElementType.setdefault(cElementType, {})
  cCachedBufferType = dcBufferType_by_uSize.get(uSize, None);
  if cCachedBufferType is None:
    sName = "%s[%d]" % (cElementType.sName, uLength);
    cBaseType = cElementType * uLength;
    cCachedBufferType = type(sName, (cBufferType, cBaseType), {
      "sName": sName,
      "_length_": uLength,
      "_type_": cElementType,
    });
    dcBufferType_by_uSize[uSize] = cCachedBufferType;
  oBuffer = cCachedBufferType();
  for uIndex in xrange(len(sData)):
    oBuffer[uIndex].value = sData[uIndex];
  return oBuffer;
    