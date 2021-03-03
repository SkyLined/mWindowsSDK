import os;

# Import all "<name>.py" files in the current folder as if we executed
#   "from <name> import <name>"
# for each of them, except for this file itself.
__all__ = [];
sFolderPath = os.path.dirname(__file__);
for sFileName in os.listdir(sFolderPath):
  sFilePath = os.path.join(sFolderPath, sFileName);
  if sFilePath == __file__:
    continue;
  sName = os.path.splitext(sFileName)[0];
  globals()[sName] = __import__(sName, globals(), locals(), [sName], -1);
  __all__.append(sName);
