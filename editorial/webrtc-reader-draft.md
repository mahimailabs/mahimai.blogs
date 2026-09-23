# How your voice travels through WebRTC: Voice AI agents edition

You say, “Can I move my appointment to Friday?”

The agent pauses, then answers. During that pause, your audio reaches the agent, the agent decides you have finished speaking, and its reply travels back to your speaker.

A call can connect successfully and still feel terrible. The audio might arrive late. A word might change on the way through speech recognition. The agent might wait after you finish, or keep talking after you interrupt.

Let’s follow that sentence from the microphone to the agent and back. I’ve split the path into six boxes so we can look at each part separately.

## Before we open anything, here’s the whole trip

Each box below has one job. I’ll introduce the protocols as we get to them.

| Box   | What happens inside it                                                       |
| ----- | ---------------------------------------------------------------------------- |
| **A** | Your device turns sound into audio the browser can send.                     |
| **B** | The two ends agree how to communicate and establish a secure, working route. |
| **C** | Small pieces of your audio travel across that route.                         |
| **D** | The receiving system turns those pieces back into usable audio.              |
| **E** | The agent listens, decides when to answer, and produces a reply.             |
| **F** | The reply travels back and becomes sound from your speaker.                  |

**The audio path:** you → A → C → D → E → F → you.

**B sets up the connection used by that path.** It doesn’t run again for every sentence. Once connected, audio can flow both ways at the same time.

These boxes are responsibilities, not necessarily six machines. Several can run in one process. Some keep working while others wait.

We’ll follow a browser connected to a media server, with a separate agent subscribed to the audio. Think of a LiveKit-style room. A browser that connects directly to a realtime model has a different layout; check where its WebRTC connection actually ends before applying this map.

The example agent uses speech recognition, a language model, and speech synthesis. An audio-to-audio model changes box E. It still needs audio to arrive and a reply to reach the caller.

A clean network trace won’t rule out a problem with turn detection or speech recognition.

## A: You start talking. What actually leaves your browser?

The microphone produces a changing electrical signal. Your device samples it into numbers, and the browser exposes an audio track through `getUserMedia()`.

Before encoding, the browser may process the microphone audio. Echo cancellation tries to remove the speaker’s output from microphone input. Noise suppression reduces unwanted sound. Automatic gain control adjusts the level.

