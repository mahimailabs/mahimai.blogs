# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/pronunciation-coach : agent.py and coach.py code quoted in the post (stt_node, hear, align, on_user_turn_completed, brief, turn_handling, the drill and level thresholds). Lands on main with the worker PR on feat/pronounce-demo-n8gyp4.
- livekit-agents 1.8.5 source: `SpeechData.words` holds `TimedString` objects with a per-word `confidence`; `livekit-plugins-deepgram` fills them from each word's `confidence` in the streaming response (`live_transcription_to_speech_data`).
- livekit-agents 1.8.5 source: per-agent `turn_handling` with `endpointing.min_delay` (default 0.5 s) and `preemptive_generation.enabled` (default on).
- https://docs.livekit.io/agents/logic/nodes/ : the STT node override and `on_user_turn_completed` hooks.
- https://developers.deepgram.com/docs/keyterm : keyterm prompting biases recognition toward listed terms; the post's argument against using it for assessment is our own reasoning, not Deepgram's guidance.
- Python `difflib.SequenceMatcher`: standard library alignment used for heard against target words.

The thresholds (0.85 clear, 0.70 pass, 0.88 up, 0.55 down) are the demo's starting points, not measured benchmarks. No benchmark numbers, prices or quotes. Brands are fictional.
