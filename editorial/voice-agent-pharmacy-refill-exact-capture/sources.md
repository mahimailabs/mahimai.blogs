# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/pharmacy-refill : agent and refill.py code quoted in the post (state model, capture, confirm, normalisers, make_stt, tts_node, split_ready, log_line). Lands on main with the worker PR on feat/pharmacy-demo-493bp2.
- https://docs.livekit.io/agents/logic/nodes/ : the TTS node override pattern ("add custom pronunciation rules").
- https://docs.livekit.io/agents/models/stt/deepgram/ : the keyterm parameter and updating keyterms mid-session.
- https://deepgram.com/pricing : keyterm prompting is a paid per-minute add-on. Checked only via third-party summaries (about $0.0013/min); confirm on the official page before quoting a number.
- Deepgram `redact` option ("pci", "numbers", "ssn", "true"): from the livekit-plugins-deepgram 1.8.5 STT docstring.
- Canada Post letter rules (no D, F, I, O, Q, U; no leading W or Z): encoded in POSTAL_RE.
- Tall Man lettering is the FDA/ISMP convention for look-alike drug names. The demo's capitalisations (metFORMIN, metOPROLOL) were chosen for the demo, not copied from an official list.

No benchmark numbers or quotes. Brands, patients and prescriptions are fictional.
