# RMPApi

An unofficial Python API for scraping professor information from **RateMyProfessors** using Selenium. Retrieve ratings, difficulty, and % of students who would take the professor again.

## Quick Install

Install directly from GitHub:

```bash
pip install git+https://github.com/DontEatTheBacon/rmp_api.git
```

Or clone and install manually:

```bash
git clone https://github.com/DontEatTheBacon/rmp_api.git
cd rmp_api
pip install -e .
```

## Usage

```python
from rmp_api import RMPApi

SCHOOL_CODE = 1234  # Your school's RateMyProfessors ID

with RMPApi(SCHOOL_CODE) as api:
    prof = api.query_prof("John Smith")
    if prof:
        print(prof.name, prof.rating)
```

## API Reference

```python
# Create API instance for a specific school (supports 'with' for browser cleanup)
RMPApi(school_code: int)

# Fetch a professor by ID
get_prof(professor_code: int) -> Optional[Professor]

# Search for a professor by name, returns first match
query_prof(text_query: str) -> Optional[Professor]

# Return a list of professor IDs matching the query
query_prof_codes(text_query: str, limit: int = 5) -> List[int]

# Return multiple professor profiles matching the query
query_profs(text_query: str, limit: int = 5) -> List[Professor]
```

## Professor Model

```python
# Professor object attributes
name
rating
difficulty
percent_take_again
```

## Error Handling

Missing elements, timeouts, or invalid IDs return `None` or empty lists.

## License

MIT License

## Author

Andrew Valentine
