asOldGlobals = list(globals().keys()) + ["asOldGlobals", "fInitializeProduct", "mExports"];

from .fInitializeProduct import fInitializeProduct;
fInitializeProduct();

from .mExports import *;

__all__ = [sName for sName in globals().keys() if sName not in asOldGlobals];