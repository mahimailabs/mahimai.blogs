# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/agent-stress-test : agent.py and stresstest.py code quoted in the post (personas, SOUND_ALIKES, simulate, CodeCheck, make_judges, POLICY, Billing.credit). Lands on main with the worker PR on feat/stresstest-demo-747t1p.
- https://docs.livekit.io/testing/unit-tests/ : AgentSession.run in text mode, JudgeGroup, the built-in judges in livekit.agents.evals.
- https://docs.livekit.io/testing/simulations/ : LiveKit Cloud Agent Simulations, scenarios.yaml, running simulations in CI.
- livekit-agents 1.8.5 source, livekit/agents/evals/judge.py : task_completion_judge grades against the latest agent instructions; safety_judge criteria; Judge base class for programmatic checks.
- Numbers in the post (v1 30/42 and v2 42/42; an earlier v2 run at 38/42 with the accent caller unverified; 9 to 14 seconds per suite; about one cent for v1 plus v2; the safety judge passing a leaked code in a live call) come from our own runs on 2026-10-09 against gpt-4o-mini. They vary run to run; the post says so.
- gpt-4o-mini prices used for metering: $0.15 per million input tokens, $0.075 cached, $0.60 output. ⚠ VERIFY on https://openai.com/api/pricing before quoting.

No quotes from third parties. Halden Fiber, Ava, the account and the callers are fictional.
