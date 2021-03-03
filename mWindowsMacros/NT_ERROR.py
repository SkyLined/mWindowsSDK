from ..mWindowsPrimitives import NTSTATUS;

def NT_ERROR(xNTStatus):
  if isinstance(xNTStatus, (int, long)):
    uNTStatus = xNTStatus;
  else:
    assert isinstance(oNTStatus, NTSTATUS), \
        "xNTStatus %s is not an NTSTATUS" % repr(oNTStatus);
    uNTStatus = oNTStatus.fuGetValue();
  return uNTStatus >= 0xC0000000;
