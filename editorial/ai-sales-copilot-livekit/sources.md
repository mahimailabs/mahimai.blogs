# Sources

- LiveKit, Text and transcriptions, https://docs.livekit.io/agents/multimodality/text/ : transcriptions of both sides are published on the lk.transcription text stream topic by default with AgentSession; conversation_item_added fires when text is committed to chat history.
- LiveKit, Agents v0.x migration guide (Python), https://docs.livekit.io/reference/migration-guides/v0-migration/python/ : transcriptions moved to text streams with topic lk.transcription in Agents 1.0.
- OpenAI, Structured outputs, https://platform.openai.com/docs/guides/structured-outputs : strict json_schema response format used for the line.
- OpenAI pricing (used for metering in hosted_copilot.py): text-embedding-3-small $0.02 per 1M tokens; gpt-4o-mini $0.15 per 1M input and $0.60 per 1M output tokens.
- Floor measurement (this thread, 2026-10-09): demos/sales-copilot/measure_floor.py with text-embedding-3-small, 14 on-topic lines scored 0.48 to 0.85 against the expected card, 5 greetings and small talk scored 0.23 to 0.32; 0 misses at floor 0.42.
- Latency (this thread, 2026-10-09, development container calling OpenAI directly, not the Railway worker): card 166 to 257 ms, line 948 to 2075 ms after the prospect line was committed, median line about 1.0 s, over three runs of a seven-line scripted call.
- Demo code: https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/sales-copilot (live once the worker PR merges).
- All companies (Ledgerline, Kestrel Freight, Quillpay, Tallyforge), people and figures in the demo are fictional.
