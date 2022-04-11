# ver 0.4
# vlad note: to install the Requests module:
#  python -m pip install requests

import requests
from requests.auth import HTTPDigestAuth
import json

#results = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast')
results = requests.get('https://swapi.dev/api/')

if results.ok:
    print('response status: 200 ok')

    # load the returned payload into JSON
    jData = json.loads(results.content)

    print(f'The JSON response contains {len(jData)} properties:')

    #print out the JSON results in a pretty indented format
    json_formatted_str = json.dumps(jData, indent=2)
    print(json_formatted_str)

else:
    print(f'something went wrong with the REST request. response status: {results.status_code}')
