from cDLL import cDLL;
from mPrimitiveTypes import *;
from mStructureTypes import *;

goAdvAPI32DLL = None;
def foLoadAdvAPI32DLL():
  global goAdvAPI32DLL;
  if goAdvAPI32DLL is None:
    goAdvAPI32DLL = cDLL(
      "Advapi32.dll", 
      {
        "GetTokenInformation": {
          "xReturnType": BOOL, 
          "txArgumentTypes": (HANDLE, TOKEN_INFORMATION_CLASS, LPVOID, DWORD, PDWORD),
        },
        "GetSidSubAuthorityCount": {
          "xReturnType": PUCHAR, 
          "txArgumentTypes": (PSID),
        },
        "GetSidSubAuthority": {
          "xReturnType": PDWORD, 
          "txArgumentTypes": (PSID, DWORD),
        },
      },
    );
  return goAdvAPI32DLL;