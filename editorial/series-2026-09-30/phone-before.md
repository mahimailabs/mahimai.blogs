# Baseline review: Building a phone line in PyTorch

Reviewed 2026-09-30. Source: `src/content/blog/building-a-phone-line-in-pytorch.mdx`, `SignalChain.astro`, `FilterRolloff.astro`, the YouTube wrapper, and pinned local `handset-bench` codec implementation. Shared site/schema was inspected in the preceding review. No later article was reviewed.

Rubric: claude-blog `blog-analyze`, `quality-scoring.md`, `ai-slop-detection.md`, and reviewer instructions. Same fixed denominator as the first article; unverified speed/mobile points are withheld, not marked as proven failures. This is an editorial heuristic, not a measured prediction of search ranking or authorship.

### Overall Score: 54/100 - Rewrite

| Category | Score | Max | Main reason |
|---|---:|---:|---|
| Content quality | 19 | 30 | Relevant implementation details, but several central claims overstate the simulator's fidelity and gradient behavior. |
| SEO optimization | 14 | 25 | Good readable title/path, but no contextual citations and imprecise headings/meta promise. |
| E-E-A-T signals | 7 | 15 | Accountable author; claims and measured values lack source/procedure identification. |
| Technical elements | 8 | 15 | Shared schema/social metadata, basic accessible SVG; no semantic comparison tables or article thumbnail. |
| AI citation readiness | 6 | 15 | Extractable code but unsafe-to-repeat conclusions and poorly scoped entities. |
| **Total** | **54** | **100** | **Material technical correction needed.** |

## Explicit subpoints

| Category | Subpoints |
|---|---|
| Content 19/30 | Coverage 3/7; readability 6/7; originality 2/5; sentence/paragraph structure 3/4; engagement 3/4; grammar/clarity 2/3. |
| SEO 14/25 | Headings/navigation 3/5; title 4/4; semantic consistency 3/4; internal links 0/4; URL 3/3; meta description 1/3; external sources 0/2. |
| E-E-A-T 7/15 | Author 4/4; source fidelity 0/4; trust 3/4; evidence basis 0/3. |
| Technical 8/15 | Schema 4/4; image optimization 2/3; structured elements 0/2; page speed 0/2 unverified; mobile 0/2 unverified; social metadata 2/2. |
| Citation 6/15 | Evidence-backed citability 0/4; purpose 2/3; entity clarity 1/3; extraction 1/3; crawler access 2/2. |

Coverage loses points because the article does not adequately separate a controlled narrowband proxy from a standards-conformant telephony stack. Readability is mostly good despite certainty that outruns the evidence. Originality has useful code/examples but unlinked measurements. Source fidelity is zero because multiple load-bearing claims are incorrect or unsupported, not because a citation-count quota was missed.

## Blocking findings

