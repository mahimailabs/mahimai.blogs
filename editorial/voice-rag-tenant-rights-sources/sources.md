# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/b881d6b864b45af1e5252e2e304877e47cf2d29b/demos/tenant-rights : agent, rag.py, build_index.py and test_rag.py quoted in the post; the nv-embedqa floor (0.33) and its score ranges come from the comment in rag.py.
- https://docs.livekit.io/agents/logic/external-data/ : on_user_turn_completed for RAG and why it avoids tool round trips.
- livekit-agents 1.8.5, livekit/agents/voice/agent_activity.py : turn_ctx is `self._agent.chat_ctx.copy()` and only the user message and reply persist. ipc/job_thread_executor.py and proc_client.py: thread jobs run their own event loop.
- https://developers.openai.com/api/docs/models/text-embedding-3-small : $0.02 per 1M tokens, used for the embedding charge.
- https://www.hud.gov/states/district_of_columbia/renting/tenantrights : HUD renter resources the guidance summarizes. The demo's data file is a plain-language summary, not HUD text.
- Score table: measured 2026-10-08 with text-embedding-3-small against the eight indexed sections (script in the hosting PR thread, not committed).
- awesome-voice-apps feat/playground-tenant-rights and mahimai.ca feat/playground-tenant-rights : hosted adapter, metering and the sources panel.

No benchmark numbers or prices beyond the above.
