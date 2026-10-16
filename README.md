# wordfreq

A small, dependency-free Python word-frequency analyzer with a CLI.

## Install

```bash
uv pip install -e .
```

or run tests without installing:

```bash
uv run --with pytest pytest tests/ -q
```

## Use

```bash
wordfreq -n 5 README.md
```

Read from stdin:

```bash
echo "the quick brown fox" | wordfreq
```

## Test

```bash
uv run --with pytest pytest tests/ -q
```
