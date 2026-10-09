# Sources

- https://developers.deepgram.com/docs/multilingual-code-switching : Nova-3 `multi` mode, the per-result `languages` array sorted by word count, and the 100 ms endpointing recommendation for code-switching.
- https://deepgram.com/pricing : Nova-3 multilingual streaming is priced above monolingual (checked 2026-10-09: $0.0058 vs $0.0048 per minute promotional, $0.0092 vs $0.0077 list). The post only says "a little higher" and links the page.
- https://docs.livekit.io/agents/logic/nodes/ : `stt_node`, `tts_node` and `on_user_turn_completed`.
- LiveKit Agents 1.8.5 source, `livekit/plugins/deepgram/stt.py` : `live_transcription_to_speech_data` copies `alt["languages"][0]` into `SpeechData.language` when the language is `multi`.
- LiveKit Agents 1.8.5 source, `agent_activity.py` : `on_user_turn_completed` receives a temporary copy of the chat context for the current generation.
- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/city-311 : the demo code quoted in the post.
- Cartesia French voice id `a249eaff-1e96-4d2c-b23b-12efa4f66f41` ("French Conversational Lady") comes from SignalWire's Cartesia voice list (https://developer.signalwire.com/voice/tts/cartesia). Verify it in the Cartesia voice library before launch; it is overridable with CITY311_VOICE_FR.
