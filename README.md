# RMPApi

An unofficial Python API for scraping professor information from **RateMyProfessors** using Selenium. Retrieve ratings, difficulty, and % of students who would take the professor again.

## Installation
```bash
pip install selenium
```
Requirements: Python 3.9+, Google Chrome, compatible ChromeDriver.

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
**RMPApi(school_code: int)** – Create API instance; supports `with` for browser cleanup  
**get_prof(professor_code: int) -> Optional[Professor]** – Fetch professor by ID  
**query_prof(text_query: str) -> Optional[Professor]** – Search by name, returns first match  
**query_prof_codes(text_query: str, limit: int = 5) -> List[int]** – Return professor IDs  
**query_profs(text_query: str, limit: int = 5) -> List[Professor]** – Return multiple professor profiles  

**Professor model:** `name`, `rating`, `difficulty`, `percent_take_again`  

Error handling: Missing elements, timeouts, or invalid IDs return `None` or empty lists.

## License
MIT License  

## Author
Andrew Valentine
