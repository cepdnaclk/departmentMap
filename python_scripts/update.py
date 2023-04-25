import requests
import json
import os

# Where the API is available
apiIndex = 'https://api.ce.pdn.ac.lk/locations/v1'

floors = ['G', '01', '02', '03', '04', '05']

r = requests.get("{0}/all".format(apiIndex))

# Fetch data from the people.ce.pdn.ac.lk
if r.status_code == 200:
    data = json.loads(r.text)

    # for floor in data:
    #     sorted_locations = {
    #         "title": data[floor]['title'],
    #         "locations": sorted(data[floor]['locations'], key=lambda x: x['id'])
    #     }
    #     data[floor] = sorted_locations

    filename = "../_data/locations.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=4))

    for floor in data:
        r2 = requests.get("{0}/{1}".format(apiIndex, floor))
        if r2.status_code == 200:
            floorData = json.loads(r2.text)

            filenameFloor = "../data/{0}.json".format(floor)
            os.makedirs(os.path.dirname(filenameFloor), exist_ok=True)

            with open(filenameFloor, "w") as f:
                f.write(json.dumps(floorData, indent=4))