Those choices affect the audio the agent receives. Requesting them in your code doesn’t tell you every detail of the device’s processing. Inspect the track’s actual settings, and listen to what you capture. The [Media Capture specification](https://www.w3.org/TR/mediacapture-streams/) defines the constraints and settings the browser exposes.

Check where your recording comes from: before or after the browser processes the microphone audio.

If you compare a local recording from one point with agent audio from another, you may blame the network for a difference introduced before the first packet left.

### A frame isn’t a word

The browser’s audio encoder works on short stretches of sound. It has no reason to wait for “Friday” to finish.

We’ll use Opus with 20 milliseconds of audio per packet in this example. Your session may use a different duration. Opus allows different frame lengths, and a packet can contain more than one frame. [Opus RTP format](https://www.rfc-editor.org/rfc/rfc7587.html).

With that assumption, one second of continuous audio produces 50 packets. A boundary can cut through a vowel. A packet can include the end of one word and the start of another.

Losing a packet removes a stretch of sound. How much that affects recognition depends on which part of the sentence was in it.

The same duration of missing audio could remove a pause or part of an appointment time. Packet counts alone won’t tell you the difference.

### Smaller packets have a cost too

A packet needs its audio before it can be sent. Collecting more audio per packet adds waiting time, but sending smaller packets increases the number of headers and packet-processing operations.

Measure both the delay and processing cost when changing packet duration. It doesn’t remove the encoder’s own delay or the buffers elsewhere in the call.

Opus also supports features such as discontinuous transmission, which can reduce transmission during silence, and forward error correction, which can include recovery information for earlier audio. These depend on configuration and encoder behaviour. Don’t assume either feature is active because the codec supports it. [Opus codec specification](https://www.rfc-editor.org/rfc/rfc6716.html).

## B: How does your voice find its way to the agent?

Opening the website proves that your browser can reach a web server. The audio connection has its own setup.

The two ends exchange session descriptions: what they can send, what they can receive, and the information needed to establish the connection. The format is called **SDP**, or Session Description Protocol.

The application carries those descriptions through its signalling channel. That might use a WebSocket or an HTTP request. Sending an offer over that channel doesn’t mean your voice travels through the same channel. [WebRTC browser API](https://www.w3.org/TR/webrtc/).

Save the negotiated session description during a test. Check which codec the session actually uses, even if you requested a specific one.

SDP also carries information for connection establishment, including ICE credentials. Candidate addresses can be exchanged as they become available. The [ICE offer/answer specification](https://www.rfc-editor.org/rfc/rfc8839.html) describes how those details fit into the exchange.

### The address you know may not be the address that works

Your laptop might have a private address behind a router. The router can rewrite addresses using network address translation, or NAT. The remote endpoint cannot necessarily reach your private address directly.

**ICE**, Interactive Connectivity Establishment, gathers possible endpoints and tests candidate pairs. Some candidates come from local interfaces. Others describe a public mapping discovered with **STUN**, Session Traversal Utilities for NAT. A relay candidate provides another possible route.

ICE checks connectivity and nominates a pair. It is not a global search for the lowest-latency path across the internet. [ICE specification](https://www.rfc-editor.org/rfc/rfc8445.html).

In our example, the browser’s remote endpoint is the media server. The selected pair doesn’t describe the entire journey to the speech model. The agent and any model provider are further along the path.

That’s why moving a language model closer to the media server won’t necessarily change the browser’s connection statistics.

### Sometimes the working route needs a relay

**TURN**, Traversal Using Relays around NAT, lets an endpoint send traffic through a relay. The relay forwards it to the other endpoint. The relay continues forwarding traffic for as long as that route is in use. [TURN specification](https://www.rfc-editor.org/rfc/rfc8656.html).

Include the relay when measuring the route. Its effect on delay depends on where it runs and the network conditions.

WebRTC also supports ways through networks that block UDP, including TURN over TCP or TLS. TCP’s ordered delivery can make later data wait for earlier lost data on that connection. An audio application still has playback deadlines. [WebRTC transport requirements](https://www.rfc-editor.org/rfc/rfc8835.html).

Write down the selected route in a test report. “Same code, different Wi-Fi” can mean a different transport path.

### Connected doesn’t yet mean readable audio

The endpoints establish security using **DTLS**, Datagram Transport Layer Security. DTLS-SRTP derives keys used to protect the media with **SRTP**, Secure Real-time Transport Protocol.

Voice packets use SRTP. They don’t travel inside the DTLS connection used by a WebRTC data channel. [WebRTC security architecture](https://www.rfc-editor.org/rfc/rfc8827.html).

Check where encryption ends. Transport encryption to a media server doesn’t, by itself, hide the audio from that server. Additional end-to-end encryption is a separate design. An agent expected to understand encrypted audio needs access to the content at an authorised endpoint. [LiveKit encryption overview](https://docs.livekit.io/transport/encryption/).

A packet capture is useful here, but an encrypted payload won’t explain why the recogniser heard “Thursday.” For that, you need evidence from a point where audio is available.

## C: Your sentence arrives in pieces. Why doesn’t it sound that way?

Each media packet carries more than compressed sound.

**RTP**, Real-time Transport Protocol, provides a sequence number, a timestamp, and a source identifier. The sequence number helps identify packet order. The timestamp places the audio on the sender’s media timeline. The source identifier distinguishes streams. [RTP specification](https://www.rfc-editor.org/rfc/rfc3550.html).

That timestamp is not the wall-clock time at which a packet arrived.

For Opus over RTP, the timestamp clock runs at 48,000 ticks per second. With our 20-millisecond packet example, consecutive packets advance by 960 ticks. That clock rate does not prove your speech recogniser consumes 48 kHz audio. [Opus RTP timestamp rules](https://www.rfc-editor.org/rfc/rfc7587.html#section-4.1).

For example, these four packets could arrive at the following times:

```text
Packet        RTP timestamp       Arrival at this receiver
4100          96000               0 ms
4101          96960              23 ms
4102          97920              61 ms
4103          98880              62 ms
```

The timestamps advance evenly, but the arrival times vary.

Playing each packet immediately on arrival would turn network timing into sound timing. The receiver needs some room to absorb that variation.

### Smooth audio means waiting somewhere

A **jitter buffer** holds arriving media so it can be played in a steadier sequence. More waiting can absorb more variation, but the caller hears the result later.

WebRTC’s NetEq audio receiver also adjusts the audio itself: playback can be accelerated or slowed, missing audio can be concealed, and recovered audio can be joined back into the stream. [NetEq implementation guide](https://webrtc.googlesource.com/src/+/refs/heads/main/modules/audio_coding/neteq/g3doc/index.md).

A recording can sound continuous even when packets arrive late or go missing. The receiver may have filled the gaps.

For a voice agent, that repaired audio can become input to another model. Listen to the audio at that boundary before drawing conclusions from the transcript.

### A late packet may already be useless

Once the receiver has played past a missing stretch of audio, a late packet cannot change what the caller heard.

Retransmission and recovery only help when the repaired media is still usable. WebRTC’s media transport includes feedback and congestion handling, but no mechanism makes arbitrary network delay disappear. [WebRTC media transport](https://www.rfc-editor.org/rfc/rfc8834.html).

I’d test both isolated packet loss and bursts. Losing several consecutive packets leaves a longer gap than losing the same number spread across a sentence.

Use the same input clip, repeat the test, and listen at the receiver. Then compare the task result. Did the agent preserve the date, name, and number you cared about?

Record whether the agent booked the right appointment as well as the packet-loss rate.

## D: The audio arrived. Did the agent hear what you said?

In a room-based setup, a **selective forwarding unit**, or SFU, routes media between participants. The agent can receive a caller’s track as another participant. A media server forwarding a stream and an agent decoding it are different jobs. [LiveKit self-hosting overview](https://docs.livekit.io/transport/self-hosting/).

The model may run in that agent process or behind another connection. Draw that connection too. Calling the whole box “the backend” hides the place where audio might queue or change format.

By the time a speech recogniser consumes the input, someone has decoded the compressed audio into samples. The integration may also resample it, change the number of channels, or collect samples into larger chunks.

At each connection, check the format, sample rate, channel count, chunk duration, and queue behaviour.

Consider a recogniser that expects 16 kHz mono audio. If your decoded stream is 48 kHz, putting `16000` in a request field doesn’t resample it. It only labels the bytes differently. The receiver would interpret the same samples against a different clock.

To check for that mistake, compare the sample count with the expected audio duration.

### Your queue can become the delay

Suppose an application collects five 20-millisecond chunks before forwarding them. The first chunk spends another 80 milliseconds waiting for the other four to arrive, assuming steady arrival.

This example assumes the application waits for all five chunks. Check how your SDK batches audio before applying that calculation.

Ask how long each audio item waits between being produced and being consumed. Queue length alone is ambiguous: ten items could mean ten tiny frames or ten large chunks.

If the queue keeps growing, the consumer cannot keep up. Increasing its capacity lets older audio accumulate.

For a controlled test, compare audio after browser processing with audio immediately before recognition. Keep the recording points explicit. Then you can investigate a changed word without guessing which component changed it.

The [phone-line article](/blog/building-a-phone-line-in-pytorch) follows a different audio path through telephony. Its channel assumptions should not be silently applied to a browser’s Opus stream.

## E: You stopped speaking. Why is the agent still waiting?

Return to the sentence:

“Can I move my appointment to… Friday?”

During the pause before Friday, the speech detector sees silence. You haven’t finished your request yet.

**Voice activity detection**, or VAD, estimates whether audio contains speech. Deciding that your conversational turn is complete needs more context. Depending on the system, that decision can use silence, recogniser events, language context, or a realtime model’s own turn handling. [LiveKit turn handling](https://docs.livekit.io/agents/logic/turns/).

The browser has no protocol message that means “this person has finished explaining their request.” That decision belongs to the conversation system.

### A final transcript still needs a definition

A recogniser may finalise a segment while the person intends to continue. Before you use an event as permission to answer, check what that provider means by “final.”

I would test the pause with several continuations: a day, a correction, and a longer explanation. Keep the audio and expected behaviour with the test. Otherwise, a change that makes one short request faster can cut off the next caller.

Waiting longer reduces the risk of cutting someone off, but also delays replies when they have finished.

### Starting early makes cancellation part of the design

An agent can begin preparing a reply before it is certain you have finished. LiveKit exposes preemptive generation alongside turn and interruption settings. Work started early may need to be discarded when the user continues. [Turn-taking tuning](https://docs.livekit.io/agents/logic/turns/tuning/).

For the appointment example, an early draft might assume the request is complete before “Friday” arrives.

An early draft can be discarded. A booking change may need to be reversed. Decide which operations can run before the caller finishes and which must wait.

The same care applies to reporting speed. If generation overlaps your speech, its duration cannot simply be added to every other stage as though the whole system runs in sequence.

Even with no network problem, the agent may still be waiting for permission to answer.

## F: The agent has an answer. Why haven’t you heard it yet?

After the first text token arrives, the agent still has to generate audio and send it to the caller. Measure each of those steps separately.

A text-to-speech system may need a useful chunk of text before it can produce speech. Your application then has to deliver its output into the media path. The browser receives the returning media and prepares it for playback.

Name these events separately in a trace. LiveKit’s observability data distinguishes model and speech timing measurements, which is useful evidence for the agent’s part of the journey. Check each metric’s start and end points before treating it as the caller’s full waiting time. [Agent observability data](https://docs.livekit.io/testing/observability/data/).

“Audio sent” is especially easy to misread. It could mean added to an application queue, accepted by an SDK, or transmitted as media. Those are different timestamps.

### Measure the wait the caller experiences

For response delay, I would use this target:

```text
first audible agent speech − end of the caller’s speech
```

Then record intermediate events to explain that interval:

| Event                                              | Where to observe it                     |
| -------------------------------------------------- | --------------------------------------- |
| The caller finishes the utterance                  | A defined capture point near the caller |
| The corresponding audio reaches the agent          | Agent audio input                       |
| The turn is accepted as complete                   | Conversation controller                 |
| The first usable reply text appears                | Model stream or application             |
| The first generated speech becomes available       | Speech output                           |
| The returning audio becomes available for playback | Receiving client                        |
| The caller hears the first speech                  | Acoustic measurement at the output      |

You’ll need measurements from several points in the system. The browser alone cannot report all seven events.

For a lab test of actual audible delay, record input and speaker output on a shared timebase. If you use a browser playback estimate instead, say so. Device output and software playback events are not interchangeable measurements.

Also keep clock boundaries explicit. Two processes can both report “milliseconds since startup” and still have unrelated zeros. Subtracting those timestamps gives you a number with no useful meaning.

Use local elapsed times for local work. To align machines, document the clock alignment and its uncertainty. If your uncertainty is larger than the improvement, the trace doesn’t establish that improvement.

### The quiet part of the chart can hide the problem

A model trace might show useful work throughout the response. The caller still experiences the gaps between audible turns.

Keep the overlap visible in your trace. Speech recognition can run while you talk. Generation can start early. Audio can start playing before the entire answer exists.

Look for the chain of unfinished work that is holding back the first audible reply. Shortening work outside that chain may leave the caller’s wait unchanged.

And check the rest of the answer. A fast opening word followed by a long silence is a poor result even if first-audio timing looks good.

## You interrupt it. How much of the old answer survives?

The agent starts saying, “I can move your appointment to Friday at…”

You say, “Actually, Monday.”

The new audio travels through the incoming path while old audio may still be travelling out. Detecting the interruption is only the start of responding to it.

I would inspect four things in the application: whether generation stops, whether queued speech is cleared, whether late output is rejected, and whether conversation history reflects what was actually delivered.

Give each response an ID. When that response is cancelled, downstream consumers reject later chunks belonging to it. Cancelling one asynchronous request does not prove every task it started has stopped producing output.

There is also audio you can no longer take back. Samples already played are part of the conversation. Packets already sent may still be in transit or receiver buffers.

Measure how long the old reply remains audible after the caller interrupts.

### The next answer needs the conversation you actually had

Suppose the full generated sentence was “Friday at three is available,” but the caller only heard “Friday.” Saving the full sentence as delivered history can mislead the next response.

LiveKit documents interruption handling that truncates history to the played portion. For any stack, inspect how it estimates that boundary and what happens when playback information is delayed. [Interruption handling](https://docs.livekit.io/agents/logic/turns/#interruptions).

Finally, include the speaker in your test. The agent’s own output can return through the microphone. Test with headphones and with the device speaker, and compare the captured audio when investigating false interruptions.

After stopping playback, check the saved conversation too. It should reflect the part of the reply the caller heard.

## If the call feels wrong, where do you look first?

Start by naming the symptom. “Latency” is too broad to choose a useful measurement.

| What you observe                            | What I would check first                                            |
| ------------------------------------------- | ------------------------------------------------------------------- |
| Joining is slow, but later turns are fine   | Signalling, candidate checks, security setup, and agent readiness   |
| Audio breaks up during speech               | Arrival timing, loss, receiver concealment, and CPU pressure        |
| The transcript changes a critical word      | Audio at the recognition boundary, followed by recogniser behaviour |
| The agent waits after complete requests     | Turn decisions and the events they depend on                        |
| Speech is generated promptly but heard late | Application queues, return transport, and receiving playback        |
| Old speech continues after an interruption  | Cancellation propagation, queued output, and late chunks            |

Use these checks to narrow down the cause. Keep the same utterance and change one condition at a time.

For the browser leg, `RTCPeerConnection.getStats()` exposes transport and media observations. Read inbound audio statistics as evidence about audio received by that browser. They do not describe the microphone audio arriving at the agent.

Two useful measurements are receiver concealment and time spent in the jitter buffer. The buffer counters are cumulative: use the change in delay divided by the change in emitted count for a sampling interval. The result is an average, not a momentary peak. Compare the same stream, and skip intervals where the emitted count does not increase or the counters reset. Fields also vary in browser support. [WebRTC statistics specification](https://www.w3.org/TR/webrtc-stats/).

A candidate pair’s round-trip time measures a network round trip. Halving it does not establish one-way delay, because the two directions can differ.

Collect agent-side evidence for the other direction. Attach the session identity, stream direction, and observation point to both sets of measurements.

Save the input audio, browser and SDK versions, selected route, negotiated codec, and logs. You’ll need them to compare runs.

Repeat the sentence with a pause before Friday, during the agent’s reply, and under a controlled burst of packet loss. Compare where each run first differs.

## Now put the whole call together

The opening diagram followed one sentence. This view shows where those jobs run in the room-based system we used throughout the article.

![WebRTC system architecture: the browser captures and encodes caller audio, an SFU forwards it to the agent receiver, and the conversation controller calls STT, LLM, and TTS services. Reply audio returns through the SFU to the browser's jitter buffer, decoder, and speaker. Connection setup sits apart from both media directions.](./images/webrtc/10-system-architecture.webp)

**A lives in the browser.** The microphone, capture processing, and encoder prepare the outgoing audio. **B establishes each WebRTC connection** through signalling, ICE, and security setup. It is drawn above the media path because it does not process every spoken sentence.

**C spans the media connections.** The browser connects to the SFU, and the agent has its own WebRTC leg. Either leg may need TURN. The SFU forwards tracks; the speech models do not run inside it in this example.

**D sits at the agent's receiving boundary.** The receiver buffers and decodes the incoming audio before the application prepares samples for recognition. **E manages the conversation**, including model calls, turn decisions, tools, and interruptions. The model services can run locally or behind remote APIs. Their connections are separate from the WebRTC media legs.

**F crosses back through the system.** The agent publishes generated audio, the SFU forwards it, and the browser buffers, decodes, and plays it. That is why F appears at both ends of the return path.

These arrows show connections, not a schedule. Recognition can run while you speak. Reply audio can play while more speech is being generated. Your microphone can keep sending audio throughout, which lets the agent hear an interruption.

## Open the box where the evidence points

When a call goes wrong, compare recordings and timings at each stage. Find the first point where they differ from what you expected, then investigate that part of the system.

[_WebRTC for the Curious_](https://webrtcforthecurious.com/) is worth reading alongside this article for a deeper treatment of the protocols. Use the same sentence in a controlled call and add your own timings to this map.

## A short glossary, if you need it

| Term                            | Meaning here                                                                                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **WebRTC**                      | Web Real-Time Communication: APIs and protocols for realtime media and data connections.                                                     |
| **Sample rate**                 | The number of audio samples representing one second, measured per channel.                                                                   |
| **Codec / Opus**                | A codec encodes and decodes media. Opus is the audio codec used in this example.                                                             |
| **Frame / packet**              | A frame represents a stretch of encoded audio. A network packet carries data and headers; the two are not always one-to-one.                 |
| **Signalling / SDP**            | Signalling exchanges setup information. Session Description Protocol is a format used to describe the session.                               |
| **NAT**                         | Network Address Translation: address mapping that can affect which endpoints are reachable.                                                  |
| **ICE / candidate pair**        | Interactive Connectivity Establishment tests possible connections. A pair identifies the local and remote candidates for a path.             |
| **STUN / TURN**                 | Session Traversal Utilities for NAT helps discover mappings and check connectivity. Traversal Using Relays around NAT provides a relay.      |
| **UDP / TCP / TLS**             | User Datagram Protocol, Transmission Control Protocol, and Transport Layer Security. They provide different transport or security functions. |
| **DTLS / SRTP**                 | Datagram Transport Layer Security and Secure Real-time Transport Protocol. WebRTC uses them to establish keys and protect media.             |
| **RTP / timestamp**             | Real-time Transport Protocol carries media timing information. An RTP timestamp belongs to a media clock.                                    |
| **Jitter buffer / concealment** | The receiver smooths uneven arrival timing. Concealment supplies replacement audio when needed.                                              |
| **SFU**                         | Selective forwarding unit: a media server that forwards streams to receiving participants.                                                   |
| **VAD / turn detection**        | Voice activity detection estimates speech activity. Turn detection decides when to treat the conversational turn as complete.                |
| **STT / LLM / TTS**             | Speech-to-text, large language model, and text-to-speech: the example agent’s recognition, response, and speech stages.                      |
| **SDK / CPU**                   | Software development kit and central processing unit: the integration library and the processor doing the work.                              |
| **Playout**                     | The process of delivering received audio for playback. A software event is not necessarily the moment sound leaves the speaker.              |
