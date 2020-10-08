import mErrorDefines;

dErrorDefine_sName_by_uValue = dict([
  (
    getattr(mErrorDefines, sErrorDefineName),
    sErrorDefineName
  )
  for sErrorDefineName in dir(mErrorDefines)
  if sErrorDefineName.upper() == sErrorDefineName
]);

def fs0GetErrorDefineName(uValue):
  return dErrorDefine_sName_by_uValue.get(uValue);
