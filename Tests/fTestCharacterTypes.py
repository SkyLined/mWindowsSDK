from mWindowsSDK import cCharacterW;

def fTestCharacterTypes(oConsole):
  def fCheckPointer(oBuffer, sExpectedBufferChars):
    sString = oBuffer.fsGetValue();
    assert sExpectedBufferChars.startswith(sString + "\0") or sExpectedBufferChars == sString, \
        "Expected string %s, got %s" % (repr(sExpectedBufferChars[:len(sString) + 1]), repr(sString + "\0"));
  def fCheckArray(oBuffer, sExpectedBufferChars):
    fCheckPointer(oBuffer, sExpectedBufferChars);
    sBufferChars = "".join(oBuffer.faxGetValues());
    assert sExpectedBufferChars == sBufferChars, \
        "Expected %s, got %s" % (repr(sExpectedBufferChars), repr(sBufferChars));
  
  WCHARx8 = cCharacterW[8];
  oBuffer = WCHARx8("....");
  oBuffer[1].fSetValue(u"X");
  oBuffer[5].fSetValue(u"\u1234");
  fCheckArray(oBuffer, u".X..\0\u1234\0\0");
  
  oBuffer.fClear();
  fCheckArray(oBuffer, u"\0" * 8);

  try:
    oOOB = oBuffer[8];
  except IndexError:
    pass;
  else:
    raise AssertionError("oOOB = %s" % repr(oOOB));
  
  cBufferTypeW = cCharacterW.fcCreatePointer();
  oBuffer = cBufferTypeW("Test");
  fCheckPointer(oBuffer, u"Test");
