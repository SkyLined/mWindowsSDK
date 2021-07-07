from ..mWindowsPrimitives import NTSTATUS;

def NT_SUCCESS(xNTStatus):
  if isinstance(xNTStatus, int):
    uNTStatus = xNTStatus;
  else:
    assert isinstance(xNTStatus, NTSTATUS), \
        "xNTStatus %s is not an NTSTATUS" % repr(xNTStatus);
    uNTStatus = xNTStatus.fuGetValue();
  return uNTStatus < 0x80000000;