1. **P0 — Torchaudio mu-law indices are presented as G.711 network bytes, lines 14–30 and 63–67.** The implementation calls `torchaudio.functional.mu_law_encoding/decoding` with256 quantization channels. The stated index128 and tiny nonzero decode describe that convention; they cannot establish that standardized G.711 mu-law has no exact zero. Label the approximation and distinguish it from wire-compatible PCMU/PCMA. Evidence agent is verifying exact codec reference vectors.
2. **P0 — Gradient explanation is wrong, lines 73–85.** Filtering, downsampling and packet erasure lose information too. Their derivatives do not cancel just because ideal companding/expansion are inverse functions. An identity straight-through rule is an intentionally chosen surrogate for a bounded operation, not the true gradient through the entire phone chain. The displayed expression also requires matching shapes; a native-rate input and 8kHz output generally do not match.
3. **P0 — Synthetic response curves masquerade as actual filter responses.** `FilterRolloff.astro` scales ideal analog Butterworth dB curves by arbitrary constants to force the measured6kHz values. That distorts the -3dB corner and is neither the actual digital response nor a standard ideal Butterworth response. Plot the response computed from the implemented coefficients at an explicit sample rate, or display honestly labeled measured points without inventing connecting curves.
4. **P1 — Anti-alias guarantee is unsupported, lines 21 and 28.** A cutoff below Nyquist does not ensure sufficient attenuation above Nyquist; a finite-order lowpass is not a brick wall. Torchaudio's resampler has its own anti-alias filtering. Remove the claim that resampling cannot introduce artifacts a carrier would not produce.
5. **P1 — Compliance and universality are overclaimed, lines 38–48.** An eighth-order Butterworth with chosen band edges is a design choice, not proof of ITU-TG.712 conformity or a description of every carrier. The source sample rate and tone-measurement method are absent. The -10.9dB value means roughly28.5% amplitude, so “almost intact” is misleading.
6. **P1 — Loss/replacement/packetization are conflated, lines 30,67,69.** The simulator replaces selected full code frames with a silence index. That is a receiver replacement policy, not packet-loss concealment in general. Real packet duration may vary; the untouched trailing partial frame is an implementation policy, not a universal inference from a jitter buffer's behavior. Explain scope, Bernoulli masks and seeded reproducibility.
7. **P1 — Bit-identical forward output is not guaranteed by the displayed expression, line83.** In floating point, `x + (exact - x)` can differ from `exact` because of cancellation/rounding. Test `torch.equal` or a deliberately stated tolerance, and avoid the universal claim. The one-ULP anecdote needs a versioned source or should be presented as an observation with its limits.
8. **P2 — Some wording makes engineering differences sound unfalsifiable by definition.** Shared code reduces drift; independently implemented training/evaluation paths do not make all quality claims “unfalsifiable.” “Everything else … details” weakens the value of the careful tests the post should teach.

## Evidence and technical status

- Initial HTML at `/blog/building-a-phone-line-in-pytorch` returnedHTTP200 and contains the primary article text. It includes WebSite, Organization/ProfessionalService, Person, BlogPosting and BreadcrumbList plus OG/Twitter metadata. Zero semantic tables.
- Shared author GitHub/avatar/bio/about/contact signals are present. No body internal or external hyperlinks; an embedded YouTube player is not a primary citation for all the technical claims.
- Two SVG figures have accessible names, but text uses10–13 unit labels over624–760-wide canvases. Mobile legibility is a concern inferred from source, not a rendered failure claimed by this review.
- YouTube embed uses lazy loading and a nocookie domain. This review has not watched or verified its relevance; do not treat it as evidence that the filter numbers were reproduced.
- Pinned implementation independently confirms the native-rate biquad passes, torchaudio resampler,256-channel mu-law helpers, condition-specific seed,160-sample full-frame replacement and preserved final remainder. Comments in the code repeat some article overclaims; comments are not independent validation of compliance.

## Editorial pattern review

The parser reports618 extracted words,18 paragraphs,43 sentence units, mean15.0 words, SD10.2, variation coefficient0.68, TTR0.558 and no configured trigger phrases. These are MDX extraction-dependent diagnostics, not exact rendered prose counts or an AI-authorship inference.

Second-order: five headings repeatedly use contrast or categorical statements (“physical, not arbitrary,” “not a carrier,” “no exact zero,” “smaller than it looks”). The short technical ToC proposed by root better matches the reader's tasks. Repeated certainty—“cannot,” “only worry,” “everywhere,” “exactly,” “bit-identical,” “unfalsifiable”—is a factual problem where its scope is unsupported, rather than a banned-word exercise. There is no need to add word count, a generic FAQ or more promotional copy.

## Rewrite acceptance targets

Use the proposed ToC: Signal Path; Filter Design; Codec Fidelity; Packet Loss; Surrogate Gradients; Verification Tests. State what the proxy includes and what it cannot claim. Add exact implementation links and verified standards/library references. Replace the distorted chart with real coefficient response and expose sample rate. Show the coded silence distinction clearly. Keep a compact test matrix that separates forward equality, gradient sanity, mask behavior, codec conformance and filter response. Add the site-blending thumbnail and a readable native-icon architecture diagram. Then inspect the actual responsive route and controls.

BLOCKING: true (54/100; codec-fidelity, gradient and filter-visual errors require correction)
