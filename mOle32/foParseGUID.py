import re;

from .mPrimitives import BYTE;
from .mStructures import GUID;

rGUID = re.compile((
  r"^\{"
  r"([0-9a-f]{8})" r"\-"
  r"([0-9a-f]{4})" r"\-"
  r"([0-9a-f]{4})" r"\-"
  r"([0-9a-f]{4})" r"\-" r"([0-9a-f]{12})"
  r"\}$"
), re.I);

def foParseGUID(sGUID, cClass = GUID):
  oGUIDMatch = rGUID.match(sGUID);
  if not oGUIDMatch: return None;
  sData1, sData2, sData3, sData4_1, sData4_2 = oGUIDMatch.groups();
  sData4 = sData4_1 + sData4_2;
  return cClass(
    int(sData1, 16),
    int(sData2, 16),
    int(sData3, 16),
    BYTE[8](*[int(sData4[uIndex:uIndex+2], 16) for uIndex in range(0, len(sData4), 2)])
  );
