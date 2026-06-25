import logging
from pathlib import Path

import pandas as pd # type: ignore

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


def load_excel(file_path):
    """
    Load an Excel file into a DataFrame.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    df = pd.read_excel(file_path)

    logging.info(
        f"Loaded {len(df)} rows from {file_path.name}"
    )

    return df


if __name__ == "__main__":
    print("Loader module ready.")