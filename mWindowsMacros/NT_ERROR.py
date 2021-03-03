from ..mWindowsPrimitives import NTSTATUS;

def NT_ERROR(xNTStatus):
  if isinstance(xNTStatus, (int, long)):
    uNTStatus = xNTStatus;
  else:
    assert isinstance(xNTStatus, NTSTATUS), \
        "xNTStatus %s is not an NTSTATUS" % repr(xNTStatus);
    uNTStatus = xNTStatus.fuGetValue();
  return uNTStatus >= 0xC0000000;
