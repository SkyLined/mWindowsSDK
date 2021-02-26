def _fasGetDumpHeader():
  sOffset = "Offset".center(9);
  sSize = "Size";
  sBytes = "Bytes".ljust(47)
  sPaddedTypeAndName = ("%-8s %s" % ("Type", "Name")).ljust(60);
  sValue = "Value";
  return [
    "|".join(["", sOffset, sSize,   sBytes,   sPaddedTypeAndName, sValue]),
    "+".join(["", "-" * 9, "-" * 4, "-" * 47,  "-" * 60, "-" * 16]),
  ];

def _fsFormatDumpLine(
  uOffset,
  u0BitsOffset = None,
  u0Size = None, 
  u0BitsSize = None,
  a0uBytes = None,
  sPadding = "",
  sType = "",
  sName = "",
  sComment = ""
):
  sOffset = "%6X%-3s" % (
    uOffset,
    ":%d" % (u0BitsOffset & 0xFFFF) if u0BitsOffset is not None else ""
  );
  sSize = "%4s" % (
    "%X" % u0Size if u0Size is not None else
    ":%d" % u0BitsSize if u0BitsSize is not None else
    ""
  );
  sBytes = "%-47s" % (
    " ".join(["%02X" % uByte for uByte in a0uBytes]) if a0uBytes is not None else ""
   );
  sPaddedTypeAndName = "%-60s" % (
    " %s%-8s %s" % (sPadding, sType, sName)
  );
  return "|".join(["", sOffset, sSize, sBytes, sPaddedTypeAndName, sComment]);

def _fasGetDumpFooter():
  return [
    "`" + ("+".join(["-" * 9, "-" * 4, "-" * 47,  "-" * 60, "-" * 16])),
  ];

