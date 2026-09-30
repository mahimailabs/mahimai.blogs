# Evidence review: Your smoke run is lying to you

Reviewed 2026-09-30. Read-only investigation; no article or benchmark changes.

## Source identity

- Local benchmark: `/Users/mahimai/code/year-2026/AUG/handset-bench`, clean commit `651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a`.
- Original project: `/Users/mahimai/code/year-2026/AUG/DialTone-TTS`, commit `28a1536da3f5749c904ec549616706a999856de9`.
- Retained result JSON is present locally under DialTone-TTS `results/`, but ignored/untracked by Git. Public findings summarize the full runs; do not invent public raw-result URLs.

## Corrections required

1. **Remove the monotonic-WER guarantee.** More erased audio does not mathematically require a recognizer to make more word errors. WER is edit distance on the recognizer's output, not a physical measure of corruption. Even nested masks would not establish that guarantee. The original benchmark README repeats the mistake; its assertion is not independent evidence.
2. **The actual loss masks are not nested.** `condition_seed()` hashes the utterance ID, condition name and run seed. `loss_1pct` and `loss_3pct` therefore get different random draws. This was already true in DialTone's initial commit `62460ef`, not a later change. Same seed plus same frame count would produce nested Bernoulli masks, but this harness does not use the same seed across those conditions. Nominal loss rates are probabilities, not exact per-clip percentages.
3. **Identical rounded scores are a diagnostic clue, not proof of a bug.** Different waveforms can produce identical transcripts or equal error counts. Sampling was genuinely incomplete, but that does not make the observed numeric result false.
4. **Resolution is not uncertainty.** `100 / N` is the change in percentage points from one additional edit with a fixed normalized reference denominator. It is not a confidence interval, statistical significance threshold, or proof that 300 utterances represent deployment traffic.
5. **Do not claim the small table proves there was no bug or proves random noise.** It shows that very few edits drove the ranking. Separate waveform repeatability, ASR repeatability, corpus sampling and scoring checks before attributing variation.
6. **Qualify Python import behavior.** Editing an already imported module does not automatically replace its objects in a normal running Python process. Explicit reload mechanisms exist and have caveats. Recommend a fresh process with a pinned revision, not an absolute statement that every Python edit is ignored.
7. **Remove unsupported cost specifics or label them historical estimates.** The original article says about one dollar versus five; the retained project README currently advertises an estimated ~$0.45 smoke run. Neither establishes actual invoices. The dollar figures add little to the technical argument.
8. **Qualify the clean-over-wideband mechanism.** It is observed that clean can score lower WER. High-frequency TTS artifacts being removed is a plausible explanation, not a mechanism established by these tables alone. Filtering, ASR response and corpus effects need isolation.

## Facts checked from code and records

### Sample coverage

The frozen corpus has 300 utterances: digits 60; proper nouns 50; addresses 40; dates/times/money 40; conversational 70; general 40. The first 60 records are digits. `[:12]` therefore returns 12 digit utterances.

`loader.sample(loader.load(), 12)` takes two from each category using deterministic round-robin selection. It is a coverage-oriented subset, not a proportional random sample. IDs: `dt-0001`, `dt-0002`, `dt-0061`, `dt-0062`, `dt-0111`, `dt-0112`, `dt-0151`, `dt-0152`, `dt-0191`, `dt-0192`, `dt-0261`, `dt-0262`.

### Arithmetic

Retained full-run records contain 2,904 normalized reference tokens. Restricting those records to the 12 selected IDs gives 114 normalized reference tokens, consistent across all eight Piper/ZipVoice condition records.

| Reference tokens | One additional edit |
| --- | --- |
| 114 | 0.8771929825 percentage points |
| 2,904 | 0.0344352617 percentage points |

Thus the historical table's 0, 1, 2 and 4 edits correctly yield 0.00%, 0.88%, 1.75% and 3.51%. These are normalized tokens: digit atomisation can change the denominator relative to whitespace in the original prose.

**Historical table limitation:** the 7.09% table and 12-row smoke error counts were not found in retained raw records or committed findings. They may be preserved as the author's historical debugging account, explicitly not a current model comparison. Current deterministic full-run subsets do not reproduce those old smoke counts: Piper has zero errors in all four selected subsets; ZipVoice has one in each.

The full deterministic ZipVoice records contain 126 errors at 1% loss and 125 at 3% loss, both over 2,904 reference tokens. The public findings report the same reversal (4.34% versus 4.30%). This directly contradicts the old universal claim about loss ordering in the same project.

### Stored transcripts / CLI

`scoring.build_quality_record()` stores `reference`, `hypothesis`, status, errors and normalized reference count per utterance. It also stores the corpus hash, ASR revision, system version, run ID and Git description. This is the path used by the Modal matrix. Caveat: the separate generic `runner.run_quality()` currently does not store the same transcript fields, so avoid saying every library path supports rescoring.

The command is real:

```bash
handset-bench rescore --results results
handset-bench rescore --results results --write
```

The first is a dry run; the second overwrites scores in existing result JSON. The implementation requires stored transcripts and rejects older records without them. It recomputes per-utterance scores and corpus WER without calling synthesis or transcription. It does not regenerate the Markdown scorecard, and does not update the record's scoring-version metadata. Recommend archiving original records before an intentional rewrite.

### Repeatability

The project's later investigation found that repeat transcription of fixed clips was stable in its tested environments, while repeat synthesis initially changed waveforms. Deterministic synthesis fixed measured drift. This is useful evidence for checking each stage; it does not prove all Whisper runs on all devices are deterministic or that repeatable results have zero sampling uncertainty.

## Primary links suitable for the article

- [Sampling implementation](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/textset/loader.py#L84-L109)
- [Frozen corpus](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/textset/dialtone_v1.jsonl)
- [Loss seeding and masking](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/codec.py#L107-L133)
- [WER implementation](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/metrics/wer.py)
- [Transcript-bearing records](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/scoring.py)
- [Offline rescoring implementation](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/rescore.py)
- [Recorded findings and repeatability investigation](https://github.com/mahimairaja/DialTone-TTS/blob/28a1536da3f5749c904ec549616706a999856de9/docs/baseline-findings.md)
- [Python reload semantics](https://docs.python.org/3/library/importlib.html#importlib.reload)
- [JiWER metric definition](https://jitsi.github.io/jiwer/)

Use the code/records for narrow claims. The original README and findings contain stale or overstated prose, including contradictory listening-gate status and overbroad intelligibility conclusions; do not copy them wholesale.
