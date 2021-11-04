gasColumnTitles = ["Offset", "Size", "Bytes", "Type and Name", "Value"];
gauColumnWidths = [9,4,47,60,16];
def _fasGetDumpHeader():
  return [
    "│".join(
      gasColumnTitles[uColumnIndex].center(gauColumnWidths[uColumnIndex])
      for uColumnIndex in range(len(gasColumnTitles))
    ),
    "┼".join(
      "─" * uWidth
      for uWidth in gauColumnWidths
    ),
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
  sOffset = (
    "%X%-3s" % (
      uOffset,
      ":%d" % (u0BitsOffset & 0xFFFF) if u0BitsOffset is not None else ""
    )
  ).rjust(gauColumnWidths[0]);
  sSize = (
    "%X" % u0Size if u0Size is not None else
    ":%d" % u0BitsSize if u0BitsSize is not None else
    ""
  ).rjust(gauColumnWidths[1]);
  sBytes = (
    " ".join(["%02X" % uByte for uByte in a0uBytes]) if a0uBytes is not None else ""
  ).ljust(gauColumnWidths[2]);
  sPaddedTypeAndName = (
    " %s%-8s %s" % (sPadding, sType, sName)
  ).ljust(gauColumnWidths[3])
  return "│".join([sOffset, sSize, sBytes, sPaddedTypeAndName, sComment]);

def _fasGetDumpFooter():
  return []; # We do not add one.

