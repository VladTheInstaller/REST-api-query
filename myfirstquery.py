# ver 0.1
# vlad note: to install the Requests module:
#  python -m pip install requests

import requests
from requests.auth import HTTPDigestAuth
import json

results = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast')

if results.ok:
    print('response status: 200 ok')
    #print((results.text))


else:
    print(f'something went wrong with the REST request. response status: {results.status_code}')
    #print(results.status_code)


