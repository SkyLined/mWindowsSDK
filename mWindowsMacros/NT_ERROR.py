from ..mWindowsPrimitives import NTSTATUS;

def NT_ERROR(oNTStatus):
  assert isinstance(oNTStatus, NTSTATUS), \
      "oNTStatus %s is not an NTSTATUS" % repr(oNTStatus);
  return oNTStatus.value >= 0xC0000000;
