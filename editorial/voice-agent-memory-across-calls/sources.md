# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/returning-caller : memory.py (TTL, NEVER_KEPT, add, forget, context_block) and agent.py (remember, forget, summarize, FileStore) quoted in the post. Lands on main with the worker PR on feat/recall-demo-nlh8se.
- mahimai.ca src/server/playground/recall.ts and migrations/0024_playground_recall_memory.sql: the server-side checks and tombstones described in "Consent first, and the server checks it too". Lands with the site PR on feat/recall-demo-nlh8se.
- https://docs.livekit.io/agents/build/ (Agent.update_instructions, function tools) and the livekit-agents 1.8.5 source: JobContext.add_shutdown_callback, and the worker's shutdown_process_timeout default of 10 seconds that bounds the post-call summary.
- https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/ : PIPEDA fair information principles (identifying purposes; limiting use, disclosure and retention).
- https://gdpr-info.eu/art-5-gdpr/ : GDPR Article 5(1)(b) purpose limitation and 5(1)(e) storage limitation.
- gpt-4o-mini list prices used to bill the summary in the hosted copy ($0.15 per million input tokens, $0.60 per million output): https://openai.com/api/pricing/ . Not quoted in the post; verify before quoting.

No benchmark numbers or quotes. The bank, clients and accounts are fictional. The retention periods are the demo's choices, not a recommendation for any regulated product.
