"""Core analysis functions for wordfreq."""

import re
from collections import Counter

# Words we ignore (simple hard-coded stop-word list).
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "is", "was", "are", "were",
    "in", "on", "at", "to", "for", "of", "by", "from", "with", "as",
    "it", "its", "this", "that", "these", "those", "i", "you", "he",
    "she", "we", "they", "he", "him", "her", "them", "me", "my", "your",
}


def tokenize(text: str) -> list[str]:
    """Split text into lower-cased word tokens (alphanumeric runs)."""
    return [m.lower() for m in re.findall(r"[a-z0-9']+", text.lower())]


def frequencies(text: str, top: int | None = None, exclude_stopwords: bool = True) -> list[tuple[str, int]]:
    """Return the most frequent words as (word, count) pairs.

    Args:
        text: The input text.
        top: Maximum number of results. `None` returns all.
        exclude_stopwords: Whether to drop common stop-words.
    """
    tokens = tokenize(text)
    if exclude_stopwords:
        tokens = [t for t in tokens if t not in STOP_WORDS]
    counts = Counter(tokens)
    items = counts.most_common()
    return items[:top] if top else items


def summary(text: str, top: int = 10) -> dict:
    """Return a summary dict of the text."""
    tokens = tokenize(text)
    words = [t for t in tokens if t not in STOP_WORDS]
    counts = Counter(tokens)
    return {
        "total_tokens": len(tokens),
        "non_stopwords": len(words),
        "unique_words": len(counts),
        "most_common": frequencies(text, top=top),
    }
