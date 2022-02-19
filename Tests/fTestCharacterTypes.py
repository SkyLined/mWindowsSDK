import json;

from mWindowsSDK import cCharacterA, cCharacterW;

def fTestCharacterTypes(oConsole):
  def fCheckString(osString, sExpectedChars, sbExpectedBytes):
    # Create a pointer to the string:
    opsString = osString.foCreatePointer();
    # Check the expected bytes.
    sbBytes = osString.fsbGetValue();
    assert sbBytes == sbExpectedBytes, \
        "%s: fsbGetValue() expected %s, got %s" % (
          repr(osString),
          repr(sbExpectedBytes)[1:],
          repr(sbBytes)[1:],
        );
    # Check the decoded Unicode string
    sString = osString.fsGetValue();
    assert sString == sExpectedChars, \
        "%s: fsGetValue() expected %s, got %s" % (
          repr(osString),
          json.dumps(sExpectedChars),
          json.dumps(sString),
        );
    # Check for NULL terminated strings if possible:
    if "\0" in sExpectedChars:
      uCharSize = osString[0].fuGetSize();
      # Look for the bytes that represent the '\0' character, and create a
      # sub-string of sbExpectedBytes up to those.
      for uOffset in range(0, len(sbExpectedBytes), uCharSize):
        if all(uByte == 0 for uByte in sbExpectedBytes[uOffset:uOffset + uCharSize]):
          sbNullTerminatedString = sbExpectedBytes[:uOffset];
          break;
      else:
        raise AssertionError(); # NOT REACHED
      # First bytes string that ends at the first bytes that represent a null
      # character.
      sb0String = osString.fsb0GetNullTerminatedString();
      assert sb0String == sbNullTerminatedString, \
          "%s: fsb0GetNullTerminatedString() expected %s, got %s" % (
            repr(osString),
            repr(sbNullTerminatedString),
            repr(sb0String),
          );
      # Next the byte string through the pointer.
      sb0String = opsString.fsb0GetNullTerminatedString();
      assert sb0String == sbNullTerminatedString, \
          "%s: fsb0GetNullTerminatedString() expected %s, got %s" % (
            repr(opsString),
            repr(sbNullTerminatedString),
            repr(sb0String),
          );
      # The Unicode string
      sNullTerminatedString = sExpectedChars.split("\0")[0];
      s0String = osString.fs0GetNullTerminatedString();
      assert s0String == sNullTerminatedString, \
          "%s: fs0GetNullTerminatedString() expected %s, got %s" % (
            repr(osString),
            json.dumps(sNullTerminatedString),
            json.dumps(s0String),
          );
      # Finally, Unicode string through the pointer
      s0String = opsString.fs0GetNullTerminatedString();
      assert s0String == sNullTerminatedString, \
          "%s: fs0GetNullTerminatedString() expected %s, got %s" % (
            repr(opsString),
            repr(sNullTerminatedString),
            repr(s0String),
          );
    # Create a new String from Unicode string and check that it decodes to the same value.
    sCycledString = osString.__class__.cElementClass.foCreateString(sExpectedChars).fsGetValue();
    assert sCycledString == sExpectedChars + "\0", \
        "%s: Attempting to create a %s-string using %s and getting its value resulted in %s" % (
          repr(osString),
          osString.__class__.cElementClass.__name__,
          json.dumps(sExpectedChars + "\0"),
          json.dumps(sCycledString),
        );
  
  WCHAR_x8 = cCharacterW[4];
  osString = WCHAR_x8("A");
  fCheckString(osString, "A\0\0\0",                b"A\0"      b"\0\0"     b"\0\0"     b"\0\0");
  osString[2].fSetValue("B");
  fCheckString(osString, "A\0B\0",                 b"A\0"      b"\0\0"     b"B\0"      b"\0\0");
  osString[3].fSetValue("\u1234");
  fCheckString(osString, "A\0B\u1234",             b"A\0"      b"\0\0"     b"B\0"      b"\x34\x12");
  osString.fSetValue("\U00012345");
  fCheckString(osString, "\U00012345\0\u1234",     b"\x08\xd8" b"\x45\xdf" b"\0\0"     b"\x34\x12");
  
  osString.fClear();
  fCheckString(osString, "\0\0\0\0",               b"\0\0"     b"\0\0"     b"\0\0"     b"\0\0");
  
  try:
    oOOBR = osString[5];
  except IndexError:
    pass;
  else:
    raise AssertionError("oOOBR = %s" % repr(oOOBR));
  
  pcCharacterW = cCharacterW.fcCreatePointer();
  opsString = pcCharacterW("Test");
  s0String = opsString.fs0GetNullTerminatedString();
  assert s0String == "Test", \
      "%s: fs0GetNullTerminatedString() expected \"Test\", got %s" % (
        repr(opsString),
        json.dumps(s0String),
      );
  sb0String = opsString.fsb0GetNullTerminatedString();
  assert sb0String == b"T\0e\0s\0t\0", \
      "%s: fsb0GetNullTerminatedString() expected 'T\\0e\\0s\\0t\\0', got %s" % (
        repr(opsString),
        repr(sbString)[1:],
      );
  
  pcCharacterA = cCharacterA.fcCreatePointer();
  opsbString = pcCharacterA(b"Test");
  sString = opsbString.fs0GetNullTerminatedString();
  assert sString == "Test", \
      "%s: fs0GetNullTerminatedString() expected 'Test', got %s" % (
        repr(opsbString),
        repr(sString)[1:],
      );
  sbString = opsbString.fsb0GetNullTerminatedString();
  assert sbString == b"Test", \
      "%s: fsb0GetNullTerminatedString() expected 'Test', got %s" % (
        repr(opsbString),
        repr(sbString)[1:],
      );
