from pathlib import Path

import pandas as pd

from src.etl.loader import load_excel


def test_missing_file():
    try:
        load_excel("does_not_exist.xlsx")
        assert False
    except FileNotFoundError:
        assert True