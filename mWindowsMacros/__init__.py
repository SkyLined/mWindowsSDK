asOldGlobals = globals().keys() + ["asOldGlobals", "mWindowsMacros"];
from .mWindowsMacros import *;
__all__ = [sName for sName in globals().keys() if sName not in asOldGlobals];
