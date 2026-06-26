"""
loader.py

Loads all Excel files from the raw data directory.
"""

import logging
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

RAW_DATA_DIR = Path(os.getenv("RAW_DATA_DIR", "data/raw"))

# Create logs directory
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_excel(file_path):
    """
    Load a single Excel file.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    df = pd.read_excel(file_path)

    logging.info(f"Loaded {file_path.name} ({len(df)} rows)")

    return df


def load_all_excel_files():
    """
    Load all Excel files from RAW_DATA_DIR.

    Returns:
        dict[str, DataFrame]
    """
    datasets = {}

    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw data directory '{RAW_DATA_DIR}' does not exist."
        )

    excel_files = list(RAW_DATA_DIR.glob("*.xlsx"))

    if not excel_files:
        logging.warning("No Excel files found.")
        return datasets

    for file in excel_files:
        try:
            datasets[file.stem] = load_excel(file)
        except Exception as e:
            logging.error(f"Failed to load {file.name}: {e}")

    return datasets


def main():
    datasets = load_all_excel_files()

    print(f"\nLoaded {len(datasets)} dataset(s).\n")

    for name, df in datasets.items():
        print(f"{name}: {len(df)} rows")


if __name__ == "__main__":
    main()