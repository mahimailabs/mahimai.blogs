# WebRTC article: research and editorial notes

Reviewed: 2026-09-23.
Source: `../posts/how-your-voice-travels-through-webrtc.mdx`.
Reader copy: `webrtc-reader-draft.md` (derived from the MDX, with frontmatter and visual comments removed).
Status: complete text draft, `draft: true`. No publication or deployment.

## Purpose and voice

Conceptual article for engineers who already build voice agents. Explain the complete path of one utterance in plain English. Use short paragraphs, useful question headings, and the same appointment example throughout. Preserve natural sentence variation; avoid forced one-line fragments and invented personal experience.

The user's requested question headings and title take precedence over the writing-guidelines skill's documentation-specific heading conventions. Apply its clarity, concision, and acronym guidance; do not turn this essay into Vercel reference documentation.

## Source checks

- W3C Media Capture and Streams: requested constraints vs actual settings; browser microphone processing.
- RFC 7587: configurable Opus packet duration; the 48,000 Hz RTP timestamp clock, independent of decoder output rate.
- RFC 6716: Opus recovery information and discontinuous transmission are codec capabilities, not assumed negotiated settings.
- W3C WebRTC browser API / RFC 8839: signalling, session descriptions, ICE information.
- RFC 8445: candidate gathering, connectivity checks, nomination. Avoid claiming ICE globally minimizes latency.
- RFC 8656 / RFC 8835: TURN remains in the traffic path; UDP-blocked routes and TCP ordering.
- RFC 8827 / LiveKit encryption docs: DTLS-SRTP and transport encryption vs additional end-to-end protection.
- RFC 3550 / RFC 8834: RTP sequence/timestamp distinction, media deadlines, recovery and feedback.
- WebRTC NetEq implementation guide: adaptive audio playout and concealment. Avoid treating smooth playback as proof of lossless delivery.
- LiveKit self-hosting docs: media server and separate agent connection. This article selects a room-based topology rather than assuming every voice architecture is identical.
- LiveKit turn overview / tuning: VAD, turn handling, speculation, interruption and history truncation. No version-sensitive API snippets or default thresholds asserted.
- LiveKit observability data: model/audio timing endpoints differ from an acoustic measurement at the caller.
- W3C WebRTC statistics: cumulative receiver counters, direction, interval averages, and round-trip time limitations.

Direct links are next to the corresponding claims in the article. WebRTC for the Curious is credited as further reading, not condensed or copied.

## Arithmetic and examples

- 20 ms per packet is an explicit illustrative choice, not a universal default.
- 1,000 / 20 = 50 packets per second for the stated continuous packetization assumption.
- 48,000 × 0.020 = 960 RTP timestamp ticks.
- Waiting for five evenly arriving 20 ms chunks adds 4 × 20 = 80 ms to the first chunk after it is available.
- Four-packet arrival table is labelled invented. No call measurements, performance improvements, or client outcomes are asserted.

## Visual pass

1. Opening A–F map: plain-language descriptions. Put B above the stream as connection setup/control. Show the media server and agent as separate responsibilities, and the reverse media direction. This avoids implying each sentence repeats ICE/DTLS setup.
2. Packet-timing sketch: use the article's four illustrative packets; show media-clock spacing, uneven network arrival, and buffered output. Label illustrative.
3. Utterance timeline: caller, transport, agent, and playback lanes. Show overlapping work and measurement endpoints; leave performance numbers out unless a real experiment supplies them.

A real call trace would strengthen a later experimental companion or replace visual 3. It requires a recorded fixture, versioned setup, declared clock alignment, and repeatable measurements. Do not present generated imagery as measured evidence.

Use image generation for optional cover artwork. Draw technical diagrams as SVG or HTML so labels, arrows, and numbers remain controlled. No visuals have been generated in this pass.

## Review outcome

- Full narrative, return path, interruption, troubleshooting, and end glossary completed.
- Definitions appear in the text and are collected in the glossary.
- Measurements are distinguished from proposals and illustrative arithmetic.
- MDX compiles successfully; draft flag verified.
- No site component, public route, or production data changed.
