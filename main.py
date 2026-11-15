from pathlib import Path
import sys


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parent
    feature_dir = project_dir / "feature"
    child_ecg_folder = project_dir / "Child_ecg"
    output_csv = project_dir / "feature data.csv"
    failed_log = project_dir / "failed_records.txt"

    import subprocess

    subprocess.run(
        [
            sys.executable,
            str(feature_dir / "extract_dataset.py"),
            "--input",
            str(child_ecg_folder),
            "--output",
            str(output_csv),
            "--failed-log",
            str(failed_log),
        ],
        check=True,
    )
