# ver 0.2
# vlad note: to install the Requests module:
#  python -m pip install requests

import requests
from requests.auth import HTTPDigestAuth
import json

results = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast')

if results.ok:
    print('response status: 200 ok')
    #print((results.text))
    jData = json.loads(results.content)

    print(f'The JSON response contains {len(jData)} properties:')
    for key in jData:
        print(f'{key} : {jData[key]}')


else:
    print(f'something went wrong with the REST request. response status: {results.status_code}')



