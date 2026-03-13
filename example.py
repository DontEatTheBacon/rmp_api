from rmp_api import RMPApi
from rmp_api.models import Professor

# Use RMPApi as a context manager to handle cleanup
with RMPApi(school_code=2774) as api:
    # Methods may return None or empty or shorter than expected lists if data is missing or a timeout occurs

    # Using a known professor code
    prof_code = 2049771
    prof = api.get_prof(prof_code)

    # Search by name and return first result
    prof = api.query_prof('Van Ma')

    # Query codes which can be used for lookup later
    prof_codes = api.query_prof_codes('Van Ma', limit=5)

    # Fetch multiple professors by name
    profs = api.query_profs('Van Ma', limit=5)

    # Safely print professor attributes
    if prof:
        print(f'{prof.name} is rated: {prof.rating}, '
              f'has difficulty {prof.difficulty} and '
              f'%{prof.percent_take_again} would take again.')

        # Convert to dict 
        json_prof = prof.to_dict()

        # Load from dict
        loaded_prof = Professor.from_dict(json_prof)
