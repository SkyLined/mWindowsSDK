import re;

from .mWindowsPrimitives import BYTE;
from .mWindowsStructures import GUID;

rGUID = re.compile((
  r"^\{"
  r"([0-9a-f]{8})" r"\-"
  r"([0-9a-f]{4})" r"\-"
  r"([0-9a-f]{4})" r"\-"
  r"([0-9a-f]{4})" r"\-" r"([0-9a-f]{12})"
  r"\}$"
), re.I);

def foParseGUID(sGUID):
  oGUIDMatch = rGUID.match(sGUID);
  if not oGUIDMatch: return None;
  sData1, sData2, sData3, sData4_1, sData4_2 = oGUIDMatch.groups();
  sData4 = sData4_1 + sData4_2;
  return GUID(
    long(sData1, 16),
    long(sData2, 16),
    long(sData3, 16),
    BYTE[8](*[long(sData4[uIndex:uIndex+2], 16) for uIndex in xrange(0, len(sData4), 2)])
  );
