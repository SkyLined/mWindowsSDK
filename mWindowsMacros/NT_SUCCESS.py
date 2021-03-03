from ..mWindowsPrimitives import NTSTATUS;

def NT_SUCCESS(oNTStatus):
  assert isinstance(oNTStatus, NTSTATUS), \
      "oNTStatus %s is not an NTSTATUS" % repr(oNTStatus);
  return oNTStatus.value < 0x80000000;
