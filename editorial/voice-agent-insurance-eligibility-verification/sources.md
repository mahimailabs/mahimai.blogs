# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/payer-verification : agent.py and payer.py code quoted in the post (choose_keys, send_keys, on_user_turn_completed, hold_signals, record_benefits, apply). Lands on main with the worker PR on feat/payer-demo-xxa4ob.
- livekit-agents 1.8.5 source: `rtc.LocalParticipant.publish_dtmf(code, digit)`, `livekit.agents.beta.tools.send_dtmf_events` (calls publish_dtmf), `voice/ivr/ivr_activity.py` (TfidfLoopDetector for IVR loops), `StopResponse` in on_user_turn_completed.
- https://docs.livekit.io/telephony/making-calls/outbound-calls/ : outbound SIP calls with CreateSIPParticipant (checked via the LiveKit docs search, 2026-10-09).
- RFC 4733: RTP payload for DTMF digits and telephone events (event codes 0-9, * = 10, # = 11).
- NPI check digit: CMS spec, Luhn over the NPI with the 80840 prefix. 1234567893 is the standard valid example.
- X12 270/271: the HIPAA eligibility inquiry and response transactions.

No benchmark numbers, hold-time statistics or quotes. The payer, practice, patient and benefits are fictional.
