# GPT-Live Research

Prepared October 5, 2026 (America/Toronto), with live documentation retrieved October 6 UTC. Research packet only; this is not a publishable article or a completed delivery review.

## Article Direction

Title: **GPT-Live with LiveKit: Beyond the First Working Call**.

Reader: a developer who can connect a voice agent and wants an inbound sales conversation to produce a correct, observable outcome. The thesis is an engineering judgment: a natural conversation is one part of a useful agent; current task state, explicit confirmation, and complete usage records make the outcome dependable. Use the simulated calendar as a concrete example throughout.

Pre-flight: no demographic, numeric, literal tutorial, or generic-noun trap. Named entities decomposed into OpenAI GPT-Live API, LiveKit GPTLiveModel plugin, the local inbound SDR demo, and VoiceGateway metering. The counter-perspective is implementation evidence and failure scenarios, not invented practitioner sentiment. Related entity: Responses backend. Time anchor: current official documentation and installed LiveKit 1.8.5. No person or social identity research was needed.

## Evidence Scope

Research used the requested LiveKit docs MCP (`docs_search`, `get_pages`), official OpenAI pages, installed package source, and local demo files. The public documents are living pages without reliable publication dates. Retrieval establishes a current snapshot, not publication within a 30- or 90-day window. A strict publication-date freshness floor is therefore unverified; do not describe it as passed. This is a practitioner implementation article, not launch news.

Official OpenAI documents form one upstream source cluster. LiveKit documentation and its package source form a second implementation cluster; source and docs are not independent vendor corroboration. Local project code is first-party implementation evidence, not a third independent study. There are no market statistics, performance measurements, external benchmarks, customer results, verified stock images, or selected YouTube embeds in this packet.

## Claim Register

