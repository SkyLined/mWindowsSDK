from .foLoadGdi32DLL import foLoadGdi32DLL;
from .mConstants import *;
from .mPrimitives import *;
from .mStructures import *;

from .mConstants import __all__ as mConstants__all__;
from .mPrimitives import __all__ as mPrimitives__all__;
from .mStructures import __all__ as mStructures__all__;

oGdi32DLL = foLoadGdi32DLL();

__all__ = mConstants__all__ + mPrimitives__all__ + mStructures__all__ + [
  "oGdi32DLL",
];

