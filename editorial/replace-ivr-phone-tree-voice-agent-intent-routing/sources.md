# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/phone-tree-router : agent.py and routing.py code quoted in the post (decide, classify, on_user_turn_completed, transfer, menu_path). Lands on main with the worker PR on feat/ivr-demo.
- https://docs.livekit.io/agents/logic/nodes/ : on_user_turn_completed runs after the user's turn, before the reply.
- https://docs.livekit.io/agents/logic/chat-context/ : messages added in on_user_turn_completed apply to the current turn only.
- https://platform.openai.com/docs/guides/structured-outputs : strict json_schema response format.
- https://cookbook.openai.com/examples/using_logprobs : logprobs for classification confidence (the approach we tried first).
- The comparison table: our own runs on 2026-10-09 against gpt-4o-mini, temperature 0, one call per sentence (scripts not committed). Single runs, not a benchmark; numbers can shift between model snapshots.
- Router latency "about 350 to 600 ms" and "roughly 300 input and 30 output tokens": same runs. The first request in each run took 1.5 to 2.3 s (cold connection).
- gpt-4o-mini list price ($0.15 per million input tokens, $0.60 per million output): voice_prices catalog bundled with voicegateway 0.27.0; the worker bills router calls at this rate.
- Menu timings (22 to 32 s for a perfect caller): computed by routing.menu_path at 150 words a minute, 0.4 s pauses, 1 s per key press. The menu is invented for the demo.

No quotes or industry statistics. Northvale, its menu and its queues are fictional.
