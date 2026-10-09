# Sources

- ITU-T G.711, https://www.itu.int/rec/T-REC-G.711 : 8 kHz telephone codec with mu-law and A-law companding.
- RFC 6716 (Opus), https://datatracker.ietf.org/doc/html/rfc6716 : in-band forward error correction (LBRR) that carries a low-bitrate copy of the previous frame.
- Deepgram keyterm prompting, https://developers.deepgram.com/docs/keyterm : Nova-3 keyterms, used for the street name on file.
- LiveKit pipeline nodes, https://docs.livekit.io/agents/logic/nodes/ : stt_node is for audio pre-processing feeding STT only; why the demo wraps AudioInput instead.
- LiveKit Agents 1.8.5 source (livekit/agents/voice/io.py, stt/stt.py): AudioInput chaining, and RecognizeStream.push_frame rejecting sample-rate changes.
- Gilbert-Elliott burst loss model: standard two-state Markov loss model; parameters are ours, in phone_line.py.
- Measurements: measure.py in this folder. 40 utterances from hf-internal-testing/librispeech_asr_dummy (validation), faster-whisper base.en int8 on CPU, beam 1, jiwer WER after lowercasing and removing punctuation, PhoneLine seed = utterance index. Run 2026-10-09:
  - web 10.03% WER; landline 11.80%; cell fixes off 15.49% (17.2% of packets silent: 7.5% lost, 9.7% late); cell fixes on 11.50% (0.2% silent, 5.6% recovered by FEC, 2.0% concealed).
- Demo source: https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/storm-outage-line
