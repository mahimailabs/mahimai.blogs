# Evidence review: The normaliser that scored itself

Reviewed 2026-09-30. Benchmark source unchanged. Reproduced the frozen benchmark dependency versions `whisper-normalizer==0.1.15` and `jiwer==4.0.0` in isolated uv environments.

- Portable script: `normaliser-validation.py` (PEP 723 dependency pins; no absolute paths).
- Output: `normaliser-validation.json`.
- Run `uv run normaliser-validation.py`; optionally pass `--corpus dialtone_v1.jsonl` for the corpus counts. The optional corpus SHA-256 is checked before counting.
- The script's copied policy agrees with the benchmark's actual `normalize()` on all 300 frozen references. It reproduces the policy's known limitations intentionally.

## Central finding

The 300% fixture is real, but it demonstrates a **normalisation-policy mismatch**, not a speech-recognition failure or a universal bug in Whisper. The benchmark used the standalone `whisper-normalizer` package. OpenAI's original paper explicitly describes its text standardisation as best effort and potentially imperfect; removal of parenthesised annotations is intentional. Applying those rules to a phone-number field gives the wrong equivalence relation for that task.

Do not preserve “everyone uses Whisper”, “digits are the hardest case”, “every transactional score is wrong”, or “three bugs and the fix” as universal claims. The code/fixtures support none of those generalisations. Describe the specific test case and the scoring contract.

## Exact reproduced results

Reference: `six one three five five five zero one nine eight`.

| Input | Stock normaliser output | Benchmark digit-policy output |
| --- | --- | --- |
| spoken reference | `6135550198` | `6 1 3 5 5 5 0 1 9 8` |
| `613 555 0198` | `613 555 198` | `6 1 3 5 5 5 0 1 9 8` |
| `(613) 555-0198` | `555 198` | `6 1 3 5 5 5 0 1 9 8` |
| `6135550198` | `6135550198` | `6 1 3 5 5 5 0 1 9 8` |

The spoken-versus-grouped stock comparison yields **1 substitution + 2 insertions + 0 deletions, over 1 reference token = 300% WER**. WER can exceed 100% because insertions add errors without adding reference tokens. This is not evidence that an audio recogniser made three acoustic mistakes.

With the benchmark policy, these four spellings yield **0 edits / 10 reference tokens**. Changing the last digit to `613 555 0199` yields **1 substitution / 10 = 10%**, and the whole-identifier exact-match result is **false**. Token error rate and whole-entity correctness answer different questions.

Leading-zero examples:

| Input | Stock | Benchmark policy |
| --- | --- | --- |
| `0198` | `198` | `0 1 9 8` |
| `007` | `7` | `0 0 7` |
| `0500` | `500` | `0 5 0 0` |

`zero zero seven` becomes `007` in the stock number parser, while literal `007` becomes `7`; input form affects interpretation. Do not claim spelled-out zero is always kept in every context.

## The regex does split single digits

The omitted definition in the original excerpt is essential:

```python
DIGIT_RUN = re.compile(r"\d+(?:st|nd|rd|th)\b|\d")
```

The first alternative matches a whole numeric ordinal; the second matches **one digit**, not a run. `findall('613')` returns `['6', '1', '3']`; `findall('31st')` returns `['31st']`. Surrounding each match with spaces therefore does atomise ordinary digit runs. Using `\d+` for both alternatives would not.

The implemented sequence is: strip bracket characters; pre-split digits; run the English normaliser; strip non-word punctuation; post-split digits; map single-digit words back to numerals; join the special meridiem spelling. Include definitions if showing the full function, or show a deliberately smaller phone-field policy. Do not imply bracket stripping is safe on arbitrary prose.

## Boundary controls: the fix is not universal

The portable script deliberately demonstrates these failures rather than hiding them:

| Semantically meaningful difference | Policy result |
| --- | --- |
| `$5` versus `5` | Both become `5` |
| `$12` versus `€12` | Both become `1 2` |
| `-12` versus `12` | Both become `1 2`; stock already removes the written sign |
| `$1.25` versus `$12.5` | Both become `1 2 5` |
| annotation `(inaudible)` versus spoken word `inaudible` | Both become `inaudible` |

These are false equivalences when the indicated semantics matter. A zero score can be wrong too. Typed values such as monetary amounts need currency, sign and decimal position preserved; annotation handling must respect the dataset convention.

Two false differences also survive:

- `AB007` becomes `ab 0 0 7`; `A B zero zero seven` becomes `a b 0 0 7`.
- `31st` stays `31st`; uppercase `31ST` becomes `3 1 saint`, because pre-splitting occurs before lowercasing and the ordinal regex is case-sensitive.

Some current test cases do pass: `first` and `1st` both become `1st`; `2:15 pm` and `two fifteen p m` both become `2 1 5 pm`; the written and spoken `$1,247.50` examples converge. These successes do not validate all ordinals, times, IDs or amounts.

Recommended framing: use the digit policy only where the field's identity is the digit sequence, define accepted formatting explicitly, keep ordinary transcript WER separately, and test both equivalent variants and real semantic differences. Preserve original references and hypotheses to allow rescoring. Avoid calling the changed tokenisation directly comparable with published WER under a different policy.

## Corpus percentages

The frozen corpus has **60 digit-category utterances / 300 = 20% of utterances**. This is not necessarily 20% of WER weight because utterances have different token counts.

**86 / 300 = 28.6667%** contain a literal `0` anywhere in the original reference text. The old “29% contain a zero” rounds correctly. It does **not** mean 29% have leading zeros, 29% lose zeros, or 29% are mis-scored. None of the reference texts contains the word `zero`; the count is a textual corpus property. All 300 references are idempotent under the current policy, which still does not prove semantic correctness.

## Sources

- [Frozen benchmark scoring implementation](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/metrics/wer.py)
- [Benchmark tests, including phone variants](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/tests/test_wer.py)
- [Frozen dependency lock](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/uv.lock)
- [Frozen corpus](https://github.com/mahimailabs/handset-bench/blob/651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a/src/handset_bench/textset/dialtone_v1.jsonl)
- [OpenAI Whisper normaliser source](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/whisper/normalizers/english.py)
- [OpenAI Whisper paper, Appendix C, PDF page 21](https://cdn.openai.com/papers/whisper.pdf#page=21)
- [JiWER alignment and metric usage](https://jitsi.github.io/jiwer/usage/)

No new ASR or TTS runs were performed. The validation covers text transforms, edit counts, and frozen-corpus counts—not whether historical audio sounded correct.
