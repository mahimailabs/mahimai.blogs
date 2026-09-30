# Staged review: Your smoke run is lying to you

Reviewed 2026-09-30 after the second source pass. Draft: `artifacts/blog-review/series/smoke-run/draft.mdx`. Review identifier supplied by parent: `smoke-v1` (not a valid nonce-bound preflight certification). Source and component review only; the final integrated route still needs desktop/mobile/light/dark and zoom verification.

### Overall Score: 91/100 - Exceptional

| Category | Score | Maximum | Assessment |
|---|---:|---:|---|
| Content quality | 29 | 30 | Clear engineering task, concrete evidence, precise limits and useful recovery steps. |
| SEO optimization | 24 | 25 | Five technical H2s, three contextual internal links and pinned primary citations. Title remains deliberately conversational. |
| E-E-A-T signals | 13 | 15 | Public source implementation and honest historical-result boundaries; original smoke manifests remain unavailable. |
| Technical elements | 11 | 15 | Schema, assets, semantic tables and social metadata supported; speed/mobile points remain withheld. |
| AI citation readiness | 14 | 15 | Definitions, error-count tables and self-contained distinctions; historical table is not independently reproducible. |
| **Total** | **91** | **100** | **Factual/editorial clearance for local integration.** |

The same fixed 100-point denominator as the baseline is retained by task-specific instruction. Withheld runtime points are not assertions of failure. This is an internal editorial-readiness heuristic, not proof of authorship, scientific validity, search ranking or performance.

## Subpoint accounting

| Category | Explicit subpoints |
|---|---|
| Content 29/30 | Coverage 7/7; readability 7/7; originality 4/5; sentence/paragraph structure 4/4; engagement 4/4; grammar/clarity 3/3. |
| SEO 24/25 | Headings/navigation 5/5; title 3/4; semantic consistency 4/4; internal links 4/4; URL 3/3; meta description 3/3; external sources 2/2. |
| E-E-A-T 13/15 | Author 4/4; source fidelity 4/4; trust 3/4; evidence basis 2/3. |
| Technical 11/15 | Schema 4/4; image optimization 3/3; structured elements 2/2; page speed 0/2 unverified; mobile 0/2 unverified; social tags 2/2. |
| Citation 14/15 | Evidence-backed citability 3/4; purpose 3/3; entity clarity 3/3; extraction 3/3; crawler access 2/2. |

Full readability credit reflects clear prose for engineers, not a fabricated Flesch measurement. Full imagery points reflect actual WebP/SVG assets, alt text, image dimensions and loading attributes, not a claim that final placement has been screenshot-verified. Three internal links count because they are directly useful; no extra links or FAQ padding is needed. Crawler credit is based on the verified shared SSR route and robots policy, with the final draft's initial HTML still to be confirmed after integration.

## Factual clearance

- Removed the false claim that increased packet loss must monotonically increase WER.
- Correctly distinguishes independent condition-seeded masks from deliberately nested masks, and both from a recognizer's output.
- Equal rounded scores are now an investigation trigger, not proof of a broken transform.
- The current categories and round-robin sampler match the pinned `handset-bench` implementation.
- WER is explicitly aggregated over errors/reference words, not averaged utterance percentages. The calculation `100 / 114 = 0.877...` is correct.
- The larger denominator is 2,904 and the updated chart now uses `100 / 2904`, with no invented target-effect shading. Resolution is explicitly distinguished from uncertainty.
- The original smoke table is marked as a historical debugging observation whose manifests are unavailable. The rewrite does not pretend to reproduce it.
- The full-run reversal is now cited to public pinned findings: ZipVoice 4.34% versus 4.30%. I opened that source and confirmed its displayed scorecard. The article does not adopt the source document's broader, overconfident claims about all telephone-line quality.
- The ordinary Python module-cache explanation is supported by official import documentation. It avoids claiming no reload mechanism can exist.
- The rescoring command is verified in `cli.py` and `rescore.py`: default dry run, `--write` mutates records; missing transcripts cause an error. The draft now acknowledges which runner retains transcripts and that the command does not update revision metadata.

Primary checks: local `handset-bench` commit `651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a`; public pinned WER implementation and DialTone-TTS findings; Python import documentation. The other evidence agent/root verified denominators and retained record sums. I independently checked sampler, seed construction, aggregate scoring and rescoring implementation, not a new GPU benchmark run.

## Visual/component source check

- `SamplingCollapse.astro`: actual six corpus categories, 12/0/... versus 2 each; readable HTML labels; no claim equal counts reproduce category proportions.
- `BenchmarkResolution.astro`: exact denominators 114 and 2,904; one-error percentage-point bars; no statistical-confidence claim.
- `TranscriptProvenance.astro`: wide/narrow Reladraw SVG variants, native icons, SVG accessible names, shared zoom component and theme-token mapping. It explicitly says changing recognition/audio still needs recognition again.
- Hero: 1,600 × 800 transparent WebP, 299,786 bytes. Social image: 1,280 × 700 opaque JPEG, 151,720 bytes. Hero has descriptive alt, responsive widths/sizes, eager loading and high fetch priority. No claim that metadata alone proves LCP.
- Shared layout already provides author identity, GitHub, bio, BlogPosting/Person/Organization/BreadcrumbList, social tags and ToC.

## Remaining verification

These are presentation checks, not unresolved factual blockers:

1. Integrate the staged MDX and verify HTTP200 with the revised content, image URLs, two semantic tables and correct ToC.
2. Screenshot desktop/mobile in light and dark themes. Check category labels, narrow diagram text, table scroll containment, hero transparency and keyboard-visible zoom controls.
3. Open/close and zoom the diagram, then inspect console errors. Ensure old heading aliases remain usable.
4. Complete the required direct Astro check/build without invoking the remote content-sync build script.
5. Keep page-speed credit at zero unless appropriate measured evidence is supplied. Do not inflate the final score because local visual checks pass.

## Advisory editorial diagnostics

Automated extraction reports 1,083 words, 31 paragraphs, 65 sentence units, mean sentence length 14.7 words, SD6.3, coefficient0.43, TTR0.563, and no configured trigger phrases. These are MDX-parser readings, exclude imported visuals and were collected while the final source pass was settling. The analyzer incorrectly identifies hash-prefixed comments inside code fences as H1 headings; manual inspection confirms five H2 sections and the shared page H1. Its automatic score is not used as the final verdict.

Second-order review: the rewrite removes repeated “first/second/third lie” framing. Section openings now state the actual check. The short “The sample contained only digits” line functions as a concrete incident reveal, not repeated dramatic filler. The final checklist adds actionable evidence requirements instead of restating the story. No filler FAQ, keyword repetition or arbitrary graphic quota is recommended.

No P0 factual/editorial issues remain in the staged prose and current components. Missing original smoke manifests are disclosed and retained as score deductions, rather than hidden or filled with invented evidence.

BLOCKING: false (91/100 editorial/source review, no P0; cleared for local integration and the explicitly pending rendered-page checks, not production publication)
