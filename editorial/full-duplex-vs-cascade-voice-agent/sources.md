# Sources

- https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/ : GPT-Live is a full-duplex model; the plugin implements it as a duplex model behind a realtime adapter; default responses delegation to a backend model.
- https://docs.livekit.io/agents/models/pipelines/ : pipeline vs realtime model trade-offs; LiveKit recommends GPT-Live for realtime.
- https://docs.livekit.io/agents/models/realtime/ : realtime models overview, overlapping speech and backchannels.
- https://developers.openai.com/api/docs/models/gpt-live-1 : the $0.05 per session minute rate, as priced in VoiceGateway 0.27.0 (`inference/pricing/realtime.py`, verified 2026-10-05). Re-check before publishing.
- livekit-agents 1.8.5 source (installed package): `Agent(llm=DuplexModel)` wraps in `DuplexRealtimeAdapter` (`voice/agent.py`); `_resolve_rt_turn_detection_enabled` in `voice/agent_activity.py` for the VAD gotcha; `MetricsReport` fields (`e2e_latency`, `end_of_turn_delay`, `transcription_delay`, `llm_node_ttft`, `tts_node_ttfb`) in `llm/chat_context.py`.
- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/interview-coach : the demo code quoted in the post (lands with the worker PR).
