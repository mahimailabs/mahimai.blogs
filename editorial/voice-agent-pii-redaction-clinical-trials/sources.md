# Sources: Voice Agent PII Redaction: Keep IDs Out of the LLM

- LiveKit Agents 1.8.5 source (installed package), voice/agent_activity.py: preemptive generation is on by default and builds its model request from the new transcript before `on_user_turn_completed` runs; `on_user_turn_completed` edits to `new_message` are kept in history. Checked 2026-10-09.
- LiveKit Agents nodes and hooks (https://docs.livekit.io/agents/build/nodes/): `stt_node`, `tts_node`, `on_user_turn_completed`.
- ICH E6(R2) (https://database.ich.org/sites/default/files/E6_R2_Addendum.pdf), glossary 1.58 Subject Identification Code: "used in lieu of the subject's name when the investigator reports adverse events and/or other trial related data". Checked 2026-10-09.
- Food and Drugs Regulations C.05.014 (https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._870/section-C.05.014.html): during a clinical trial the sponsor reports serious unexpected adverse drug reactions to the Minister, within 15 days, or 7 if fatal or life threatening. Checked 2026-10-09.
- Nova Scotia PIIDPA FAQ (https://novascotia.ca/just/iap/piidpaquest.asp): public bodies store and access personal information only in Canada, with exceptions.
- Quebec Law 25 (https://cloud.google.com/security/compliance/quebeclaw25): privacy impact assessment before communicating personal information outside Quebec. Secondary source; check the statute or CAI guidance before quoting further.
- The demo code: awesome-voice-apps demos/private-health-line/agent.py (`redact`, `screen`, `CountingTransport`, `DataLedger`).
