# Lab 7 — Fuzz Testing with Hypothesis

## Completed files
- `processor.py`: hardened input-processing functions.
- `test_processor.py`: Hypothesis no-crash tests plus valid/invalid behaviour checks.

## Run on your machine
From this `LAB7` directory:

```bash
python -m pip install hypothesis pytest
python processor.py
python -m pytest -v test_processor.py
```

The Hypothesis tests generate arbitrary text and `None` values. The completed
processor returns `None` for invalid inputs rather than raising exceptions.
Valid inputs preserve the lab's expected outputs.

## Input handling decisions
- Storage quota accepts non-negative integer values with MB, GB, or TB suffixes.
- Compression metrics require exactly two finite numeric values separated by
  one colon; raw bytes must be non-negative and compressed bytes must be positive.
- Bandwidth tiers recognize HOT, COL, and ARC prefixes, case-insensitively.
- Invalid or unsupported values return `None`.

## Screenshot deliverables still to capture locally
The handout requests screenshots of:
1. Running the original buggy `processor.py`.
2. Failing tests against the original buggy processor.
3. Running the fixed `processor.py`.
4. Passing tests against the fixed processor.

The original versions are available in the uploaded files in this conversation.
