# /// script
# requires-python = ">=3.10"
# dependencies = ["whisper-normalizer==0.1.15", "jiwer==4.0.0"]
# ///
"""Reproduce a text-scoring fixture and expose the benchmark policy's boundaries.

Run: uv run verify-normaliser.py
Optional corpus audit: uv run verify-normaliser.py --corpus dialtone_v1.jsonl

No audio is generated or evaluated. This reproduces the benchmark's normalization
policy, including its limitations; it is not a general-purpose entity parser.
The optional corpus must match the published frozen corpus SHA-256.

Policy source (MIT): mahimailabs/handset-bench, commit
651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a, src/handset_bench/metrics/wer.py.
"""
import argparse
import collections
import hashlib
import importlib.metadata
import json
import re
from pathlib import Path

import jiwer
from whisper_normalizer.english import EnglishTextNormalizer

STOCK = EnglishTextNormalizer()
DIGIT_RUN = re.compile(r"\d+(?:st|nd|rd|th)\b|\d")
BRACKET = re.compile(r"[()\[\]{}]")
NON_WORD = re.compile(r"[^\w\s]")
MERIDIEM = re.compile(r"\b[ap] m\b")
DIGIT_WORDS = dict(zip(
    "zero oh one two three four five six seven eight nine".split(),
    "0 0 1 2 3 4 5 6 7 8 9".split(),
))
CORPUS_HASH = "851cb1b30397921da76aa3bfae4ec97994cbb4f5a32fe3616f9502c847b73306"


def benchmark_policy(text):
    presplit = BRACKET.sub(" ", text)
    presplit = DIGIT_RUN.sub(lambda m: f" {m.group()} ", presplit)
    normalised = STOCK(presplit)
    stripped = NON_WORD.sub(" ", normalised)
    atomised = DIGIT_RUN.sub(lambda m: f" {m.group()} ", stripped)
    tokens = [DIGIT_WORDS.get(token, token) for token in atomised.split()]
    return MERIDIEM.sub(lambda m: m.group().replace(" ", ""), " ".join(tokens))


def score(reference, hypothesis, normalizer):
    ref = normalizer(reference)
    hyp = normalizer(hypothesis)
    result = jiwer.process_words(ref, hyp)
    return {
        "reference": ref,
        "hypothesis": hyp,
        "reference_tokens": len(ref.split()),
        "substitutions": result.substitutions,
        "deletions": result.deletions,
        "insertions": result.insertions,
        "wer_percent": result.wer * 100,
        "exact_match": ref == hyp,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path)
    args = parser.parse_args()
    spoken = "six one three five five five zero one nine eight"
    variants = [spoken, "613 555 0198", "(613) 555-0198", "6135550198"]
    out = {
        "dependencies": {name: importlib.metadata.version(name) for name in ["whisper-normalizer", "jiwer"]},
        "policy_commit": "651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a",
        "scope": "Text fixtures only. Benchmark policy, not a general-purpose entity parser.",
        "original_failure": score(spoken, "613 555 0198", STOCK),
        "phone_variants": [{"input": text, "stock": STOCK(text), "policy": score(spoken, text, benchmark_policy)} for text in variants],
        "wrong_digit": score(spoken, "613 555 0199", benchmark_policy),
        "leading_zero_control": score("007", "7", benchmark_policy),
        "ordinal_equivalence": score("first", "1st", benchmark_policy),
        "numeric_examples": [],
        "boundary_pairs": [],
        "regex_matches": {text: DIGIT_RUN.findall(text) for text in ["613", "31st", "31ST"]},
    }
    for text in ["0198", "007", "0500", "1", "31st", "31ST", "2:15 pm", "two fifteen p m", "$1,247.50", "one thousand two hundred forty seven dollars and fifty cents", "47B29K", "AB007", "A B zero zero seven", "(inaudible)"]:
        out["numeric_examples"].append({"input": text, "stock": STOCK(text), "policy": benchmark_policy(text)})
    for label, left, right, expected_equal in [
        ("Currency is meaningful", "$5", "5", False),
        ("Currency identity is meaningful", "$12", "€12", False),
        ("Euro unit is meaningful", "€12", "12", False),
        ("Sign is meaningful", "-12", "12", False),
        ("Decimal position is meaningful", "$1.25", "$12.5", False),
        ("Annotation is not spoken content", "(inaudible)", "inaudible", False),
        ("Alphanumeric letter grouping", "AB007", "A B zero zero seven", True),
        ("Case-insensitive ordinal", "31ST", "31st", True),
    ]:
        scored = score(left, right, benchmark_policy)
        out["boundary_pairs"].append({"case": label, "left": left, "right": right, "intended_equivalence": expected_equal, "policy_agrees": scored["exact_match"] == expected_equal, **scored})
    assert out["original_failure"]["wer_percent"] == 300.0
    assert out["original_failure"]["substitutions"] == 1
    assert out["original_failure"]["insertions"] == 2
    assert all(row["policy"]["wer_percent"] == 0 and row["policy"]["reference_tokens"] == 10 for row in out["phone_variants"])
    assert out["wrong_digit"]["wer_percent"] == 10.0
    assert out["wrong_digit"]["exact_match"] is False
    assert out["leading_zero_control"]["exact_match"] is False
    assert out["ordinal_equivalence"]["exact_match"] is True
    assert all(row["policy_agrees"] is False for row in out["boundary_pairs"])
    if args.corpus:
        raw = args.corpus.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != CORPUS_HASH:
            raise ValueError(f"Corpus hash mismatch: {digest}")
        rows = [json.loads(line) for line in raw.decode().splitlines() if line.strip()]
        counts = collections.Counter(row["category"] for row in rows)
        zeros = sum("0" in row["text"] for row in rows)
        out["corpus"] = {
            "sha256": digest, "utterances": len(rows), "categories": dict(counts),
            "digit_category_percent": 100 * counts["digits"] / len(rows),
            "references_containing_literal_zero": zeros,
            "references_containing_literal_zero_percent": 100 * zeros / len(rows),
            "all_reference_normalizations_idempotent": all(benchmark_policy(benchmark_policy(row["text"])) == benchmark_policy(row["text"]) for row in rows),
        }
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
