# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/7ee5154b5b83943dc0e9fa3f587d3bdf221a4338/demos/front-desk-interpreter : agent code quoted in the post (build_instructions, resolve_target_language with the 40-character cap, user_input_transcribed accumulation, conversation_item_added captions, active-speaker relinking with the agent-speaking guard, ui_request replay, MAX_CAPTION_ROWS = 8, Gemini Live model).
- https://github.com/mahimairaja/awesome-voice-apps/pull/76 : the hosted adapter (hosted_interp.py): GPT-Live, one visitor plays both sides, greeting kept off captions, 30-response guard.
- https://docs.livekit.io/agents/ : AgentSession, RoomIO linked participant.

Design reasoning, not measured: the cascade vs speech-to-speech trade-offs in "Why speech to speech" (no latency or accuracy numbers are claimed).
