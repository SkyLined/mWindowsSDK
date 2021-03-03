from ..mWindowsPrimitives import NTSTATUS;

def NT_SUCCESS(xNTStatus):
  if isinstance(xNTStatus, (int, long)):
    uNTStatus = xNTStatus;
  else:
    assert isinstance(oNTStatus, NTSTATUS), \
        "xNTStatus %s is not an NTSTATUS" % repr(oNTStatus);
    uNTStatus = oNTStatus.fuGetValue();
  return uNTStatus < 0x80000000;
