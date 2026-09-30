# Baseline review: The normaliser that scored itself

Reviewed 2026-09-30 using the same claude-blog five-category rubric as the first two posts. Source: `src/content/blog/the-normaliser-that-scored-itself.mdx`, both imported normaliser figures, and the shared layout/SEO. Fixed100 denominator; unverified speed/mobile points remain withheld rather than counted as proven failures.

### Overall Score: 57/100 - Rewrite

| Category | Score | Max | Assessment |
|---|---:|---:|---|
| Content quality | 21 | 30 | Useful concrete scoring failure; missing policy boundaries and overbroad claims undermine the fix. |
| SEO optimization | 13 | 25 | Stable URL and topical unity; vague rhetorical headings and no contextual source/internal links. |
| E-E-A-T signals | 8 | 15 | Accountable author, but normalizer version, source and reproductions are not provided. |
| Technical elements | 8 | 15 | Shared schema/social support and SVG accessible names; no semantic comparison tables or article thumbnail. |
| AI citation readiness | 7 | 15 | Recognizable example, but key conclusions should not be reused without version and scope. |
| **Total** | **57** | **100** | **Policy and evidence rewrite required.** |

## Explicit subpoints

| Category | Subpoints |
|---|---|
| Content21/30 | Coverage4/7; readability6/7; originality3/5; structure3/4; engagement3/4; grammar/clarity2/3. |
| SEO13/25 | Headings3/5; title2/4; semantic consistency3/4; internal links0/4; URL3/3; description2/3; external links0/2. |
| E-E-A-T8/15 | Author4/4; source fidelity0/4; trust3/4; evidence basis1/3. |
| Technical8/15 | Schema4/4; image optimization2/3; structured elements0/2; speed0/2 unverified; mobile0/2 unverified; social tags2/2. |
| Citation7/15 | Evidence-backed citability1/4; purpose2/3; entity clarity1/3; extraction1/3; crawler access2/2. |

This score is an editorial heuristic, not an AI-authorship judgment or ranking prediction. No points are deducted merely for being short, lacking a FAQ, or missing an arbitrary image/statistic quota.

## Material findings

1. **P0 — False comparability promise in `NormaliserConvergence.astro`.** The caption says the custom transformation is a no-op for digit-free prose and therefore remains comparable with published numbers. Stripping brackets changes annotation handling even when no digits are present; remapping spelled digit words also changes tokenization. A custom scoring policy changes the metric. State the policy and version it, and do not compare WER numbers produced by different pipelines as if they were interchangeable.
2. **P1 — Universal claims exceed the example.** Lines14 and100 claim everyone uses Whisper normalization and anyone scoring transactional speech has wrong scores. The example demonstrates one mismatch under a particular policy, not every benchmark. Identify the actual implementation/package/version and scope the conclusion to tested inputs.
3. **P1 — Text fixture is conflated with audio proof.** The opener and `NormaliserFailure` caption assert perfect audio and perfect recognition without linked audio/listening evidence. A supplied equivalent-text fixture suffices to show a normalizer failure. Present it as that unless verifiable listening evidence is available.
4. **P1 — The “fix” changes annotation semantics, lines69–90.** Removing bracket delimiters preserves their contents; it will also preserve annotations such as `(inaudible)`. A number-aware or field-specific policy needs to distinguish protected digits from actual annotations. Blindly retaining all bracketed text is not universally correct.
5. **P1 — Snippet cannot stand alone.** The displayed `normalize` function relies on `_BRACKET`, `_DIGIT_RUN`, `_NON_WORD`, `_DIGIT_WORDS`, `_MERIDIEM` and `_normalizer` without their definitions or a link. Provide the pinned source or a complete downloadable fixture. Regression tests should include negative controls so distinct numbers do not become equal.
6. **P1 — Metric definition and failure granularity need clarification.** Show `WER=(S+D+I)/N` and why it can exceed100%. If the reproduced alignment is one substitution plus two insertions over one reference token, say so. For a phone-number field, digit error rate and exact entity match can answer different operational questions from corpus WER. Do not silently rename a customized digit-token score as standard published WER.
7. **P2 — Category and leading-zero statistics lack provenance.** Independent corpus inspection confirms60/300 digit-category entries=20%, and86/300 references contain literal`0`=28.67%, rounded29%. The article should state that exact definition; “contain a zero” is not the same as “contain a leading zero” or “suffer normalization damage.” Digits being the universally hardest narrowband category is unsupported.
8. **P2 — Old phone-model assertion is stale.** Line14 calls the offline model a “real G.711 phone line.” The previous article's correction establishes TorchAudio quantization is an approximation; align this opener with that scope.
9. **P2 — Heading rhetoric and diagram copy hide the actual decisions.** “The first layer,” “The actual fix” and “The part that should worry you” make poor scan targets. The proposed Token Alignment, Leading Zeros, Bracket Removal, Scoring Policy and Regression Tests headings better expose the engineering structure.

## Technical/evidence status

The existing local route returnedHTTP200 with primary content in initial HTML, five schema graph entries (WebSite, Organization/ProfessionalService, Person, BlogPosting, BreadcrumbList),17OG/Twitter tags and zero semantic tables. Shared author/GitHub/bio/about/contact signals remain valid.

The two SVGs have accessible descriptions but use10–15-unit labels across640-wide drawings; responsive legibility has not been checked on this original post. The YouTube embed is lazy and uses a nocookie domain, but this review has not watched it or verified the underlying demonstration. It is not treated as blanket support for package behavior.

The exact normalizer transformations, zero loss and bracket handling are being reproduced by the evidence agent. Until fixtures are available, this review does not certify that every literal string shown matches every OpenAI/third-party normalizer version. The historical example is not labeled fabricated; it is insufficiently specified.

## Editorial diagnostics

Automated extraction:524words,19paragraphs,38sentence units, mean14.6words, SD8.4, coefficient0.58, TTR0.571, no configured trigger phrases. These readings exclude imported diagrams and can misinterpret MDX; they do not infer authorship.

Second-order: repeated “first/second/third layer” escalation and a dramatic warning ending make a narrow, useful finding sound universal. The final paragraph tells the reader they are wrong before establishing their scoring policy. Replace that certainty with a reproducible test and visible policy boundary. Keep the concrete input/output example and chronological discovery only where it aids understanding.

## Acceptance targets

Pin the normalizer and scoring implementation. Reproduce phone formats, leading zeros, bracketed digits, actual annotations, ordinals, amounts/times and deliberately incorrect digits. Make the scoring contract explicit: equivalent accepted forms converge, meaningful differences remain differences. Show a semantic input/output/alignment comparison and a readable architecture of normalization before scoring. Add site-blending thumbnail and downloadable verification where it earns its place. Preserve the original URL, supply useful primary/internal sources, and inspect final responsive/theme behavior.

BLOCKING: true (57/100; false comparability claim, unscoped scoring policy and missing reproducible fixtures)
