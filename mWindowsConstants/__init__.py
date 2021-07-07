asOldGlobals = list(globals().keys()) + ["asOldGlobals", "mWindowsConstants"];
from .mWindowsConstants import *;
__all__ = [sName for sName in globals().keys() if sName not in asOldGlobals];
