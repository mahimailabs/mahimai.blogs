# Evidence review: Building a phone line in PyTorch

Reviewed 2026-09-30. No benchmark source changes. Validation used an isolated `uv run` environment, Python 3.12.11, torch 2.8.0, torchaudio 2.8.0, CPU.

Reproduction: `phone-validation.py`; results: `phone-validation.json`, beside this report. No global or site dependencies installed.

## Editorial decision

Describe this as an **offline narrowband channel approximation**. It models a chosen bandpass, resampling, TorchAudio mu-law quantisation and independent frame erasure with silence substitution. It does not implement a complete telephone call, wire-compatible G.711, ITU G.712 compliance, jitter, adaptive packet-loss concealment, burst loss, echo, AGC, or live RTP transport.

Suggested technical ToC: **Channel Model / Filter Response / Mu-law Quantisation / Packet Erasure / Surrogate Gradients / Reference Checks**.

## Required corrections

### Codec identity

TorchAudio's `mu_law_encoding` applies the continuous log companding formula, then uniform quantisation into 256 indexed levels. Its ordering is not the ITU G.711 PCMU byte format. The project wraps those functions directly. Replace claims of a real G.711 codec or wire-ready bytes with the named TorchAudio approximation. For deployment bit compatibility, use a G.711 implementation and reference vectors.

The two zero examples are different representations:

| Representation | Encode zero | Decode that code |
| --- | --- | --- |
| TorchAudio 2.8, 256 levels, float32 | 128 | +0.00008621309098 |
| PCMU, checked with Python 3.12 `audioop` | `0xFF` | integer PCM zero |

The analytic TorchAudio formula gives approximately +8.62116e-5, or -81.29 dBFS. This is **not a universal property of mu-law**. Avoid a universal audibility claim: audibility depends on gain and context. The older source comments and tests themselves incorrectly call this a universal mu-law/G.711 property.

### Filter / resampling

The 3.4 kHz cutoff being below the target Nyquist frequency does not guarantee zero aliasing. Finite filters have transition bands and finite stop-band attenuation. TorchAudio's resampler also uses bandlimited interpolation with its own anti-alias filter. Keep the two design responsibilities separate and inspect the complete chain at each input sample rate.

Four biquads using the correct section Q values form an eighth-order low-pass response. The source's Q formula is correct. Four copies of Q=1/sqrt(2) do not preserve the same cutoff. Avoid identifying either curve as a measured carrier or certified G.712 channel.

**Reproduced fixture:** low-pass stage only, Fs=24,000 Hz, cutoff=3,400 Hz, one-second sine at amplitude 0.1, RMS over the final 0.5 seconds, float64 CPU. The numerical results agree with direct evaluation of the digital biquad coefficients.

| Low-pass design | Gain at 3,400 Hz | Gain at 6,000 Hz |
| --- | --- | --- |
| One section, Q=1/sqrt(2) | -3.01030 dB | -13.07932 dB |
| Four correct Butterworth sections | -3.01030 dB | -51.44065 dB |
| Four repeated Q=1/sqrt(2) sections | -12.04120 dB | -52.31727 dB |

Correct Q values: 0.5097955791, 0.6013448869, 0.8999762231, 2.5629154477. The repeated-section design reaches its -3.0103 dB corner at approximately **2,328.33 Hz** at this sample rate.

Thus the old article's **10.9 dB / 42.0 dB / 2,260 Hz** figures should be replaced or removed. A chart should state that it plots the digital coefficient response at 24 kHz. Do not silently label the analytic curve a carrier measurement. A float32 sine fixture produces slightly different very-low-level RMS values because its generated tone has finite precision; do not imply universal decimal precision across dtypes and devices.

Digital low-pass coefficients used in the chart calculation:

```text
w0 = 2*pi*3400/24000
alpha = sin(w0)/(2*Q)
b = [(1-cos(w0))/2, 1-cos(w0), (1-cos(w0))/2]
a = [1+alpha, -2*cos(w0), 1-alpha]
H(f) = (b0+b1*z+b2*z^2)/(a0+a1*z+a2*z^2), z=exp(-j*2*pi*f/24000)
```

### Erasure model

