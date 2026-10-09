# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/delivery-window-call : agent code quoted in the post (dialling, AMD branch, DTMF path, tools). Added in awesome-voice-apps PR for branch feat/delivery-demo-s2feoe.
- https://docs.livekit.io/telephony/features/answering-machine-detection/ : AMD categories, the parallel heuristic and LLM paths, default thresholds (2.5 s, 0.5 s, 1.5 s, 10 s), default Inference models, evaluated model list.
- https://docs.livekit.io/telephony/making-calls/outbound-calls/ : voicemail answers with 200 OK so wait_until_answered succeeds; SipCallError with SIP status codes; ringing timeout.
- https://docs.livekit.io/reference/telephony/sip-participant/ : sip.callStatus values (dialing until answered, then active).
- https://docs.livekit.io/telephony/features/dtmf/ : sip_dtmf_received, publishDtmf, GetDtmfTask.
- https://github.com/livekit/agents/blob/main/examples/telephony/amd.py : the reference flow (set_participant before AMD, create_sip_participant inside the AMD context).
- AMD constructor (llm, stt=None reuses session transcripts, suppress_compatibility_warning) checked in livekit-agents 1.8.5 source, livekit/agents/voice/amd/detector.py.

No benchmark numbers or prices. AMD timing shown in the demo panel comes from the live call, not from the post.
