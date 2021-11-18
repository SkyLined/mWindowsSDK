from ..mWindowsConstants import __all__ as asWindowsConstantName;
from ..mWindowsConstants import *;
__all__ = asWindowsConstantName[:];

asNotToBeExported = list(globals().keys());

# Add additional constants here:
WINHTTP_ACCESS_TYPE_DEFAULT_PROXY       =          0;
WINHTTP_ACCESS_TYPE_NO_PROXY            =          1;
WINHTTP_ACCESS_TYPE_NAMED_PROXY         =          3;
WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY     =          4;
WINHTTP_AUTO_DETECT_TYPE_DHCP           = 0x00000001;
WINHTTP_AUTO_DETECT_TYPE_DNS_A          = 0x00000002;
# Some of this comes from https://github.com/wine-mirror/wine/blob/master/include/winhttp.h
WINHTTP_AUTOPROXY_ALLOW_AUTOCONFIG      = 0x00000100;
WINHTTP_AUTOPROXY_ALLOW_CM              = 0x00000400;
WINHTTP_AUTOPROXY_ALLOW_STATIC          = 0x00000200;
WINHTTP_AUTOPROXY_AUTO_DETECT           = 0x00000001;
WINHTTP_AUTOPROXY_CONFIG_URL            = 0x00000002;
WINHTTP_AUTOPROXY_HOST_KEEPCASE         = 0x00000004;
WINHTTP_AUTOPROXY_HOST_LOWERCASE        = 0x00000008;
WINHTTP_AUTOPROXY_NO_CACHE_CLIENT       = 0x00080000;
WINHTTP_AUTOPROXY_NO_CACHE_SVC          = 0x00100000;
WINHTTP_AUTOPROXY_NO_DIRECTACCESS       = 0x00040000;
WINHTTP_AUTOPROXY_RUN_INPROCESS         = 0x00010000;
WINHTTP_AUTOPROXY_RUN_OUTPROCESS_ONLY   = 0x00020000;
WINHTTP_AUTOPROXY_SORT_RESULTS          = 0x00400000;
WINHTTP_NO_PROXY_NAME                   =       NULL;
WINHTTP_NO_PROXY_BYPASS                 =       NULL;

# Make sure everything we defined in this file is exported:
__all__ += [sName for sName in globals().keys() if sName not in asNotToBeExported];

