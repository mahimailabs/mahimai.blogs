# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/support-cost-router : router.py and agent.py code quoted in the post (route, TIER_TOOLS, PRICES, llm_node, metric re-emission). Lands on main with the worker PR on feat/cost-demo-v9o0ka.
- voice-prices 0.11.0 (via voicegateway 0.27.0, the playground's meter): gpt-4.1 $2.00 / $0.50 cached / $8.00 per 1M tokens, gpt-4.1-mini $0.40 / $0.10 / $1.60, gpt-4.1-nano $0.10 / $0.025 / $0.40, text-embedding-3-small $0.02 per 1M, Deepgram nova-3 $0.0048 per minute, Cartesia sonic-3 $0.05 per 1,000 characters. Checked 2026-10-09 by calling calculate_llm_cost_detail and calculate_cost_detail. Cross-check the OpenAI rows at https://openai.com/api/pricing/ before publishing.
- https://docs.livekit.io/agents/logic/nodes/ : the llm_node override pattern.
- LiveKit Agents 1.8.5 source (livekit/agents/voice/turn.py): preemptive generation is enabled by default; disabled per agent with turn_handling={"preemptive_generation": {"enabled": False}}.
- Measured on 2026-10-09 with the real OpenAI API from the build container: twelve held-out rephrasings of cached questions scored 0.54 to 0.90 on text-embedding-3-small, 8 of 12 at or above 0.70; "how do I turn off autopay" scored 0.74 against the autopay entry. Router (embedding) round trip 150 to 220 ms; cache-hit first words 147 to 194 ms; model-turn first words about 0.9 to 1.0 s. Text-mode runs via AgentSession.run, not a phone line.
- The eight-turn ledger table is one real text-mode run of the demo agent on 2026-10-09 (gpt-4.1 family, real usage chunks); cache and greeting baselines are estimates, marked ~.
- The $120,000 figure is arithmetic, not a measurement: 6,000 input tokens x $2 per 1M x 10 turns x 1,000,000 calls.

Brands, accounts and credits are fictional.
