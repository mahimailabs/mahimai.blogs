# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/router-rescue : the demo code quoted in the post (look_at_camera, sample_frames, contact_strip, diagnose).
- https://docs.livekit.io/agents/models/realtime/plugins/gemini/ : default video sampling, one frame per second while the user speaks and one every three seconds otherwise; `video_sampler` to change it. Checked 2026-10-09.
- https://docs.livekit.io/agents/multimodality/vision/video/ : live video input needs a realtime model with video support; models consume tokens for each frame, so higher frame rates increase cost. Checked 2026-10-09.
- https://docs.livekit.io/agents/multimodality/audio/customization/ : playing a hold message with `say()` inside a tool without awaiting it, and `disallow_interruptions()` so the result is still spoken. Checked 2026-10-09.
- https://agents-playground.livekit.io : client for running the standalone demo with a camera.
- gpt-4.1-mini prices used for per-look metering in the hosted adapter ($0.40 per 1M input, $1.60 per 1M output): from OpenAI's published pricing; not quoted in the post.
