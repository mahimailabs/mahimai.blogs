# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/billing-deescalation : agent code quoted in the post (CUES, WEIGHTS, pick_strategy, on_user_turn_completed, VOICE_BY_BAND, handoff rules, apply_credit). Added in awesome-voice-apps feat/deescalate-demo-blizln; the link resolves once that PR merges.
- https://docs.cartesia.ai/build-with-cartesia/capability-guides/volume-speed-emotion : sonic-3 generation_config speed 0.6 to 1.5, volume 0.5 to 2.0, emotion is beta and English only, primary emotions neutral, calm, angry, content, sad, scared; emotion must match the transcript. Read 2026-10-09.
- livekit-agents 1.8.5 source, read locally: voice/agent_activity.py passes a copy of the agent chat context (temp_mutable_chat_ctx) to on_user_turn_completed and uses it for the reply; plugins/cartesia/tts.py copies options (replace(tts._opts)) when each stream starts and sends speed/emotion in generation_config for sonic-3.
- https://docs.livekit.io/agents/logic/nodes/ : pipeline nodes and hooks, including on_user_turn_completed.
- The thresholds (85, 70 for three turns, two asks), weights and the $75 credit limit are the demo's own design choices, not industry figures. No benchmark or outcome numbers are claimed. Not yet run against live providers (no keys in the build environment).
