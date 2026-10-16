"""Command-line interface for wordfreq."""

import argparse
import sys

from .analyze import summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="wordfreq",
        description="Analyze word frequency in a text file.",
    )
    parser.add_argument("file", nargs="?", default="-", help="Input file (- for stdin)")
    parser.add_argument("-n", "--top", type=int, default=10, help="Number of top words to show (default: 10)")
    args = parser.parse_args(argv)

    if args.file == "-":
        text = sys.stdin.read()
    else:
        with open(args.file, "r", encoding="utf-8") as fh:
            text = fh.read()

    result = summary(text, top=args.top)
    print(f"Total tokens:      {result['total_tokens']}")
    print(f"Non-stopwords:     {result['non_stopwords']}")
    print(f"Unique words:      {result['unique_words']}")
    print()
    print("Top words:")
    for word, count in result["most_common"]:
        bar = "#" * min(count, 40)
        print(f"  {word:<12} {count:5} |{bar}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
