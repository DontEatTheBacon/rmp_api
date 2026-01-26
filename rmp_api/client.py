from typing import List, Optional

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from .exceptions import MissingElement
from .models import Professor

class RMPApi:
    _chrome_options = Options()
    _chrome_options.add_argument('--headless')
    _chrome_options.add_argument("--disable-gpu")
    _chrome_options.add_argument("--no-sandbox")
    _chrome_options.add_argument("--disable-dev-shm-usage")
    _chrome_options.page_load_strategy = 'eager'

    _prof_url = 'https://www.ratemyprofessors.com/professor'
    _search_url = 'https://www.ratemyprofessors.com/search/professors'

    class _CssClasses:
        PROFESSOR_NAME = 'cSXRap'
        RATING = 'duhvlP'
        PERCENT_AND_DIFFICULTY = 'ecFgca'
        PROF_CARD = 'TeacherCard__StyledTeacherCard-syjs0d-0'
        PAGINATION_BUTTON = 'joxzkC'

    def __init__(self, school_code: int):
        self._browser = webdriver.Chrome(options=RMPApi._chrome_options)
        self._wait = WebDriverWait(self._browser, 10)
        self.school_code = school_code

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._browser.quit()

    def __repr__(self):
        return '<RMPApi>'
    
    def _extract_prof_code(self, element: WebElement) -> int:
        href = element.get_attribute('href')
        if not href:
            raise MissingElement('RMPApi element href could not be found.')
        
        url_parts = href.split('/')
        if len(url_parts) < 5:
            raise MissingElement('RMPApi element prof_code could not be found.')
        
        return int(url_parts[4])


    def get_prof(self, professor_code: int) -> Optional[Professor]:
        try:
            self._browser.get(f'{RMPApi._prof_url}/{professor_code}')

            name = self._browser.find_element(By.CLASS_NAME, self._CssClasses.PROFESSOR_NAME).text
            rating = self._browser.find_element(By.CLASS_NAME, self._CssClasses.RATING).text

            elements = self._browser.find_elements(By.CLASS_NAME, self._CssClasses.PERCENT_AND_DIFFICULTY)

            if len(elements) < 2:
                raise MissingElement('RMPApi element percent_take_again or difficulty could not be found.')
            
            percent_take_again, difficulty = [
                element.text for element in elements
                ]

            return Professor(name, rating, difficulty, percent_take_again)
        
        except (MissingElement, NoSuchElementException, TimeoutException):
            return None
        
    def query_prof(self, text_query: str) -> Optional[Professor]:
        search_arg = '%20'.join(text_query.split())
        url = f'{RMPApi._search_url}/{self.school_code}?q={search_arg}'

        try:
            self._browser.get(url)
            element = self._browser.find_element(By.CLASS_NAME, self._CssClasses.PROF_CARD)

            prof_code = self._extract_prof_code(element)

            return self.get_prof(prof_code)
        
        except (MissingElement, NoSuchElementException, TimeoutException, ValueError):
            return None
        
    def query_prof_codes(self, text_query: str, limit: int=5) -> List[int]:
        search_arg = '%20'.join(text_query.split())
        url = f'{RMPApi._search_url}/{self.school_code}?q={search_arg}'

        try:
            self._browser.get(url)
        except TimeoutException:
            return []

        try: 
            button = self._browser.find_element(By.CLASS_NAME, self._CssClasses.PAGINATION_BUTTON)
            current_count = len(self._browser.find_elements(By.CLASS_NAME, self._CssClasses.PROF_CARD))

            while(current_count < limit):
                button.click()

                self._wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, self._CssClasses.PROF_CARD)) > current_count)
                new_count = len(self._browser.find_elements(By.CLASS_NAME, self._CssClasses.PROF_CARD))

                if new_count == current_count:
                    break

                current_count = new_count
        except NoSuchElementException:
            pass

        elements = self._browser.find_elements(By.CLASS_NAME, self._CssClasses.PROF_CARD)
        if len(elements) > limit:
            elements = elements[:limit]

        prof_codes = []
        for element in elements:
            try:
                prof_codes.append(self._extract_prof_code(element))

            except (MissingElement, NoSuchElementException, ValueError):
                continue

        return prof_codes 

    def query_profs(self, text_query: str, limit: int=5) -> List[Optional[Professor]]:
        prof_codes = self.query_prof_codes(text_query, limit)
        profs = [prof for prof in [self.get_prof(prof_code) for prof_code in prof_codes] if prof]
        return profs