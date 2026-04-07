import os
from pathlib import Path
import sys

# Handle PyInstaller vs normal execution
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent

# Imports
from modules.translator import run_translation
from modules.collector import collect_and_clean
from modules.exporter import export_wide

# Paths
INPUT_DIR = BASE_DIR / "Input"
OUTPUT_DIR = BASE_DIR / "Output" / "TranslatorOutput"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

RAW_OUT = OUTPUT_DIR / "TranslatedData_raw.csv"
FINAL_OUT = OUTPUT_DIR / "TranslatedData.csv"
WIDE_OUT = OUTPUT_DIR / "TranslatedData_wide.csv"


def get_latest_input(input_dir):
    files = [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, f))
    ]

    if not files:
        raise RuntimeError("No input files found in Input folder.")

    return max(files, key=os.path.getmtime)


if __name__ == "__main__":
    try:
        print("=== Capability Engine ===\n")

        input_file = get_latest_input(INPUT_DIR)
        print("Reading:", input_file)

        print("Running translator...")
        run_translation(input_file, RAW_OUT)

        print("Running collector...")
        collect_and_clean(RAW_OUT, FINAL_OUT)

        print("\nFinished.")
        print("Raw data:", RAW_OUT)
        print("Cleaned data:", FINAL_OUT)

        print("Running exporter...")
        export_wide(FINAL_OUT, WIDE_OUT)

        print("\nFinished.")
        print("Long format:", FINAL_OUT)
        print("Wide format:", WIDE_OUT)

    except Exception as e:
        print("ERROR:", e)
