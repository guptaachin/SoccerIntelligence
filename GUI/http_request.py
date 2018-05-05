import requests

URL = 'http://localhost:7200/repositories/testis'

def make_request(query):
    PARAMS = {'query': query}
    try:
        r = requests.get(url=URL, params=PARAMS)
    except Exception as e:
        print(e)

    return r.text