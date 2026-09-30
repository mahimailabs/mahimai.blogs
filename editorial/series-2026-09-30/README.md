# Three blog rewrites — 30 September 2026

Completed sequentially: each outline, evidence review, draft, visual work and independent content score preceded work on the next article. Local only; no commit or deployment.

| Article | Before | Final | Principal correction |
| --- | ---: | ---: | --- |
| Your smoke run is lying to you | 59 | 93 | Loss masks are not nested; WER is not guaranteed to rise monotonically; resolution is not uncertainty. |
| Building a phone line in PyTorch | 54 | 96 | TorchAudio mu-law is not wire-compatible G.711; real digital filter response and properly scoped surrogate gradients. |
| The normaliser that scored itself | 57 | 95 | Reproduced 300% text fixture; explicit phone-number policy and semantic counterexamples to the proposed fix. |

Scores use AgriciDaniel/claude-blog revision `2500d4c` and its five-category, 100-point rubric. They are manual editorial assessments, not authorship or search-performance claims. All final scores include two responsive-design points after browser inspection; all withhold two page-speed points because production LCP was not measured. Detailed reviews are in `*-before.md` and `*-after-draft.md`; `normaliser-final.md` includes its final runtime evidence.

## Work delivered

- Three rewritten MDX articles with 2–3-word technical headings, contextual primary sources, old anchor aliases and an updated date of 2026-09-30.
- Three transparent watercolor WebP heroes and three 1200 × 630 social JPEGs, produced with built-in image generation. Prompts are in each article’s `image-prompt.md`; the tool does not expose its model identifier.
- Three Reladraw diagrams using native icons, narrow and wide views, and a shared zoom library.
- Responsive sampling comparison, exact WER resolution graphic, measured digital filter response chart, and token alignment figure.
- Downloadable Python validation fixtures and recorded outputs for the phone-line and normaliser posts, executed with pinned dependencies.
- All 22 article assets and three MDX files are byte-identical in the canonical mahimai.blogs repository and local website copy.

## Verification

- Direct `pnpm exec astro build` passed; the default build with remote content sync was not used.
- `pnpm exec astro check`: 294 files, zero errors, zero warnings, 13 pre-existing hints.
- Scoped ESLint passed for DiagramZoom.
- All three routes viewed at 1280px desktop and 390px mobile, with light and dark theme checks, zero horizontal overflow and no browser console errors. Zoom opened and closed. First-click hydration was fixed on the transcript diagram.
- All 17 editorial external links returned HTTP 200. Downloadable source and JSON assets served correctly. Generated Astro HTML contains valid JSON-LD and correct 1200 × 630 social metadata.
- The Python phone fixture reproduced the recorded output exactly. The normaliser fixture verifies 300% WER, positive formatting cases, a 10% wrong-digit case and eight semantic negative controls.

## Remaining evidence limits

Original smoke-run manifests were not available; historical numbers are labelled and not presented as new model results. Carrier compliance, live audio quality and production page performance were not claimed. The underlying benchmark repositories were read, not modified.

## Local links

- [Your smoke run is lying to you](http://127.0.0.1:4321/blog/your-smoke-run-is-lying-to-you)
- [Building a phone line in PyTorch](http://127.0.0.1:4321/blog/building-a-phone-line-in-pytorch)
- [The normaliser that scored itself](http://127.0.0.1:4321/blog/the-normaliser-that-scored-itself)
