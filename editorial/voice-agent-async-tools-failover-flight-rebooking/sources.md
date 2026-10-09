# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/flight-rebooking : agent code quoted in the post (search_flights, check_policy, build_llm, build_tts, FlakyLLM and FlakyTTS, the availability handlers). Path exists once the worker PR (feat/rebook-demo-1jkhfg) merges.
- https://docs.livekit.io/agents/logic/tools/async/ : ctx.update() makes a tool non-blocking, ctx.with_filler() semantics (only plays after continuous idle), on_duplicate modes.
- https://docs.livekit.io/agents/logic/tools/definition/ : function_tool basics.
- livekit-agents 1.8.5 source, read locally: llm/fallback_adapter.py (attempt_timeout default 5.0, max_retry_per_llm default 0, retry_on_chunk_sent default False, sticky, recovery probe replays the request, llm_availability_changed) and tts/fallback_adapter.py (max_retry_per_tts default 2, no sticky option, a segment that already pushed audio is not retried, tts_availability_changed). The claim that a sticky backup stops the primary from being probed comes from _llm_order and _run in that file.
- voicegateway 0.27.0 pricing, checked locally: openai/gpt-4.1-nano and openai/tts-1 are priced, openai/gpt-4o-mini-tts is not (characters unrated), which is why the TTS backup is tts-1.

"Four hundred callers" and the storm are a scenario, not a statistic. No benchmark numbers, prices or latency figures are claimed; the 8 second search and 15 second outage are the demo's own constants.
