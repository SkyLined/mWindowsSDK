import re;

def fsDumpInteger(iValue, bHexOnly = False):
  if abs(iValue) < 10:
    return str(iValue);
  sSign = ("-" if iValue < 0 else "");
  sHexadecimal = sSign + "0x" + re.sub(
    # With a '`' between each block of 8 chars for readability.
    r"(.)" "(?=" "(.{8})+$" ")",
    r"\1`",
    "%X" % abs(iValue)
  );
  if bHexOnly:
    return sHexadecimal;
  sDecimal = sSign + re.sub(
    # With a ',' between each block of 3 digits for readability.
    r"(.)" "(?=" "(.{3})+$" ")",
    r"\1,",
    str(abs(iValue))
  )
  return "%s / %s" % (sDecimal, sHexadecimal);