# Baseline review: Your smoke run is lying to you

Reviewed 2026-09-30. Source: `src/content/blog/your-smoke-run-is-lying-to-you.mdx`, its two figure components, and shared article layout/SEO/footer/robots implementation. Only this post was reviewed.

Rubric: claude-blog `blog-analyze`, `quality-scoring.md`, `ai-slop-detection.md`, and `agents/blog-reviewer.md`, read from `/tmp/mahimai-claude-blog-review-20260930`. This is an internal editorial-readiness heuristic, not an SEO ranking forecast, accuracy guarantee, or AI-authorship score.

### Overall Score: 59/100 - Rewrite

| Category | Score | Maximum | Assessment |
|---|---:|---:|---|
| Content quality | 21 | 30 | Useful concrete incident, but an incorrect diagnostic rule and overstated conclusions undermine it. |
| SEO optimization | 14 | 25 | Readable path and topical consistency; no contextual links and weak section names. |
| E-E-A-T signals | 8 | 15 | Accountable author; experiment has no linked artifacts or reproducible provenance. |
| Technical elements | 8 | 15 | Raw fixed denominator; 4 unverified speed/mobile points withheld. |
| AI citation readiness | 8 | 15 | Specific examples, but unsupported conclusions and machine-unfriendly results blocks. |
| **Total** | **59** | **100** | **Substantive correction required.** |

## Explicit subpoints

### Content quality: 21/30

| Check | Score | Max | Reason |
|---|---:|---:|---|
| Coverage | 4 | 7 | Sampling, metric granularity, module lifetime and transcript retention are useful. Missing uncertainty distinction and reproducibility metadata; loss-ordering conclusion is wrong. |
| Readability | 6 | 7 | Conversational, short paragraphs suit engineers. Some overloaded claims need precision. Automated Flesch estimate is unreliable for MDX/code; no penalty for accessible technical prose. |
| Originality | 3 | 5 | Concrete model names, counts, and failure case, but original run logs/code revision are not supplied. |
| Sentence/paragraph structure | 3 | 4 | Coherent flow, yet three similarly framed “lie” sections and a repetitive ending obscure the actual checks. |
| Engagement | 3 | 4 | Code, result examples, two figures. A compact decision/checklist would be more useful than repeated rhetoric. |
| Grammar/clarity | 2 | 3 | Clean grammar; title/intro say two lies, body says three; percentages and percentage points need sharper labels. |

### SEO optimization: 14/25

| Check | Score | Max | Reason |
|---|---:|---:|---|
| Headings/navigation | 3 | 5 | Shared ToC and clean H2 hierarchy; headings are long rhetorical claims, final “The rule” is vague. |
| Title clarity | 2 | 4 | Memorable but does not name ASR or benchmark sampling; categorical “lying” framing is not supported. |
| Semantic consistency | 4 | 4 | One recognizable reader task: interpreting a speech benchmark smoke run. |
| Internal links | 0 | 4 | No contextual article-body links. Global navigation/footer do not substitute. |
| URL | 3 | 3 | Stable, lowercase, readable slug. Preserve it. |
| Meta description | 2 | 3 | Specific topic, but repeats “two false results” and does not accurately describe all three sections. |
| External links | 0 | 2 | No primary-source links. |

### E-E-A-T signals: 8/15

| Check | Score | Max | Reason |
|---|---:|---:|---|
| Author attribution | 4 | 4 | Real name, GitHub link, shared substantive bio. |
| Source fidelity | 0 | 4 | No cited material support; nested-mask-to-monotonic-WER inference is false. |
| Trust indicators | 3 | 4 | About/contact and author ownership in shared site; no demonstrated editorial-method transparency for these results. |
| Evidence basis | 1 | 3 | Detailed report of an incident, but run artifacts, seed, models/ASR versions, scorer revision and code are not traceable. Do not classify the supplied results as fabricated; classify their provenance as unverified. |

### Technical elements: 8/15 (fixed denominator)

| Check | Score | Max | Reason |
|---|---:|---:|---|
| Schema | 4 | 4 | Shared SEO implementation supplies BlogPosting, Person, Organization and BreadcrumbList. Source-inspected; rich-results validator not run. |
| Image optimization | 2 | 3 | SVG figures have accessible names; founder WebP is appropriately lazy/decorative. No article-specific thumbnail or social cover. |
| Structured content | 0 | 2 | Numerical comparisons are fenced plaintext instead of semantic tables. |
| Page speed | 0 unverified | 2 | No current-post measured LCP or production performance evidence. Points withheld rather than a proven failure. |
| Mobile friendliness | 0 unverified | 2 | No current-post rendered/mobile evidence. Source suggests figure labels will be tiny; not treated as a verified screenshot finding. Points withheld rather than a proven failure. |
| Social metadata | 2 | 2 | Shared code supplies OG/Twitter tags and fallback social image. |

