# Updated writer handoff

Updated in place: /tmp/mahimai-blogs-gpt-live/posts/gpt-live-livekit-beyond-first-call.mdx. Preserved exact approved title/subtitle, all image imports/figures, frontmatter draft:true, and ten H2s of two or three words. Added useful /learn/components/turn-detection internal link. No publication or paid execution.

## Evidence inspected

- Reread implemented agent.py and booking.py in /tmp/awesome-voice-apps-gpt-live/demos/talk-to-our-team.
- Inspected /tmp/gpt-live-sdr-audio-result-seventh.json, including event trace, final booking, usage, and public attachment records.
- Backend request configuration now shown with reasoning effort low. Context excerpt matches available-only append_thinking.
- Explained request_turn guard before a retry lookup, finalised-transcript invalidation during lookup, proposal freshness, clearing proposals on non-confirmation, and bounded three-second final-transcript wait that refuses booking when evidence is absent.
- Parent supplied final offline counts: demo 16 (14 state cases including parametrised cases plus two async race tests); VG focused 58; full suite 3916 passed, 25 skipped, two expected failures. Writer did not rerun suites.
- Seventh native synthetic-audio trace records correction15.78s, original stale result18.98s, stale retry rejection20.87s, Monday update28.98s, proposal35.45s, final confirmation48.58s, booking51.62s. Table explicitly labels elapsed events, not audible latency.
- Usage53sec voice; backend18265input,5697cached,5011cachewrites,549output including257reasoning. Summed JSON ledger entries independently: voice0.04416666666666667USD, backend0.00353689USD, total0.047703556666666674USD; article rounds appropriately.
- Verified official https://developers.openai.com/api/docs/models/gpt-5.6-luna rates: input0.20/M,cached0.02/M,output1.20/M,cachewrites1.25x input (0.25/M). Article partitions ordinaryinput7557 + cached5697 + cachewrites5011 and explains reasoning not added twice.

## Limits preserved

Single successful synthetic smoke, after development runs that failed or produced stale proposals. No aggregate reliability rate. No LiveKit room, browser/phone transport, hosted deployment, proven human offer playback, semantic interpretation guarantee, audible latency benchmark, or invoice reconciliation. Cost excludes synthetic caller generation, hosting/transport, and other deployment charges. Final shutdown increment6sec included; unavailable timing remains unknown.

request_turn proves an update happened after a transcript, not that tool arguments semantically match the caller. Article states this explicitly.

## Remaining parent work

- Replace branch demo link https://github.com/mahimairaja/awesome-voice-apps/tree/feat/gpt-live-sdr/demos/talk-to-our-team with immutable committed permalink when available.
- Metering PR https://github.com/mahimailabs/voicegateway/pull/311 unmerged/CI pending per parent checkpoint. Update that sentence only on verified changed status.
- Add durable public evidence link for native trace and test evidence; local paths stay out of article.
- Current title dates stay 2026-10-05; align actual publish/update dates when publishing.
- Delivery gates, independent review, renderer/visual checks, build, external-link validation remain parent's responsibility. This writer assigns no score or delivery-gate pass.
- Figure semantics preserved. Correction diagram remains qualitative, with transcript dependency caption; parent should inspect layout and current guard coverage before release.
