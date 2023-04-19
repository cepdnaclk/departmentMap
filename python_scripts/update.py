import requests
import json
import os

# Where the API is available
apiIndex = 'https://api.ce.pdn.ac.lk/locations/v1/all'

r = requests.get(apiIndex)

# Fetch data from the people.ce.pdn.ac.lk
if r.status_code == 200:
    data = json.loads(r.text)

    filename = "../_data/locations.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=4))

