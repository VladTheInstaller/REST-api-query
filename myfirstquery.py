# ver 0.6
# vlad note: to install the Requests module:
#  python -m pip install requests

import requests
from requests.auth import HTTPDigestAuth
import json

apiURL = 'https://swapi.dev/api/'
#apiURL = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'

print(f'sending GET request to API URL {apiURL}')
response = requests.get(apiURL)

if response.ok:
    print('response status: 200 ok')
    print(f'Content Type from response header: {response.headers["Content-Type"]}')

    # load the returned payload into JSON
    jData = json.loads(response.content)

    print(f'The JSON response contains {len(jData)} properties:')

    #print out the JSON response in a pretty indented format
    json_formatted_str = json.dumps(jData, indent=2)
    print(json_formatted_str)

else:
    print(f'something went wrong with the REST request. response status: {response.status_code}')
