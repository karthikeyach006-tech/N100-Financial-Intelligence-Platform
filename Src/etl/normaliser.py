"""
normaliser.py

Utility functions for normalizing financial data before loading it
into the SQLite database.
"""

import re
from typing import Any


def normalize_year(year: Any) -> int:
    """
    Normalize year values into a 4-digit integer.

    Supported formats:
        2024
        "2024"
        "2024-25"
        "2024/25"
        "FY2024"
        "FY 2024"
        2024.0

    Returns:
        int

    Raises:
        ValueError
    """

    if year is None:
        raise ValueError("Year cannot be None")

    year = str(year).strip().upper()

    if year == "":
        raise ValueError("Year cannot be empty")

    match = re.search(r"(19|20)\d{2}", year)

    if not match:
        raise ValueError(f"Invalid year: {year}")

    normalized = int(match.group())

    if normalized < 1900 or normalized > 2100:
        raise ValueError(f"Year out of range: {normalized}")

    return normalized


def normalize_ticker(ticker: Any) -> str:
    """
    Normalize stock ticker.

    Examples:
        tcs
        TCS
        tcs.ns
        INFY.NS

    Returns uppercase ticker.
    """

    if ticker is None:
        raise ValueError("Ticker cannot be None")

    ticker = str(ticker).strip().upper()

    if ticker == "":
        raise ValueError("Ticker cannot be empty")

    ticker = re.sub(r"\s+", "", ticker)

    return ticker