At 8 kHz, the chosen 20 ms interval contains **160 samples/codes**. Twenty milliseconds is a common RTP default, not a G.711 requirement. G.711 is sample based and packetisation is a separate choice.

The project replaces each selected full 160-code block with code 128. A real lost packet has no payload; a receiver's concealment algorithm decides the replacement waveform. Call this **silence substitution**, not a realistic PLC model. Independent Bernoulli erasure does not model burst correlation.

The code leaves the final partial block unchanged. This is an implementation policy, not proof that a jitter buffer cannot lose a final short or padded packet.

Do not claim all pre-encoding masks are physically invalid. For this memoryless quantiser, replacing already-filtered 8 kHz samples with zero immediately before encoding produces the same replacement code 128. Mask placement matters when it crosses filtering, resampling or a stateful codec. Showing erasure at the encoded-frame stage is a clear simulation convention.

### Gradients / exactness

The codec-only `x + (exact - x).detach()` supplies an identity surrogate gradient. It does not make filtering, resampling or packet loss identity operations, and it is not the true derivative of quantisation. The complete chain remains lossy outside the quantiser. A fixed erasure mask removes gradients from the replaced samples; filters/resampling propagate their own gradients. TorchAudio biquads also clamp by default, so unrestricted claims of linearity need care near clipping.

The formula's forward output is **not guaranteed bit identical** after floating-point subtract/add. Reproduced with 2,000,001 float32 inputs, including a dense grid around zero: 3,766 mismatches; maximum absolute error 7.2759576e-12. Example:

```text
x          = -0.000025175966584356502
reference  = -0.00008621169399702922
arithmetic = -0.0000862116867210716
```

This difference is tiny, but it disproves the original guarantee. A custom `torch.autograd.Function` whose `forward` returns the reference encode/decode result directly and whose `backward` returns `grad_output` avoids the additional cancellation arithmetic. That custom path was bit-equal across the same fixture and produced all-one gradients for a sum loss. Scope it to the samplewise codec roundtrip, with valid normalized inputs; retain normal gradient paths for the other operations.

The written `sign(x)*log1p(mu*abs(x))` expression receives an autograd gradient of zero at exactly zero, despite the continuous analytic companding function having a nonzero derivative there. Remove “smooth and differentiable everywhere” as a blanket implementation claim. `expand(compand(x))` is algebraically an inverse pair before quantisation; floating-point results are approximate and filters are not part of that identity.

## Video verification

YouTube oEmbed confirms `3wurfKru-kE` exists and is titled **One biquad is not a phone line: filter roll-off for telephony benchmarks**, by **iKurious** (`@mahimaidev`). It is relevant by title. Its contents were not watched, so its numbers are unverified and could preserve the old article's errors. Recommend omitting it from this rewrite until reviewed.

## Primary sources

- [Benchmark codec implementation](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/codec.py)
- [Existing training codec layer](https://github.com/mahimairaja/DialTone-TTS/blob/28a1536da3f5749c904ec549616706a999856de9/packages/dialtone/src/dialtone/vocoder/codec_layer.py)
- [TorchAudio 2.8 mu-law implementation](https://docs.pytorch.org/audio/2.8.0/_modules/torchaudio/functional/functional.html#mu_law_encoding)
- [TorchAudio 2.8 biquad implementation](https://docs.pytorch.org/audio/2.8.0/_modules/torchaudio/functional/filtering.html#lowpass_biquad)
- [TorchAudio resampling](https://docs.pytorch.org/audio/main/generated/torchaudio.functional.resample.html)
- [ITU G.711 and reference-code pointer](https://www.itu.int/rec/T-REC-G.711-198811-I/en)
- [ITU G.191 reference software](https://www.itu.int/rec/T-REC-G.191/en)
- [PCMU/PCMA RTP format](https://datatracker.ietf.org/doc/html/rfc3551#section-4.5.14)
- [Default RTP packetisation interval](https://datatracker.ietf.org/doc/html/rfc3551#section-4.2)
- [Python 3.12 PCMU encode/decode implementation](https://github.com/python/cpython/blob/3.12/Modules/audioop.c)
- [Straight-through estimator paper](https://arxiv.org/abs/1308.3432)

Scope citations narrowly. Source comments and README marketing text are not proof of bit compatibility, carrier realism, or compliance.
