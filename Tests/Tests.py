import os, sys;
sTestsFolderPath = os.path.dirname(os.path.abspath(__file__));
sMainFolderPath = os.path.dirname(sTestsFolderPath);
sParentFolderPath = os.path.dirname(sMainFolderPath);
sModulesFolderPath = os.path.join(sMainFolderPath, "modules");
asOriginalSysPath = sys.path[:];
sys.path = [sMainFolderPath, sParentFolderPath, sModulesFolderPath] + sys.path;
# Save the list of names of loaded modules:
asOriginalModuleNames = sys.modules.keys();

from mWindowsSDK import *;

# Sub-packages should load all modules relative, or they will end up in the global namespace, which means they may get
# loaded by the script importing it if it tries to load a differnt module with the same name. Obviously, that script
# will probably not function when the wrong module is loaded, so we need to check that we did this correctly.
for sModuleName in sys.modules.keys():
  assert (
    sModuleName in asOriginalModuleNames # This was loaded before cBugId was loaded
    or sModuleName.lstrip("_").split(".", 1)[0] in [
      "mWindowsSDK", # This was loaded as part of the mWindowsSDK package
      # These built-in modules are loaded by mWindowsSDK:
      "ctypes", "collections", "gc", "heapq", "itertools", "keyword", "msvcrt",
      "platform", "string", "strop", "struct", "subprocess", "thread",
      "threading", "time",
    ]
  ), \
      "Module %s was unexpectedly loaded outside of the mWindowsSDK package!" % sModuleName;
# Restore the search path
sys.path = asOriginalSysPath;

oKernel32 = cDLL("kernel32.dll", {
  "GetLastError": {
    "xReturnType": DWORD,
  },
  "GetWindowsDirectoryW": {
    "xReturnType": UINT,
    "txArgumentTypes": (LPWSTR, UINT),
  },
});

uBufferSize = MAX_PATH;
oBuffer = foCreateBuffer(uBufferSize, bUnicode = True);
ouResult = oKernel32.GetWindowsDirectoryW(
  oBuffer.foCreatePointer(LPWSTR), # lpBuffer
  uBufferSize, # uSize
);
assert ouResult.value != 0, \
    "oKernel32.GetWindowsDirectoryW(lpBuffer=0x%X, uSize=0x%X) => 0x%X" % \
    (oBuffer.fuGetAddress(), uBufferSize, oKernel32.GetLastError().value);
assert ouResult.value <= uBufferSize, \
    "Path is larger than MAX_PATH !?";
print "Windows directory = %s" % oBuffer.fsGetString();
