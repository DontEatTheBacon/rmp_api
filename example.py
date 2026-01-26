from rmp_api import RMPApi

with RMPApi(school_code=2774) as api:
    prof = api.query_prof('Van Ma')
    print(prof)