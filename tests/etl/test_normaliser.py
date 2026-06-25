import pytest

from src.etl.normaliser import (
    normalize_year,
    normalize_ticker
)


def test_year_integer():
    assert normalize_year(2024) == 2024


def test_year_string():
    assert normalize_year("2024") == 2024


def test_year_financial():
    assert normalize_year("2024-25") == 2024


def test_year_fy():
    assert normalize_year("FY2023") == 2023


def test_ticker_lower():
    assert normalize_ticker("tcs") == "TCS"


def test_ticker_upper():
    assert normalize_ticker("TCS") == "TCS"


def test_ticker_spaces():
    assert normalize_ticker(" infy ") == "INFY"