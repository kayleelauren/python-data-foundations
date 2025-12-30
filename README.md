# Python Data Foundations

[![CI](https://github.com/kayleelauren/python-data-foundations/actions/workflows/ci.yml/badge.svg)](https://github.com/kayleelauren/python-data-foundations/actions/workflows/ci.yml)

A small Python project demonstrating clean project structure, data processing,
testing, and modern Python tooling. This repository is intended as a foundation
for data-focused and AI-adjacent Python workflows.

---

## Project Goals

- Practice Python fundamentals for data workflows
- Demonstrate pandas-based data cleaning and validation
- Use a modern `src/` project layout with an installable package
- Include automated tests and reproducible setup
- Follow current Python best practices (Python 3.14+)

---

## Project Structure

```
.
├── src/
│   └── python_data_foundations/
│       ├── __init__.py
│       └── clean_scores.py
├── scripts/
│   └── clean_scores.py
├── tests/
│   └── test_clean_scores.py
├── data/
│   ├── sample_scores.csv
│   └── clean_scores.csv
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Directory Overview

- **`src/python_data_foundations/`**  
  Reusable, importable project code (library-style modules).

- **`scripts/`**  
  Runnable entry-point scripts that orchestrate project logic.

- **`tests/`**  
  Automated tests using `pytest`.

- **`data/`**  
  Small example input and output datasets for demonstration purposes.

---

## Requirements

- Python 3.14+
- macOS or Linux
- `pip` and `venv`

---

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

---

## Command-Line Interface (CLI)

This project provides a command-line interface for running data workflows.

Clean a scores CSV using the package CLI:

```bash
python -m python_data_foundations clean-scores data/sample_scores.csv data/clean_scores.csv
```

If the project is installed in editable mode, the CLI can also be run as a command:

```bash
python-data-foundations clean-scores data/sample_scores.csv data/clean_scores.csv
```

The CLI is designed to be extensible and will serve as the primary interface
for future data and AI-related workflows.

---

## Run the Example Script

```bash
python scripts/clean_scores.py
```

This will:
- Read sample CSV data
- Clean and validate score values
- Write a cleaned output file
- Print a summary to the console

---

## Run Tests

```bash
pytest
```

Tests validate that:
- Missing data is handled correctly
- Invalid score values are clamped
- Output files are generated as expected

---

## Tooling

- pandas for data processing
- pytest for testing
- ruff for linting and formatting
- editable install (`pip install -e .`) for clean imports

**Note**: Linting, formatting and tests are enforced locally via pre-commit hooks.

---

## Status

This project is intentionally small and focused. It serves as a foundation for
future expansion into more advanced data processing, annotation tooling, and
AI-related workflows.

