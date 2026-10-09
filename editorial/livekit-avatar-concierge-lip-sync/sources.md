# Sources

- https://docs.livekit.io/agents/models/avatar/ : avatar as a separate participant, `wait_for_join()` and its 30 s default, `lk.publish_on_behalf`, `AvatarMetrics` join and playback latency, provider list.
- https://docs.livekit.io/agents/models/avatar/plugins/anam/ : Anam plugin usage, `PersonaConfig`, `ANAM_API_KEY`, director notes, AI disclosure watermark.
- livekit-agents 1.8.5 source, `livekit/agents/voice/avatar/_datastream_io.py`: RPC names `lk.clear_buffer`, `lk.playback_started`, `lk.playback_finished`, byte stream topic `lk.audio_stream`, playback position and interrupted flag on playback finished.
- livekit-plugins-anam 1.8.5 source, `avatar.py`: avatar token with `kind=agent` and `lk.publish_on_behalf`, `replace_audio_tail(DataStreamAudioOutput(...))`.
- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/hotel-concierge : the demo code quoted in the post (lands when the worker PR merges).
- Anam pricing: no official per-minute rate found publicly. Third-party pages say Anam bills by the second of session time. The post carries a VERIFY marker; confirm the rate on the account before publishing and set ANAM_USD_PER_MINUTE on the worker.
