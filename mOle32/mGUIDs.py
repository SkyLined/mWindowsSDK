from .foParseGUID import foParseGUID;

__all__ = [];
for (sName, sGUID) in {
  # sapi.h
  "CLSID_SpNotifyTranslator":           "E2AE5372-5D40-11D2-960E-00C04F8EE628",
  "CLSID_SpObjectTokenCategory":        "A910187F-0C7A-45AC-92CC-59EDAFB77B53",
  "CLSID_SpObjectToken":                "EF411752-3736-4CB4-9C8C-8EF4CCB58EFE",
  "CLSID_SpResourceManager":            "96749373-3391-11D2-9EE3-00C04F797396",
  "CLSID_SpStreamFormatConverter":      "7013943A-E2EC-11D2-A086-00C04F8EF9B5",
  "CLSID_SpMMAudioEnum":                "AB1890A0-E91F-11D2-BB91-00C04F8EE6C0",
  "CLSID_SpMMAudioIn":                  "CF3D2E50-53F2-11D2-960C-00C04F8EE628",
  "CLSID_SpMMAudioOut":                 "A8C680EB-3D32-11D2-9EE7-00C04F797396",
  "CLSID_SpStream":                     "715D9C59-4442-11D2-9605-00C04F8EE628",
  "CLSID_SpVoice":                      "96749377-3391-11D2-9EE3-00C04F797396",
  "CLSID_SpSharedRecoContext":          "47206204-5ECA-11D2-960F-00C04F8EE628",
  "CLSID_SpInprocRecognizer":           "41B89B6B-9399-11D2-9623-00C04F8EE628",
  "CLSID_SpSharedRecognizer":           "3BEE4890-4FE9-4A37-8C1E-5E7E12791C1F",
  "CLSID_SpLexicon":                    "0655E396-25D0-11D3-9C26-00C04F8EF87C",
  "CLSID_SpUnCompressedLexicon":        "C9E37C15-DF92-4727-85D6-72E5EEB6995A",
  "CLSID_SpCompressedLexicon":          "90903716-2F42-11D3-9C26-00C04F8EF87C",
  "CLSID_SpShortcut":                   "0D722F1A-9FCF-4E62-96D8-6DF8F01A26AA",
  "CLSID_SpPhoneConverter":             "9185F743-1143-4C28-86B5-BFF14F20E5C8",
  "CLSID_SpPhoneticAlphabetConverter":  "4F414126-DFE3-4629-99EE-797978317EAD",
  "IID_ISpNotifySource":                "5EFF4AEF-8487-11D2-961C-00C04F8EE628",
  "IID_ISpNotifySink":                  "259684DC-37C3-11D2-9603-00C04F8EE628",
  "IID_ISpNotifyTranslator":            "ACA16614-5D3D-11D2-960E-00C04F8EE628",
  "IID_ISpDataKey":                     "14056581-E16C-11D2-BB90-00C04F8EE6C0",
  "IID_ISpRegDataKey":                  "92A66E2B-C830-4149-83DF-6FC2BA1E7A5B",
  "IID_ISpObjectTokenCategory":         "2D3D3845-39AF-4850-BBF9-40B49780011D",
  "IID_ISpObjectToken":                 "14056589-E16C-11D2-BB90-00C04F8EE6C0",
  "IID_ISpObjectTokenInit":             "B8AAB0CF-346F-49D8-9499-C8B03F161D51",
  "IID_IEnumSpObjectTokens":            "06B64F9E-7FDA-11D2-B4F2-00C04F797396",
  "IID_ISpObjectWithToken":             "5B559F40-E952-11D2-BB91-00C04F8EE6C0",
  "IID_ISpResourceManager":             "93384E18-5014-43D5-ADBB-A78E055926BD",
  "IID_ISpEventSource":                 "BE7A9CCE-5F9E-11D2-960F-00C04F8EE628",
  "IID_ISpEventSource2":                "2373A435-6A4B-429e-A6AC-D4231A61975B",
  "IID_ISpEventSink":                   "BE7A9CC9-5F9E-11D2-960F-00C04F8EE628",
  "IID_ISpStreamFormat":                "BED530BE-2606-4F4D-A1C0-54C5CDA5566F",
  "IID_ISpStream":                      "12E3CCA9-7518-44C5-A5E7-BA5A79CB929E",
  "IID_ISpStreamFormatConverter":       "678A932C-EA71-4446-9B41-78FDA6280A29",
  "IID_ISpAudio":                       "C05C768F-FAE8-4EC2-8E07-338321C12452",
  "IID_ISpMMSysAudio":                  "15806F6E-1D70-4B48-98E6-3B1A007509AB",
  "IID_ISpTranscript":                  "10F63BCE-201A-11D3-AC70-00C04F8EE6C0",
  "IID_ISpLexicon":                     "DA41A7C2-5383-4DB2-916B-6C1719E3DB58",
  "IID_ISpContainerLexicon":            "8565572F-C094-41CC-B56E-10BD9C3FF044",
  "IID_ISpShortcut":                    "3DF681E2-EA56-11D9-8BDE-F66BAD1E3F3A",
  "IID_ISpPhoneConverter":              "8445C581-0CAC-4A38-ABFE-9B2CE2826455",
  "IID_ISpPhoneticAlphabetConverter":   "133ADCD4-19B4-4020-9FDC-842E78253B17",
  "IID_ISpPhoneticAlphabetSelection":   "B2745EFD-42CE-48ca-81F1-A96E02538A90",
  "IID_ISpVoice":                       "6C44DF74-72B9-4992-A1EC-EF996E0422D4",
  "IID_ISpPhrase":                      "1A5C0354-B621-4b5a-8791-D306ED379E53",
  "IID_ISpPhraseAlt":                   "8FCEBC98-4E49-4067-9C6C-D86A0E092E3D",
  "IID_ISpPhrase2":                     "F264DA52-E457-4696-B856-A737B717AF79",
  "IID_ISpRecoResult":                  "20B053BE-E235-43cd-9A2A-8D17A48B7842",
  "IID_ISpRecoResult2":                 "27CAC6C4-88F2-41f2-8817-0C95E59F1E6E",
  "IID_ISpXMLRecoResult":               "AE39362B-45A8-4074-9B9E-CCF49AA2D0B6",
  "IID_ISpGrammarBuilder":              "8137828F-591A-4A42-BE58-49EA7EBAAC68",
  "IID_ISpRecoGrammar":                 "2177DB29-7F45-47D0-8554-067E91C80502",
  "IID_ISpGrammarBuilder2":             "8AB10026-20CC-4b20-8C22-A49C9BA78F60",
  "IID_ISpRecoGrammar2":                "4B37BC9E-9ED6-44a3-93D3-18F022B79EC3",
  "IID_ISpeechResourceLoader":          "B9AC5783-FCD0-4b21-B119-B4F8DA8FD2C3",
  "IID_ISpRecoContext":                 "F740A62F-7C15-489E-8234-940A33D9272D",
  "IID_ISpRecoContext2":                "BEAD311C-52FF-437f-9464-6B21054CA73D",
  "IID_ISpProperties":                  "5B4FB971-B115-4DE1-AD97-E482E3BF6EE4",
  "IID_ISpRecognizer":                  "C2B5F241-DAA0-4507-9E16-5A1EAA2B7A5C",
  "IID_ISpSerializeState":              "21B501A0-0EC7-46c9-92C3-A2BC784C54B9",
  "IID_ISpRecognizer2":                 "8FC6D974-C81E-4098-93C5-0147F61ED4D3",
  "IID_ISpRecoCategory":                "DA0CD0F9-14A2-4f09-8C2A-85CC48979345",
  "IID_ISpRecognizer3":                 "DF1B943C-5838-4AA2-8706-D7CD5B333499",
  "IID_ISpEnginePronunciation":         "C360CE4B-76D1-4214-AD68-52657D5083DA",
  "IID_ISpDisplayAlternates":           "C8D7C7E2-0DDE-44b7-AFE3-B0C991FBEB5E",
  "IID_ISpeechDataKey":                 "CE17C09B-4EFA-44d5-A4C9-59D9585AB0CD",
  "IID_ISpeechObjectToken":             "C74A3ADC-B727-4500-A84A-B526721C8B8C",
  "IID_ISpeechObjectTokens":            "9285B776-2E7B-4bc0-B53E-580EB6FA967F",
  "IID_ISpeechObjectTokenCategory":     "CA7EAC50-2D01-4145-86D4-5AE7D70F4469",
  "IID_ISpeechAudioBufferInfo":         "11B103D8-1142-4edf-A093-82FB3915F8CC",
  "IID_ISpeechAudioStatus":             "C62D9C91-7458-47f6-862D-1EF86FB0B278",
  "IID_ISpeechAudioFormat":             "E6E9C590-3E18-40e3-8299-061F98BDE7C7",
  "IID_ISpeechWaveFormatEx":            "7A1EF0D5-1581-4741-88E4-209A49F11A10",
  "IID_ISpeechBaseStream":              "6450336F-7D49-4ced-8097-49D6DEE37294",
  "IID_ISpeechFileStream":              "AF67F125-AB39-4e93-B4A2-CC2E66E182A7",
  "IID_ISpeechMemoryStream":            "EEB14B68-808B-4abe-A5EA-B51DA7588008",
  "IID_ISpeechCustomStream":            "1A9E9F4F-104F-4db8-A115-EFD7FD0C97AE",
  "IID_ISpeechAudio":                   "CFF8E175-019E-11d3-A08E-00C04F8EF9B5",
  "IID_ISpeechMMSysAudio":              "3C76AF6D-1FD7-4831-81D1-3B71D5A13C44",
  "IID_ISpeechVoice":                   "269316D8-57BD-11D2-9EEE-00C04F797396",
  "IID_ISpeechVoiceStatus":             "8BE47B07-57F6-11d2-9EEE-00C04F797396",
  "IID_ISpeechRecognizer":              "2D5F1C0C-BD75-4b08-9478-3B11FEA2586C",
  "IID_ISpeechRecognizerStatus":        "BFF9E781-53EC-484e-BB8A-0E1B5551E35C",
  "IID_ISpeechRecoContext":             "580AA49D-7E1E-4809-B8E2-57DA806104B8",
  "IID_ISpeechRecoGrammar":             "B6D6F79F-2158-4e50-B5BC-9A9CCD852A09",
  "IID_ISpeechGrammarRule":             "AFE719CF-5DD1-44f2-999C-7A399F1CFCCC",
  "IID_ISpeechGrammarRules":            "6FFA3B44-FC2D-40d1-8AFC-32911C7F1AD1",
  "IID_ISpeechGrammarRuleState":        "D4286F2C-EE67-45ae-B928-28D695362EDA",
  "IID_ISpeechGrammarRuleStateTransition": "CAFD1DB1-41D1-4a06-9863-E2E81DA17A9A",
  "IID_ISpeechGrammarRuleStateTransitions": "EABCE657-75BC-44a2-AA7F-C56476742963",
  "IID_ISpeechTextSelectionInformation": "3B9C7E7A-6EEE-4DED-9092-11657279ADBE",
  "IID_ISpeechRecoResult":              "ED2879CF-CED9-4ee6-A534-DE0191D5468D",
  "IID_ISpeechRecoResult2":             "8E0A246D-D3C8-45de-8657-04290C458C3C",
  "IID_ISpeechRecoResultTimes":         "62B3B8FB-F6E7-41be-BDCB-056B1C29EFC0",
  "IID_ISpeechPhraseAlternate":         "27864A2A-2B9F-4cb8-92D3-0D2722FD1E73",
  "IID_ISpeechPhraseAlternates":        "B238B6D5-F276-4c3d-A6C1-2974801C3CC2",
  "IID_ISpeechPhraseInfo":              "961559CF-4E67-4662-8BF0-D93F1FCD61B3",
  "IID_ISpeechPhraseElement":           "E6176F96-E373-4801-B223-3B62C068C0B4",
  "IID_ISpeechPhraseElements":          "0626B328-3478-467d-A0B3-D0853B93DDA3",
  "IID_ISpeechPhraseReplacement":       "2890A410-53A7-4fb5-94EC-06D4998E3D02",
  "IID_ISpeechPhraseReplacements":      "38BC662F-2257-4525-959E-2069D2596C05",
  "IID_ISpeechPhraseProperty":          "CE563D48-961E-4732-A2E1-378A42B430BE",
  "IID_ISpeechPhraseProperties":        "08166B47-102E-4b23-A599-BDB98DBFD1F4",
  "IID_ISpeechPhraseRule":              "A7BFE112-A4A0-48d9-B602-C313843F6964",
  "IID_ISpeechPhraseRules":             "9047D593-01DD-4b72-81A3-E4A0CA69F407",
  "IID_ISpeechLexicon":                 "3DA7627A-C7AE-4b23-8708-638C50362C25",
  "IID_ISpeechLexiconWords":            "8D199862-415E-47d5-AC4F-FAA608B424E6",
  "IID_ISpeechLexiconWord":             "4E5B933C-C9BE-48ed-8842-1EE51BB1D4FF",
  "IID_ISpeechLexiconPronunciations":   "72829128-5682-4704-A0D4-3E2BB6F2EAD3",
  "IID_ISpeechLexiconPronunciation":    "95252C5D-9E43-4f4a-9899-48EE73352F9F",
  "IID_ISpeechXMLRecoResult":           "AAEC54AF-8F85-4924-944D-B79D39D72E19",
  "IID_ISpeechRecoResultDispatch":      "6D60EB64-ACED-40a6-BBF3-4E557F71DEE2",
  "IID_ISpeechPhraseInfoBuilder":       "3B151836-DF3A-4E0A-846C-D2ADC9334333",
  "IID_ISpeechPhoneConverter":          "C3E4F353-433F-43d6-89A1-6A62A7054C3D",
}.items():
  if sName.startswith("CLSID_"):
    cClass = CLSID;
  else:
    assert sName.startswith("IID_"), \
        "Name %s does not start with 'CLSID_' or 'IID_'!" % sName;
    cClass = IID;
  oGUID = foParseGUID(sGUID, cClass);
  globals()[sName] = oGUID; # Make it available in the context of this file
  __all__.append(sName); # Make it available as an export from this module.
