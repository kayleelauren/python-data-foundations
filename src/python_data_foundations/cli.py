import argparse
from pathlib import Path

from python_data_foundations.clean_scores import clean_scores


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python-data-foundations",
        description="Small data workflow utilities (cleaning, validation, etc.).",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    clean = subparsers.add_parser(
        "clean-scores",
        help="Clean a scores CSV (drop missing, clamp scores to 0–100).",
    )
    clean.add_argument("input_csv", type=Path, help="Path to input CSV")
    clean.add_argument("output_csv", type=Path, help="Path to write cleaned CSV")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "clean-scores":
        df = clean_scores(args.input_csv, args.output_csv)
        print(f"Wrote: {args.output_csv}")
        print(df)
        return 0

    # Should never get here because argparse enforces commands
    return 1
