# N100 Financial Intelligence Platform

## Sprint 1 – Data Foundation

### Project Overview
This project builds the data foundation for the N100 Financial Intelligence Platform. It focuses on extracting, validating, normalizing, and loading financial data into a SQLite database.

### Sprint 1 Objectives
- Load data from 12 Excel source files
- Validate data using 16 Data Quality (DQ) rules
- Create a normalized SQLite database (`nifty100.db`)
- Generate load and validation reports
- Prepare the foundation for future analytics modules

### Project Structure

```
N100_Financial_Intelligence_Platform/
├── data/
├── db/
├── src/
├── tests/
├── notebooks/
├── output/
├── requirements.txt
├── .env
├── Makefile
└── README.md
```

### Technologies
- Python
- Pandas
- SQLite
- SQLAlchemy
- OpenPyXL
- Pytest

### Author
CH Karthikeya
