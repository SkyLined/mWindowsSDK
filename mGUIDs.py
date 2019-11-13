from .foParseGUID import foParseGUID;

for (sName, sGUID) in {
  "CATID_ActiveScript":                       "{F0B7A1A1-9847-11cf-8F20-00805F2CD064}",
  "CATID_ActiveScriptParse":                  "{F0B7A1A2-9847-11cf-8F20-00805F2CD064}",
  "CATID_ActiveScriptEncode":                 "{F0B7A1A3-9847-11cf-8F20-00805F2CD064}",
  "IID_IActiveScript":                        "{BB1A2AE1-A4F9-11cf-8F20-00805F2CD064}",
  "IID_IActiveScriptParse32":                 "{BB1A2AE2-A4F9-11cf-8F20-00805F2CD064}",
  "IID_IActiveScriptParse64":                 "{C7EF7658-E1EE-480E-97EA-D52CB4D76D17}",
  "IID_IActiveScriptEncode":                  "{BB1A2AE3-A4F9-11cf-8F20-00805F2CD064}",
  "IID_IActiveScriptHostEncode":              "{BEE9B76E-CFE3-11d1-B747-00C04FC2B085}",
  "IID_IActiveScriptParseProcedureOld32":     "{1CFF0050-6FDD-11d0-9328-00A0C90DCAA9}",
  "IID_IActiveScriptParseProcedureOld64":     "{21F57128-08C9-4638-BA12-22D15D88DC5C}",
  "IID_IActiveScriptParseProcedure32":        "{AA5B6A80-B834-11d0-932F-00A0C90DCAA9}",
  "IID_IActiveScriptParseProcedure64":        "{C64713B6-E029-4CC5-9200-438B72890B6A}",
  "IID_IActiveScriptParseProcedure2_32":      "{71EE5B20-FB04-11d1-B3A8-00A0C911E8B2}",
  "IID_IActiveScriptParseProcedure2_64":      "{FE7C4271-210C-448D-9F54-76DAB7047B28}",
  "IID_IActiveScriptSite":                    "{DB01A1E3-A42B-11cf-8F20-00805F2CD064}",
  "IID_IActiveScriptSiteTraceInfo":           "{4B7272AE-1955-4bfe-98B0-780621888569}",
  "IID_IActiveScriptSiteWindow":              "{D10F6761-83E9-11cf-8F20-00805F2CD064}",
  "IID_IActiveScriptSiteInterruptPoll":       "{539698A0-CDCA-11CF-A5EB-00AA0047A063}",
  "IID_IActiveScriptSiteUIControl":           "{AEDAE97E-D7EE-4796-B960-7F092AE844AB}",
  "IID_IActiveScriptError":                   "{EAE1BA61-A4ED-11cf-8F20-00805F2CD064}",
  "IID_IActiveScriptError64":                 "{B21FB2A1-5B8F-4963-8C21-21450F84ED7F}",
  "IID_IBindEventHandler":                    "{63CDBCB0-C1B1-11d0-9336-00A0C90DCAA9}",
  "IID_IActiveScriptStats":                   "{B8DA6310-E19B-11d0-933C-00A0C90DCAA9}",
  "IID_IActiveScriptProperty":                "{4954E0D0-FBC7-11D1-8410-006008C3FBFC}",
  "IID_ITridentEventSink":                    "{1DC9CA50-06EF-11d2-8415-006008C3FBFC}",
  "IID_IActiveScriptGarbageCollector":        "{6AA2C4A0-2B53-11d4-A2A0-00104BD35090}",
  "IID_IActiveScriptSIPInfo":                 "{764651D0-38DE-11d4-A2A3-00104BD35090}",
  "IID_IActiveScriptTraceInfo":               "{C35456E7-BEBF-4a1b-86A9-24D56BE8B369}",
  "OID_VBSSIP":                               "{1629F04E-2799-4db5-8FE5-ACE10F17EBAB}",
  "OID_JSSIP":                                "{06C9E010-38CE-11d4-A2A3-00104BD35090}",
  "OID_WSFSIP":                               "{1A610570-38CE-11d4-A2A3-00104BD35090}",
  "IID_IActiveScriptStringCompare":           "{58562769-ED52-42f7-8403-4963514E1F11}",
}.items():
  oGUID = foParseGUID(sGUID);
  globals()[sName] = oGUID; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.
