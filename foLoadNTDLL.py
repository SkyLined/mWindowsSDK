from cDLL import cDLL;
from mWindowsPrimitiveTypes import *;
from mWindowsStructureTypes import *;

goNTDLL = None;
def foLoadNTDLL():
  global goNTDLL;
  if goNTDLL is None:
    goNTDLL = cDLL(
      "ntdll.dll",
      {
        "NtResumeProcess": {
          "xReturnType": NTSTATUS,    
          "txArgumentTypes": (HANDLE,),
        },
        "NtSuspendProcess": {
          "xReturnType": NTSTATUS,    
          "txArgumentTypes": (HANDLE,),
        },
        "NtQueryInformationProcess": {
          "xReturnType": NTSTATUS,   
          "txArgumentTypes": (HANDLE, PROCESSINFOCLASS, PVOID, ULONG, PULONG),
        },
        "NtQueryInformationThread": {
          "xReturnType": NTSTATUS,   
          "txArgumentTypes": (HANDLE, THREADINFOCLASS, PVOID, ULONG, PULONG),
        },
      },
    );
  return goNTDLL;