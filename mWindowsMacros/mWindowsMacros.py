import os;

# Import all "<name>.py" files in the current folder as if we executed
#   "from <name> import <name>"
# for each of them, except for this file itself and "__init__.py".
sMainFileName = os.path.basename(__file__);
sFolderPath = os.path.dirname(os.path.abspath(__file__));
oExcludedFileNames = frozenset((sMainFileName, "__init__.py"));
__all__ = [];
for sFileName in os.listdir(sFolderPath):
  if not sFileName.endswith(".py") or sFileName in oExcludedFileNames:
    continue;
  sImportName = os.path.splitext(sFileName)[0];
  globals()[sImportName] = getattr(__import__(sImportName, globals(), locals(), [sImportName], -1), sImportName);
  __all__.append(sImportName);
