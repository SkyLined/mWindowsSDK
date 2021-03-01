from .mWindowsPrimitiveTypes import HRESULT;
from .mWindowsConstantDefines import FACILITY_NT_BIT;

def HRESULT_FROM_NT(uNTStatus):
  return HRESULT(uNTStatus | FACILITY_NT_BIT);