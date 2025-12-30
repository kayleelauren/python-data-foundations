from pathlib import Path

from python_data_foundations.clean_scores import clean_scores


def main() -> None:
    input_path = Path("data/sample_scores.csv")
    output_path = Path("data/clean_scores.csv")

    df = clean_scores(input_path, output_path)

    print("Wrote:", output_path)
    print(df)
    print("\nSummary:")
    print(df["score"].describe())


if __name__ == "__main__":
    main()
