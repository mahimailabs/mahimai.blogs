# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/postop-checkin : agent.py and protocol.py code quoted in the post (typed record tools, RULES, _evaluate, tier, record, handoff). Lands on main with the worker PR on feat/postop-demo-os9vcp.
- https://docs.livekit.io/agents/build/tools/ : function_tool and how Python type hints become the tool schema.
- https://platform.openai.com/docs/guides/function-calling : strict mode schemas (all fields required, nullable via a type list, enums). The `["number", "null"]` and enum output was checked offline with livekit-agents 1.8.5 `build_strict_openai_schema`.
- https://developers.deepgram.com/docs/smart-format : smart formatting writes spoken numbers as digits.
- https://www.ihi.org/resources/tools/sbar-tool-situation-background-assessment-recommendation : SBAR as a clinical handoff structure.
- Nurse telephone triage protocols (for example Schmitt-Thompson) ask emergency-level questions first; stated in general terms, not quoted.

The thresholds (101.5°F, pain 8 with medication not helping) belong to the fictional Northfield General protocol and are not medical advice. ⚠ VERIFY: if the post is ever reworded to say real hospitals use 101.5°F, cite a real discharge instruction first. No benchmark numbers or quotes. Hospital, patients and protocol are fictional.
