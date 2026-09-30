# Staged review: The normaliser that scored itself

Reviewed 2026-09-30. Draft: `artifacts/blog-review/series/normaliser/draft.mdx`, including completed token-alignment/policy visuals, watercolor cover, portable fixture and recorded output. Manual claude-blog five-category review; no generic preflight certificate is claimed.

### Overall Score: 93/100 - Exceptional

| Category | Score | Max | Assessment |
|---|---:|---:|---|
| Content quality | 29 | 30 | Concrete reproducible failure, correction boundaries and positive/negative controls. |
| SEO optimization | 24 | 25 | Five short technical sections and useful source/internal links; title remains less explicit than the description. |
| E-E-A-T signals | 14 | 15 | Pinned policy/dependencies and reviewable outputs; shared editorial-policy transparency remains limited. |
| Technical elements | 11 | 15 | Optimized images, accessible visuals, semantic tables and shared metadata; mobile/speed points withheld. |
| AI citation readiness | 15 | 15 | Self-contained explanations with exact alignments, versioned evidence and explicit scope. |
| **Total** | **93** | **100** | **Cleared for local integration.** |

This is the same fixed100 denominator as the baseline. Runtime deductions mean unverified, not failed. The score is an editorial heuristic rather than an AI-authorship verdict, ranking prediction or universal metric-validity claim.

## Explicit subpoints

| Category | Subpoint accounting |
|---|---|
| Content29/30 | Coverage7/7; readability7/7; originality5/5; structure3/4; engagement4/4; grammar/clarity3/3. |
| SEO24/25 | Headings5/5; title3/4; semantic consistency4/4; internal links4/4; URL3/3; description3/3; external links2/2. |
| E-E-A-T14/15 | Author4/4; source fidelity4/4; trust3/4; evidence basis3/3. |
| Technical11/15 | Schema4/4; images3/3; structured content2/2; speed0/2 unverified; mobile0/2 unverified; social2/2. |
| Citation15/15 | Evidence-backed citability4/4; purpose3/3; entity clarity3/3; extraction3/3; crawler access2/2. |

The minor structure deduction reflects the Scoring Policy section combining regex mechanics and several field-policy distinctions; it remains clear enough and does not need expansion. The title's metaphor does not tell a new reader this is about phone-number evaluation, while the description and opening do. These are polish deductions, not blockers or reasons to add filler. Reproducible examples and negative controls earn evidence credit; a first-person story alone would not.

## Factual clearance

- The opener is explicitly a text fixture, not proof of perfect audio or recognition. The older “realG.711 phone line” framing is gone.
- `whisper-normalizer0.1.15` and `jiwer4.0.0` are pinned and named. The example is not generalized to every Whisper release.
- The recorded original failure has one substitution, zero deletions and two insertions against one reference token, yielding300%WER. The article explains why insertions allow WER above100%.
- The four tested forms converge to ten digit tokens under the specified wrapper. The article does not claim all conceivable number formats converge.
- `0198`, `007` and `0500` outputs match the supplied fixture. Pre-splitting cannot recover a zero already removed; the need to protect it earlier is clear.
- Bracket content preservation is accurately described as a policy change. The article acknowledges that actual annotations can be retained and need separate handling.
- The regex is shown with its real ordinal alternative and a runnable assertion. One tiny wording refinement was sent to root: “complete lowercase numeric ordinal” accurately scopes suffix handling, since the provided fixture intentionally shows uppercase`31ST`failing.
- The currency collision is concrete and reproduced: `€12` and`12` both become`1 2`. The article treats this as a limitation of the benchmark policy, not desired semantics.
- Whole-identifier exact match is now defined after the agreed field normalization. A wrong digit remains wrong even when the digit-token error rate is10%.
- The false claim that digit-free prose is unchanged and remains comparable with publishedWER is removed from the prose and replacement component. Comparisons must be rescored under the same policy.

The proposed lowercase-word refinement does not alter the tested examples or the overall policy boundary. No material factual blocker remains.

## Evidence reviewed

- Portable `verify-normaliser.py` pins dependencies in inline metadata, includes a run command, identifies the benchmark commit, and uses no machine-specific path.
- Its output verifies the original300%case, four equivalent phone forms, a wrong-digit negative control, `007`versus`7`, and `first`versus`1st`.
- Boundary fixtures explicitly expose currency, sign, decimal-position, annotation, alphanumeric-grouping and uppercase-ordinal failures. They are not accidentally reported as successful semantics.
- The optional corpus audit checks the frozen SHA-256 before computing statistics. Removing20%/29%from the article keeps the focus on demonstrated failures without confusing “contains a zero” with “contains a damaged leading zero.”
- I inspected the fixture code/output; the evidence agent/root ran the package-level reproduction. I did not evaluate any audio or run ASR.
- JiWER usage/alignment documentation, the pinned OpenAI normalizer source and the pinned project tests were opened through the web tool. The four external citations returnedHTTP200 according to the saved link check.

## Visual/technical source check

- `NormaliserFailure.astro` uses semantic input labels and a three-column alignment, explicitly identifies gap markers as alignment placeholders, and says this fixture does not measure recording quality.
- `NormaliserConvergence.astro` now uses responsive Reladraw diagrams with native icons, scoped four-form labels, accessible descriptions, theme mappings and shared zoom. The old no-op/comparability caption is absent.
- Cover inspected: the007versus7strips are legible and match the article's example; lavender/charcoal watercolor and transparent edges fit the established direction.
- Hero:1,600×800transparentWebP,369,628bytes. Social:1,200×630opaqueJPEG (final social derivative corrected during asset verification). Correct alt, responsive widths, eager loading and fetchpriority are specified.
- Five technicalH2s, two semantic body tables, contextual internal links and old heading aliases are present. Shared source provides ToC, author/GitHub/bio, social tags and structured data.
- InitialHTML/robots/schema were verified on the original route. Final rewritten initialHTML, downloads and rendered controls still require integration verification.

## Remaining checks

1. Verify the final rewritten route and both download URLs after integration, including expected JSON/source contents.
2. Inspect desktop/mobile/light/dark. In particular, ten-digit token text must fit its first alignment cell on small screens, and narrow policy-diagram labels must remain readable.
3. Exercise zoom open/close and keyboard behavior, inspect console, and complete direct Astro validation.
4. Add mobile points only after actual responsive evidence. Keep page-speed points withheld unless measured appropriately.

## Advisory editorial diagnostics

Latest parser extraction:828words,24paragraphs,51sentence units, mean14.3words, SD6.8, coefficient0.48, TTR0.579, no configured trigger phrases. MDX/component extraction limitations apply; these values do not infer authorship or independently affect scoring.

Second-order review: technical headings replace serial “layers” and a fear-based ending. The article shows an actual failure before the mechanism, then separates the useful fix from its limits. The final regression table tests both what should become equal and what must remain different. No padded FAQ, extra anecdote, or repetitive summary is needed.

No P0 factual/editorial issues remain in the staged prose and completed component source.

BLOCKING: false (93/100, no P0; cleared for local integration and pending rendered-page checks, not production publication)
