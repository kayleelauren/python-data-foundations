"""Small pandas sanity-check demo."""

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie", "Dana"],
            "score": [85, 92, 78, 88],
        }
    )

    print(df)
    print("\nAverage score:", df["score"].mean())


if __name__ == "__main__":
    main()
