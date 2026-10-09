# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/fair-cancellation : agent.py and policy.py code quoted in the post (OFFERS, observe_caller, make_offer, accept_offer, screen, the on_user_turn_completed hook and the tts_node). Lands on main with the worker PR on feat/cancel-demo-f4dzoy. Two quoted blocks elide log calls with `...`.
- https://www.cooley.com/news/insight/2025/2025-07-11-click-to-cancel-just-got-cancelled-eighth-circuit-vacates-entirety-of-ftcs-negative-option-rule : the Eighth Circuit vacated the FTC's 2024 Negative Option Rule amendments (Custom Communications v. FTC), decided July 8, 2025, on procedural grounds.
- https://ktslaw.com/en/insights/alert/2024/10/california-latest-automatic-renewal-law-amendments-take-effect-in-july-2025 : AB 2863 applies to contracts entered into, amended or extended on or after July 1, 2025; by phone, a discount or other benefit is allowed only if consumers are told they can cancel at any time by saying "cancel"; no obstruction or delay. This is a law-firm summary, not the statute. VERIFY against Business and Professions Code section 17602 before quoting more closely (leginfo returned 403 to our fetch).
- https://docs.livekit.io/agents/logic/nodes/ : on_user_turn_completed, StopResponse and the TTS node override.
- livekit-agents 1.8.5 source: `AgentSession.say(..., allow_interruptions=...)` and `StopResponse` exported from `livekit.agents`.

The one-offer and three-turn limits are the demo's product choices, not legal requirements. Not legal advice. No benchmark numbers or quotes. Brands and accounts are fictional.
