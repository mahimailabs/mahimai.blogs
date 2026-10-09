# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/mortgage-renewal : agent code quoted in the post (classify, OverlapGate, tts_node tee, on_user_turn_completed). Added in awesome-voice-apps feat/mortgage-demo-45t1sw; the link resolves once that PR merges.
- https://docs.livekit.io/agents/logic/turns/ : interruption modes, false interruptions (false_interruption_timeout, resume_false_interruption), min_words, and that interrupted speech is truncated to what the user heard. Read 2026-10-09.
- https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling/ : adaptive interruption; the turns overview says it is the default for agents deployed to LiveKit Cloud.
- livekit-agents 1.8.5 source (voice/turn.py, voice/agent_activity.py), read locally: defaults min_duration 0.5 s and false_interruption_timeout 2.0 s; min_words checked in _interrupt_by_audio_activity and on end of turn; on_final_transcript interrupts a paused speech; forwarded_text uses the synchronized transcript after an interruption.
- No latency figures are claimed in the post: the demo measures them per call. Not yet run against live providers (no keys in the build environment).
