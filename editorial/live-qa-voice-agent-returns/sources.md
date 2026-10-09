# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/returns-desk-qa : agent and QaSupervisor code quoted in the post (lands on main with the worker PR; branch feat/returns-demo-jr7e3s until then).
- awesome-voice-apps demos/drive-thru-coffee/hosted_returns.py and hosted.py (HostedReturns): grade billing and per-call grade cap.
- Grade latency (about 0.75 to 1.35 s), tokens (about 650 to 700 input, under 50 output) and the gpt-4o-mini vs gpt-4.1-mini false-flag observations: my own probe runs on 2026-10-09 with livekit-agents 1.8.5, a handful of runs each. Not a benchmark; the post says so.
- The whisper behaviour ("I'm sorry for any confusion, but we can't offer a credit for clearance items"): text-mode probe with an injected note, same date.
- llm_node vs on_user_turn_completed: checked in livekit-agents 1.8.5 source (AgentSession.run calls generate_reply with user_input, which skips on_user_turn_completed).
- https://docs.livekit.io/agents/build/nodes/ : pipeline nodes, llm_node.
- https://platform.openai.com/docs/guides/structured-outputs : strict JSON schema output.
- gpt-4.1-mini list price $0.40 / $1.60 per 1M tokens: OpenAI pricing page. ⚠ VERIFY before publishing.
