# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/421135071b6279dc18b211a8a03c13d27edc0ece/demos/roadside-dispatch : agent.py and health.py quoted in the post (score loop, EMA and streaks, intervention lines, capture gate, dispatch).
- https://docs.ai-coustics.com/models/audio-insight/tyto : risk_score definition (audio-derived risk indicator, 0 to 1, 0.50 is not a calibrated probability), dimensions, provisional bands 0.30 / 0.50, EMA with alpha 0.3 as an illustrative start, fixed 5 s window, real-time uses (disable barge-in, prompt the user).
- https://docs.ai-coustics.com/models/audio-insight/real-time-analysis : a 1 s interval analyzes overlapping audio; the newer SDK (3.x) and tyto-1.1 model referenced as "a newer release".
- https://docs.ai-coustics.com/models/get-started/pricing : subscription licensing, 30-day free trial, usage metered by duration of audio processed.
- Measured locally (aic-sdk 2.5.0, Python 3.11): tyto-l-16khz model file 19.8 MB; SDK import plus model load about 41 MB RSS. Inference time was not measured (needs a licence key).
- livekit-agents 1.8.5 source: AgentState includes "listening"; local sessions return to "listening" after speech, which is why the hosted wrapper watches speaking to listening.
- mahimai.ca feat/playground-roadside-dispatch and awesome-voice-apps feat/playground-roadside-dispatch : hosted wrapper (shared model, per-call analyzer, licence-optional scoring) described in "Hosting it next to other demos".

No benchmark numbers or prices quoted. The demo's 0.35 / 0.60 bands come from health.py, not from ai-coustics.