A subsequent request to the local post returned HTTP 200 with article copy in the initial HTML, five schema graph entries (WebSite, Organization/ProfessionalService, Person, BlogPosting, BreadcrumbList), all OG/Twitter metadata, and zero semantic tables. Per the task-specific comparison convention, this report keeps a fixed 100-point denominator and withholds unverified performance/mobile points. This is an explicit adaptation from the skill’s default N/A reweighting, not evidence that those checks failed.

### AI citation readiness: 8/15

| Check | Score | Max | Reason |
|---|---:|---:|---|
| Evidence-backed citability | 1 | 4 | Arithmetic is inspectable, but key generalizations are unsupported or incorrect. |
| Purpose fit | 2 | 3 | Useful benchmark-audit purpose; hard for skimmers to identify actual corrective actions. |
| Entity clarity | 2 | 3 | G.711, Piper, ZipVoice, Whisper and WER appear, but exact roles/versions and WER denominator need explicit treatment. |
| Extraction structure | 1 | 3 | Examples exist; fenced tables have no headers/thead, and findings are buried in narrative. |
| Crawler accessibility | 2 | 2 | HTTP 200 contains the primary content and schema; robots allows posts. Local HTTP inspected, no claim about remote search indexing. |

## Blocking findings

1. **P0 — Incorrect diagnostic rule, MDX lines 57–61 and 110.** A superset of dropped frames does not force an ASR decoder to make a superset of word errors. WER need not rise monotonically on individual or small samples. Remove the claim that the observed reversal is physically impossible. Separate assertions about the loss mask/audio from inferences about recognizer output.
2. **P1 — Identical WER is not proof of a bug, line 26.** Rounded equality is an investigation trigger. The demonstrated bug is category coverage, not the possibility of equal scores.
3. **P1 — Resolution is not uncertainty, lines 70 and 100.** `100 / N_ref` is one pooled word error's percentage-point increment for fixed N. It is not a confidence interval, statistical significance threshold, or proof that 300 utterances can resolve an effect. Keep counts and denominator, explicitly separate uncertainty.
4. **P1 — Numeric provenance is missing.** Preserve existing observations with a clear provenance/limitations note; do not imply independently reproduced results. Link actual repository/artifacts if verified. Add sources for WER computation and Python import/cache behavior.
5. **P1 — Misleading resolution graphic.** `BenchmarkResolution.astro` uses 0.06 pp tick spacing for the ~2,900-word row while calling it one error = 0.03 pp. Its 0.5 pp “effect you are measuring” is an invented visual target with no basis in the reported run. Replace with exact counts and calculated increments.
6. **P2 — Figure text and phrasing.** Native SVG text runs at 9–12 units over ~700-wide canvases, likely becoming much smaller on a phone. “First N … is not sampling” is rhetorically overstated: it is unrepresentative subset selection. “The benchmark, scaled down” overpromises equal category coverage as representativeness.
7. **P2 — Experimental conditions and retention.** Band-limiting can change a decoder's result, but the particular mechanism involving TTS high-frequency artifacts is unproven here. “Audio will not change” and rescoring “for nothing” are too broad. Preserve raw output plus scorer, dataset, model, audio and run revisions so scoring changes are reproducible.

## Editorial pattern review (advisory, not authorship inference)

First-order automated diagnostics from `analyze_blog.py`: no configured trigger phrases; 60 sentence units, mean 14.3 words, standard deviation 6.5, variation coefficient 0.45; TTR 0.485. The parser reports 830 body words and 29 paragraphs, omits text inside imported figures and has no textstat/BeautifulSoup installed. These are extraction-dependent descriptive readings, not exact rendered-page prose statistics. Its automatic 40/100 is not adopted: it misses shared schema/byline/social metadata and actual component visuals.

Second-order review: repeated “first lie / second lie / third lie” framing makes the article sound more certain than its evidence. The conclusion repeats the opening premise and reinstates an incorrect rule. The most useful material is the concrete 114-word denominator, category coverage mistake, and transcript-rescoring workflow. Preserve those. No rhetorical-question or keyword-padding problem was found. Style observations do not alter the score independently of reader clarity and accuracy.

## Acceptance targets for revision

- Correct the loss-mask/WER distinction; acknowledge original reported results were not re-run.
- Use short technical section names and an opening that states the engineering task.
- Show semantic result tables, error counts, WER formula, and exact denominator increments.
- Explain sample coverage and reproducibility using relevant, readable visuals; include the site-blending thumbnail.
- Retain/transparently explain evidence, add primary references and relevant internal reading paths.
- Verify actual desktop/mobile/light/dark rendering, images, controls and SSR; do not claim measured production performance from a local screenshot.

No review nonce was supplied for this baseline, so this document is not a nonce-bound final publication approval.

BLOCKING: true (59/100; incorrect monotonic-WER rule and unsupported inference must be corrected before integration)