| Claim | Evidence and scope | Writer action |
|---|---|---|
| GPT-Live can listen while speaking and delegate backend work. | [Getting started with GPT-Live](https://developers.openai.com/api/docs/guides/live) and [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/). | Explain through a caller correcting Friday to Monday while a lookup runs. Do not equate full duplex with perfect interruption recognition. |
| Applications own permissions, confirmations, functions, and task state; interrupting speech does not necessarily cancel backend work. | [Getting started with GPT-Live](https://developers.openai.com/api/docs/guides/live). | Make this the key boundary. The booking guard is application logic. |
| LiveKit exposes GPTLiveModel through a duplex-to-realtime adapter in AgentSession. | [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/), Overview. | Distinguish transport/session integration from business policy. |
| In Responses mode, the backend selects tools, while application function tools run in the agent process. | [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/), Tools. | Do not say GPT-Live itself directly executes the booking function. |
| GPT-Live controls its own turns; local playback can stop before the model stops generating speech. | [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/), Overview and interruptions. | Separate interruption heard by the caller from backend cancellation. |
| Voice and backend prompts have different jobs. | [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/), Voice and backend instructions. | Voice: conversation and delegation. Backend: tools and procedure. Application: enforced invariants. |
| Context channels have different purposes; appended context is absent from session.history. | [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/), Conversation context. | Log deliberate context appends separately if needed for troubleshooting, with appropriate redaction. |
| Append acknowledgement is not evidence of completed speech playback. | Installed `livekit/plugins/openai/realtime/gpt_live_model.py`, GPTLiveSession docstring lines 385-386; [Live API reference](https://developers.openai.com/api/reference/cli/resources/live), commentary_appended_event. | Keep tool completion, context acknowledgement, generated audio, and played audio distinct in any diagram or event view. |
| Voice pricing is session duration; backend usage is separate. | [GPT-Live 1 Model](https://developers.openai.com/api/docs/models/gpt-live-1): $0.05 per minute, billed per second; backend model and tools additional. | Date the rate, label any arithmetic illustrative, and do not present this as total call cost. |
| LiveKit emits duration deltas, not cumulative seconds. | [OpenAI GPT-Live plugin guide](https://docs.livekit.io/agents/models/realtime/plugins/gpt-live/), Pricing and usage; installed `_handle_usage` lines 973-994 subtract previous cumulative seconds. | Sum deltas once. Preserve session identity and event identity. Capture final close usage. |
| Backend tokens carry backend identity separately from voice metrics. | Same LiveKit Pricing and usage section; local progress evidence records LLMMetrics metadata. | Keep model identity from metric metadata. Do not assign both streams the voice component's name. |
| The simulated booking flow guards state changes and confirmation. | [booking.py](/tmp/awesome-voice-apps-gpt-live/demos/talk-to-our-team/booking.py) and [README.md](/tmp/awesome-voice-apps-gpt-live/demos/talk-to-our-team/README.md). | Describe implementation rules, not demonstrated audio behavior. Replace local citation with merged public permalink before publication. |

## Important Distinctions

**Access status.** LiveKit's current authentication section still says alpha access. The OpenAI model page is publicly listed, and the parent task reports a successful model lookup. A model lookup is not a successful Live session, and public documentation does not prove access for every account. Recommended wording: “You need an OpenAI project with access to GPT-Live.” Report any actual call attempt separately once verified.

**Delegation defaults.** The [Managing GPT-Live sessions](https://developers.openai.com/api/docs/guides/live-conversations) API guide says omitted or null delegation selects client mode. LiveKit's plugin defaults to Responses mode. State the layer whenever discussing a default.

**Mutable configuration.** The [Delegation and tools in GPT-Live](https://developers.openai.com/api/docs/guides/live-delegation) API guide allows supported Responses settings, including backend instructions, to be updated through session.update. The LiveKit guide says its instruction sets cannot be changed after session start. Avoid describing the plugin restriction as a universal API limitation.

**Client tools.** The LiveKit guide says client mode ignores function tools and logs a warning. Installed LiveKit 1.8.5 `_update_tools` actually raises `llm.RealtimeError` when tools are nonempty. Source location: [gpt_live_model.py](/tmp/gpt-live-demo-env/lib/python3.11/site-packages/livekit/plugins/openai/realtime/gpt_live_model.py:1115). Correct implementation guidance: leave registered tools empty and handle delegation events yourself, or use Responses mode. This demo uses Responses mode. Do not copy the guide's warning claim as verified runtime behavior.

**Metric semantics.** Provider usage is cumulative; plugin metrics are incremental. Native GPT-Live metric `ttft=-1` is unavailable, not a negative observed latency and not zero. The plugin's zero token values on voice duration events do not mean the voice session is free. A missing rate must remain unknown rather than silently becoming a complete zero-cost call.

## Demo Evidence

The parent progress record reports 11 offline booking tests and 48 VoiceGateway tests. This researcher did not execute those tests. No real audio call, production booking, released integration, latency benchmark, or cost reconciliation is established by this packet. Recheck the final implementation and test evidence immediately before writing claims.

The README describes a simulated calendar using weekday/time labels in America/Toronto, not dated appointments. It makes no CRM or calendar-provider call. State is per call and in memory. The deliberate lookup delay is a demonstration control, not measured provider latency. Current state logic rejects a lookup when a newer finalized caller transcript has arrived, proposes a slot, and requires a fresh standalone confirmation before one booking. A real calendar also needs durable operation identity and provider-side idempotency.

The useful story is the correction race: “Friday” launches a lookup; “Actually Monday” arrives before the lookup returns; stale Friday data cannot become a confirmed booking. Show the intended sequence as a scenario until a recorded test verifies the end-to-end behavior. A transcript event must not be mislabeled as direct proof that every spoken correction was recognized.

## Proposed Outline

All proposed section headings contain two or three words.

1. **A Useful Outcome**: Introduce the caller's need, correction, and explicitly confirmed meeting. Explain the simulated scope. Open with the outcome and a specific engineering problem.
2. **Two Working Parts**: Voice conversation versus backend work; LiveKit integration and application policy. Include one compact architecture diagram.
3. **Changing Your Mind**: The Friday-to-Monday race. Show revisions, stale lookup rejection, new offer, and fresh confirmation. Explain which behavior is deterministic application code.
4. **Context That Matters**: Thinking, commentary, instructions, and why transcript history alone cannot reconstruct everything. Include only a short purposeful code excerpt.
5. **Count Both Costs**: Duration stream plus backend tokens; unknown pricing, shutdown remainder, and actual versus estimated costs. Cite current model pricing once.
6. **Prove The Outcome**: Present actual completed checks, then real-call observations only if collected. Explain the next validation step precisely if it remains unrun.
7. **Try The Demo**: Link the merged example and prerequisites. Set clear expectations: simulated appointment, no personal details needed. Keep promotional copy out.

Avoid repeating the same API caveats in every section. The article should not become an exhaustive API reference, nor claim universal product limitations from one plugin version.

## Useful Visuals

Use the requested reladraw and imagegen workflows when the parent produces assets. No chart needs invented data.

| Visual | Content | Alt text |
|---|---|---|
| Hero illustration | Editorial split scene: a continuing voice conversation alongside a calendar correction. Treat as illustration, not a product screenshot. | A voice conversation continues while a calendar request changes from Friday to Monday. |
| Responsibility diagram | Caller and LiveKit session, GPT-Live voice, Responses backend, application tools and state. Metering receives separate duration and token streams. | GPT-Live manages speech while the backend selects tools and the application controls booking state. |
| Correction sequence | Qualitative ordered events with no millisecond scale: Friday request, lookup, Monday correction, stale result rejected, Monday offer, confirm. | A newer caller request invalidates an earlier availability result before a meeting is confirmed. |
| Usage breakdown | Two labeled inputs, seconds and backend tokens, feeding a cost record with rate provenance and completeness. No fabricated monetary totals. | Session duration and backend token usage contribute separate entries to the call cost record. |

AI image generation is recommended for the conceptual hero only. Diagrams should use exact application semantics. A real screenshot may replace a diagram after the UI exists and is inspected. Do not fabricate a dashboard screenshot that implies a completed call.

## Open Questions

- Has a real Live session connected and handled an audible correction? Required before “working call” is used as a personal test claim.
- Does the final hosted demo have admission control and preserve the authorized playground budget?
- Does VoiceGateway capture the adapter's session-level events once, include final duration usage, separate backend identity, and expose unknown rates honestly?
- Which pricing source/version and quote-time policy will the released implementation use?
- Does the UI distinguish a simulated confirmed meeting from a real calendar event?
- What are the merged demo and release permalinks? Local files are not public citations.

## Editorial Rubric

Research self-assessment, not the article's mandatory reviewer score: groundedness 28/30; specificity 24/25; coverage 14/20; actionability 14/15; format compliance 10/10; total 90/100. Coverage is limited by vendor-owned primary evidence, unavailable publication dates, and no completed audio experiment. This does not establish article delivery approval or a freshness pass.

For the eventual independent reviewer: Content Quality 30, SEO 25, E-E-A-T 15, Technical 15, AI Citation Readiness 15, as required by claude-blog. Review for a clear practical outcome; headings of two or three simple words; exact distinction between API, plugin, and application; links beside material claims; candid simulated scope; no invented tests, latency, cost totals, or conversion claims; correct responsibility diagrams and descriptive alt text; useful title/description/internal links without keyword padding. Require reviewer score at least 90 and zero P0 issues, plus the skill's separate delivery gates. Do not assign a final article score to this packet.
