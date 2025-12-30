from pathlib import Path

import pandas as pd


def clean_scores(input_path: Path, output_path: Path) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    df = df.dropna(subset=["score"])
    df["score"] = pd.to_numeric(df["score"], errors="coerce").astype(int)
    df["score"] = df["score"].clip(lower=0, upper=100)

    df.to_csv(output_path, index=False)
    return df
