# RMPApi

A lightweight, **unofficial Python API** for scraping professor information from **RateMyProfessors** using Selenium.

This project allows you to search for professors by name and school, retrieve ratings, difficulty, and the percentage of students who would take the professor again.

---

## Features

*  Search professors by name
*  Retrieve professor details by professor ID
*  Extract rating, difficulty, and % would take again
*  Fetch multiple professor results with pagination support
*  Simple, Pythonic interface
*  Headless Chrome browser (no UI required)

---

## Installation

### Prerequisites

* Python **3.9+** recommended
* Google Chrome installed
* Compatible **ChromeDriver** version

### Install dependencies

```bash
pip install selenium
```

Make sure `chromedriver` is available on your system PATH or managed automatically by your environment.

---

## Project Structure

```text
rmp_api/
├── rmp_api.py        # Main API logic (this file)
├── models.py         # Professor data model
├── exceptions.py     # Custom exceptions
└── __init__.py
```

All primary functionality lives inside **`rmp_api.py`**.

---

## Usage

### Basic Example

```python
from rmp_api import RMPApi

SCHOOL_CODE = 1234  # Replace with your school's RateMyProfessors ID

with RMPApi(SCHOOL_CODE) as api:
    prof = api.query_prof("John Smith")
    if prof:
        print(prof.name, prof.rating)
```

---

## API Reference

### `RMPApi(school_code: int)`

Creates a new API instance for a specific school.

* `school_code`: RateMyProfessors school ID

Supports context manager usage (`with` statement) to ensure the browser closes properly.

---

### `get_prof(professor_code: int) -> Optional[Professor]`

Fetches professor data directly from a professor ID.

Returns:

* `Professor` object on success
* `None` if data cannot be retrieved

---

### `query_prof(text_query: str) -> Optional[Professor]`

Searches for a professor by name and returns the **first match**.

```python
api.query_prof("Jane Doe")
```

---

### `query_prof_codes(text_query: str, limit: int = 5) -> List[int]`

Returns a list of professor IDs matching the search query.

* Automatically paginates results
* Stops once `limit` is reached

---

### `query_profs(text_query: str, limit: int = 5) -> List[Professor]`

Fetches **multiple professor profiles** for a given search query.

```python
api.query_profs("Calculus", limit=3)
```

---

## Professor Model

Each `Professor` object contains:

* `name`
* `rating`
* `difficulty`
* `percent_take_again`

Exact implementation lives in `models.py`.

---

## Error Handling

The API gracefully handles:

* Missing HTML elements
* Timeouts
* Invalid professor IDs

Failures return `None` or empty lists instead of raising errors.

---

## Notes & Limitations

* Scraping depends on RateMyProfessors CSS class names
* Heavy usage may trigger bot detection
* Not suitable for large-scale scraping

---

## Future Improvements

* Replace Selenium with requests + Playwright fallback
* Add caching layer
* Async support
* CLI interface

---

## License

MIT License

---

## Author

Created by **Andrew Valentine** 🚀
