from ..mWindowsConstants import __all__ as asWindowsConstantName;
from ..mWindowsConstants import *;
__all__ = asWindowsConstantName[:];

asNotToBeExported = list(globals().keys());

# Add additional constants here:
D3DKMT_CLIENTHINT_UNKNOWN               = 0;
D3DKMT_CLIENTHINT_OPENGL                = 1;
D3DKMT_CLIENTHINT_CDD                   = 2;
D3DKMT_CLIENTHINT_OPENCL                = 3;
D3DKMT_CLIENTHINT_VULKAN                = 4;
D3DKMT_CLIENTHINT_CUDA                  = 5;
D3DKMT_CLIENTHINT_RESERVED              = 6;
D3DKMT_CLIENTHINT_DX7                   = 7;
D3DKMT_CLIENTHINT_DX8                   = 8;
D3DKMT_CLIENTHINT_DX9                   = 9;
D3DKMT_CLIENTHINT_DX10                  = 10;
D3DKMT_CLIENTHINT_DX11                  = 11;
D3DKMT_CLIENTHINT_DX12                  = 12;
D3DKMT_CLIENTHINT_9ON12                 = 13;
D3DKMT_CLIENTHINT_11ON12                = 14;
D3DKMT_CLIENTHINT_MFT_ENCODE            = 15;
D3DKMT_CLIENTHINT_MAX                   = 16;

# Make sure everything we defined in this file is exported:
__all__ += [sName for sName in globals().keys()if sName not in asNotToBeExported];

