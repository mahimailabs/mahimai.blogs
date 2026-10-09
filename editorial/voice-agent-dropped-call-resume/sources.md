# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/loan-callback : agent.py and application.py code quoted in the post (CheckpointStore, record_answer, checkpoint, current, opening, llm_node, compact, the note argument). Lands on main with the worker PR on feat/resume-demo-0ayvj8.
- https://docs.livekit.io/agents/logic/agents-handoffs/ : session.userdata for passing state, and the summarise-before-handoff helper that uses a separate LLM call.
- https://docs.livekit.io/agents/logic/nodes/ : overriding llm_node.
- https://docs.livekit.io/reference/recipes/metrics_llm/ : per-plugin metrics_collected on the LLM instance (not deprecated; the session-level event is).
- livekit-agents 1.8.5 source (agent_activity.py): generate_reply(instructions=...) appends the turn instructions as a system message at the end of the chat context, which is why compact keeps trailing system messages.
- mahimai.ca site PR (migration 0030, src/server/playground/checkpoints.ts): versioned upsert, account looked up from the reservation, 24-hour expiry.

Token figures in the post are illustrative of the carried message's size (about 60 tokens for three answers and a note), measured with the demo's four-characters-per-token estimate. No benchmark numbers or quotes. Brands and applicants are fictional.
