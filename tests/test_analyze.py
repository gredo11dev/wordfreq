from wordfreq.analyze import frequencies, summary, tokenize


def test_tokenize():
    assert tokenize("Hello, World! hello world") == [
        "hello", "world", "hello", "world",
    ]


def test_frequencies_top():
    text = "apple apple banana banana banana cherry"
    assert frequencies(text, top=1, exclude_stopwords=False) == [("banana", 3)]


def test_summary_counts():
    text = "the cat sat on the mat"
    s = summary(text)
    assert s["total_tokens"] == 6
    assert s["non_stopwords"] == 3  # the & on are stop-words
    assert s["unique_words"] == 5
    # "the" is a stopword, so top should be cat/sat/on/mat
    words = [w for w, _ in s["most_common"]]
    assert "the" not in words


def test_empty_text():
    s = summary("")
    assert s["total_tokens"] == 0
    assert s["most_common"] == []
