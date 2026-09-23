# WebRTC article visuals

Draft assets for **How Your Voice Travels Through WebRTC — Voice AI Agents Edition**. These are illustrations, not measurements of a real call. Not published.

| File | Placement | Suggested alt text |
| --- | --- | --- |
| 01-cover.png | Article cover | Speech travels from a caller to a voice agent, with a reply returning as audio. |
| 02-overview.png | Opening big picture | Six responsibilities: capture, connection setup, delivery, reception, agent processing, and return playback. Connection setup establishes the media path. |
| 03-packets.png | Encoding and packetization | Packet boundaries divide sound by time, not by words. Four example packets each carry 20 milliseconds of audio. |
| 04-routes.png | ICE and TURN | A browser reaches a media server directly or through a TURN relay; the media server connects to the agent. |
| 05-jitter-buffer.png | Jitter buffer | Evenly sent packets arrive at uneven intervals. Delayed, evenly spaced playback smooths that variation. |
| 06-decoding.png | Agent audio input | Forwarded media reaches an agent receiver, becomes decoded audio samples, and is prepared for speech recognition. |
| 07-response-timeline.png | Response latency | Recognition overlaps caller speech, and playback can begin while the agent is still generating its reply. |
| 08-interruption.png | Barge-in | Interruption cancels generation and clears queued audio. In-flight audio may still arrive, while audio already heard cannot be recalled. |
| 09-debugging-guide.png | Closing reference | Six symptoms mapped to the first part of the voice path to inspect, from connection setup to cancellation and playback. |

## Usage notes

- Keep captions and explanations as real article text, alongside image alt text.
- The 20 ms packet duration is an example, not a universal WebRTC setting.
- Timeline spacing is conceptual and does not establish latency measurements.
- The route diagram illustrates a media-server architecture, not every WebRTC topology.
- The debugging table gives starting points, not definitive diagnoses.
- Preserve originals; create web-optimized derivatives when integrating into the article.

## Closing architecture

`10-system-architecture.png` maps A–F to browser, SFU, agent, and model-service boundaries. It shows concurrent bidirectional media, separate connection setup, and model calls. TURN is an optional route on either WebRTC leg. This is the article’s room-based example, not every WebRTC deployment. Generated with the built-in imagegen tool.
