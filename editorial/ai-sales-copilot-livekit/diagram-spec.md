# Diagram: two agents, one call

Explains why the copilot is separate from the speaking agent, and the two-stage cue.

Nodes, left to right:
1. Rep (microphone icon).
2. LiveKit room.
3. Prospect agent (speaks): STT, LLM, TTS in a row inside one box.
4. Copilot agent (silent), drawn below the prospect with a dashed outline and an ear icon.
5. Playbook index (12 cards), beside the copilot.
6. Rep's screen: a cue card with three rows (card, say, ask next).

Arrows:
- Rep to room to prospect and back: solid, audio.
- Room to copilot: dashed, labelled "both transcripts (lk.transcription)".
- Copilot to playbook index: "embed + match, ~200 ms".
- Copilot to screen, two arrows: "card" (solid, ink) and "line, ~1 s" (purple).
- No arrow from the copilot into the room's audio: label the gap "never speaks".

Layout: black stage, purple glow for the copilot path, coral for nothing (nothing breaks here).
