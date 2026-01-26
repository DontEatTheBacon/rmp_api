from rmp_api import RMPApi

with RMPApi(school_code=2774) as api:
    profs = api.query_profs('mom')
    for prof in profs:
        print(prof)
    print(f'{len(profs)} results')