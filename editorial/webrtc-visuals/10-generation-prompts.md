Use case: infographic-diagram. Create a polished final technical architecture plate for Mahimai's advanced WebRTC voice-agent article. Dark mode, black #0a0a0a background, charcoal containers, crisp white text, lavender outgoing caller audio, cyan returning agent audio, muted gray dashed setup/control connections. Extremely legible professional system design, flat sharp typography, no glow or decorative 3D. Landscape 3:2, high resolution. This is NOT a sequential six-box flowchart. Nested deployment boundaries and a two-way media topology with a separate control plane. All text must be accurate and readable.

Title: "Now put the whole call together."
Subtitle: "One room-based architecture. Two audio directions. Work happens in parallel."
Small brand line: "MAHIMAI · WEBRTC"

TOP full-width detached band labeled "B · CONNECTION SETUP"
Inside concise text "Signalling + SDP • ICE + STUN • DTLS-SRTP key setup"
Below small note "Setup runs between WebRTC endpoints. It is not the speech pipeline."
Gray dashed branches from band to browser, media server, and agent SDK. No media routes through this band.

MAIN three deployment areas:
LEFT container "CALLER'S DEVICE / BROWSER".
Upper inner card "A · Capture" with "Microphone → getUserMedia()" then "Echo cancellation · noise suppression".
Below small sender card "Opus encoder · RTP / SRTP".
Lavender connector from capture through encoder out to center SFU.
Lower distinct inner card "F · Receive and play" containing "Jitter buffer · Opus decoder" and "Speaker".
Cyan connector from SFU enters this lower card. Do not connect capture to playback in series.

CENTER relatively narrow container "MEDIA SERVER".
Central card "SFU" with text "Forwards audio tracks" and "Does not run STT / LLM / TTS".
Between browser and SFU two parallel solid directional connectors: lavender toward SFU and cyan toward browser. Label area "C · Encrypted media".
Below these connectors a separate little optional box "TURN relay (if needed)" with a thin alternate bidirectional media route connecting browser and SFU via relay. Label "Alternative route". TURN must not be shown as mandatory; STUN never forwards media.
Between SFU and right agent SDK parallel lavender arrow toward agent and cyan arrow back toward SFU. Clearly label "Separate WebRTC leg".

RIGHT largest container "AGENT PROCESS".
Left/top inner card "D · Audio receiver" containing "Jitter buffer · Opus decoder" and "PCM · resampling · input queue". Lavender media arrow from SFU enters this card.
Below this receiver, inner large card "E · Conversation controller" with "VAD · turn detection · interruptions" and "Context · tools · cancellation".
Receiver connects to controller.
Bottom inner card "F · Audio publisher" containing "Output queue · Opus encoder". Controller connects down to publisher and publisher sends cyan media BACK to SFU, not straight to browser.
At far right OUTSIDE AGENT PROCESS, or in separate bottom-right detached panel with clearly separate boundary "MODEL SERVICES · local or remote".
This panel has three named ports/cards "STT", "LLM", "TTS". Three distinct short bidirectional gray connectors from conversation controller to corresponding model ports, labeled respectively "audio / transcript", "context / tokens", "text / speech". These are model API connections, NOT WebRTC arrows. Compact note "Streaming calls can overlap".
Use enough room for this model panel; make overall diagram a spatial topology with hierarchy, not a single chain. Model panel may sit below agent area to avoid crowding.

Footer legend lavender arrow "Caller audio", cyan arrow "Agent audio", gray dashed "Setup / control".
Footer exact statement "A–F are jobs, not six machines. The microphone can stay live while the reply plays."
No numeric performance claims. No logos. Avoid crossings, tiny text, ambiguous arrow endpoints and implying STUN relays audio. Retain all six A–F references, with F deliberately present at both publisher and playback.

---

Edit this architecture diagram keeping all main containers, title, typography, A-F mapping and component names. Fix accuracy and readability:
1. Remove ALL glow, gradients, haze, bloom. Entire background solid #0a0a0a; panels solid #171717, text white or light gray. Flat crisp technical editorial diagram.
2. Cyan arrow from SFU toward browser must go down then LEFT INTO the RIGHT EDGE of "F · Receive and play". Delete cyan arrow pointing into Opus encoder. Delete disconnected cyan loop above playback. ONE continuous cyan SFU-to-playback route, ending only at playback.
3. Remove TURN box and all its connections completely. Replace in the now empty center lower space with a plain text note (no arrows): "Either WebRTC leg may use a TURN relay." This avoids confusing alternative topology. Keep SFU main bidirectional media routes.
4. Remove all three connectors between model services and audio publisher/controller. Replace with ONE gray solid bidirectional line from RIGHT EDGE of E Conversation controller, routed outside the agent boundary down the far right edge, into RIGHT EDGE of MODEL SERVICES panel. Label beside line "Model calls". NO connectors between F publisher and model services. Inside MODEL SERVICES retain STT / LLM / TTS and their expansions. Add text below cards "Audio → transcript · Context → tokens · Text → speech". Retain "Streaming calls can overlap".
5. Arrow from E controller down to F publisher should be cyan (reply audio), not lavender.
6. Preserve B setup dashed connections, left capture encoder lavender route to SFU, SFU lavender route to D receiver, D downward to E, and F publisher cyan back to SFU. Preserve text "Separate WebRTC leg".
7. Footer legend gray dashed remains "Setup / control"; add thin solid gray legend "Model calls" if room.
All details must be precise, no arrow connecting wrong card. This is spatial system architecture, not temporal sequence.

---

Make exactly ONE correction to this diagram, preserve everything else pixel-for-pixel as much as possible. The lavender outgoing arrow from SFU at x855 y467 currently ends at x1040 y467 aimed at E. It MUST instead reach D Audio receiver: run horizontally from SFU to x1020 y467, bend UP vertically to y355, then bend RIGHT and end with an arrowhead at the LEFT EDGE of D Audio receiver at x1068 y355. Remove the old arrowhead at x1040 y467. This must form one continuous orthogonal lavender connector SFU → D Audio receiver. Preserve all text, other connectors, background, colors, component positions. No other changes.
