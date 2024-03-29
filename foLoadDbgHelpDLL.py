from .cDLL import cDLL;
from .mWindowsPrimitiveTypes import \
  DWORD, PCSTR, PCWSTR, PSTR, PWSTR;

goDbgHelpDLL = None;
def foLoadDbgHelpDLL():
  global goDbgHelpDLL;
  if goDbgHelpDLL is None:
    # All functions in DbgHelp are single threaded!
    goDbgHelpDLL = cDLL(
      "DbgHelp.dll",
      {
        "UnDecorateSymbolName": {
          "xReturnType": DWORD,
          "txArgumentTypes": (PCSTR, PSTR, DWORD, DWORD),
          "bSingleThreaded": True,
        },
        "UnDecorateSymbolNameW": {
          "xReturnType": DWORD,
          "txArgumentTypes": (PCWSTR, PWSTR, DWORD, DWORD),
          "bSingleThreaded": True,
        },
      },
    );
  return goDbgHelpDLL;