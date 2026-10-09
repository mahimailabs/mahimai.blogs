# Sources

- https://docs.livekit.io/agents/models/avatar/ : avatar as a separate participant, `wait_for_join()` and its 30 s default, `lk.publish_on_behalf`, `AvatarMetrics` join and playback latency, provider list.
- https://docs.livekit.io/agents/models/avatar/plugins/spatius/ : Spatius plugin usage, `SPATIUS_API_KEY`, `SPATIUS_APP_ID`, `SPATIUS_AVATAR_ID`, client-side rendering with 3D Gaussian splatting, black frame in the Agent Console, Ogg Opus sample rates.
- livekit-plugins-spatius 1.8.5 source, `avatar.py`: egress token with `kind=agent`, publish only and `lk.publish_on_behalf`; `QueueAudioOutput` forwarding to the Spatius session; interrupt on clear buffer with a 2 s local fallback; `lk.playback_started` and `lk.playback_finished` RPCs with playback position and interrupted flag.
- https://docs.spatius.ai/livekit-agents/client and `@spatius/avatarkit-rtc` 1.1.5 type definitions: `AvatarPlayer.attach(room)` before `room.connect()`, `Room({ singlePeerConnection: false })`, `RTCRtpScriptTransform` requirement.
- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/hotel-concierge : the demo code quoted in the post (lands when the worker PR merges).
- Spatius pricing: no official per-minute rate read directly. Third-party listings (voiceaispace.com, toolify.ai) show credit plans from $19 for about 2,000 minutes, roughly $0.007 to $0.01 a minute. The post carries a VERIFY marker; confirm on the account and set SPATIUS_USD_PER_MINUTE on the worker.
