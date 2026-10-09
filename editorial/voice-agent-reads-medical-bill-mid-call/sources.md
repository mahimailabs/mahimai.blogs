# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/medical-bill-explainer : the demo code quoted in the post (_receive, read_bill, normalize, audit, show_lines, open_dispute).
- https://docs.livekit.io/transport/data/byte-streams/ : byte streams send files between participants on a topic; the receiver registers a handler per topic. Checked 2026-10-09.
- https://docs.livekit.io/agents/multimodality/vision/images/ : the "Upload from frontend" example reads a byte stream and adds the image to the chat context; reading can fail partway, so catch StreamError. Checked 2026-10-09.
- Measurements in the post: one run of the real read_bill() against the three sample PNGs on 2026-10-09 with gpt-4.1-mini, detail high (2.1 to 3.4 s; 1,567 to 1,751 input and 199 to 323 output tokens; all 11 lines and 44 amounts copied exactly).
- Text-only grounding checks: AgentSession test runs with gpt-4o-mini on 2026-10-09 (disputing a clean line was refused; repeated lines now trigger show_lines each time after the prompt change).
- gpt-4.1-mini prices used for cost ($0.40 per 1M input, $1.60 per 1M output): OpenAI published pricing, as used in the hosted adapter. ⚠ VERIFY before publishing.
- In-network balance billing: a contracted provider accepts the plan's allowed amount, so member cost share is at most allowed minus plan paid. General industry definition; the post avoids citing specific statutes.
