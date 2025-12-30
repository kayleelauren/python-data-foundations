from pathlib import Path

from scripts.clean_scores import clean_scores



def test_clean_scores_creates_output(tmp_path: Path) -> None:
    input_csv = tmp_path / "in.csv"
    output_csv = tmp_path / "out.csv"

    input_csv.write_text("name,score\nA,10\nB,\nC,999\n", encoding="utf-8")

    df = clean_scores(input_csv, output_csv)

    assert output_csv.exists()
    assert df["score"].tolist() == [10, 100]
