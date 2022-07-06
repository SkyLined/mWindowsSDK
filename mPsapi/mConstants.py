from ..mWindowsConstants import __all__ as asWindowsConstantName;
from ..mWindowsConstants import *;
__all__ = asWindowsConstantName[:];

asNotToBeExported = list(globals().keys());

# Add additional constants here:

# https://docs.microsoft.com/en-us/windows/win32/api/psapi/nf-psapi-enumprocessmodulesex
LIST_MODULES_DEFAULT  =    0;
LIST_MODULES_32BIT    = 0x01;
LIST_MODULES_64BIT    = 0x02;
LIST_MODULES_ALL      = 0x03;

# Make sure everything we defined in this file is exported:
__all__ += [sName for sName in globals().keys()if sName not in asNotToBeExported];

