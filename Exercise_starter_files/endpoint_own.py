import requests
import json

url = "http://4aeb0182-4589-4dbc-acd7-bf11ebe46f34.southcentralus.azurecontainer.io/score"
key = "ZlOZnbfAElkd25W3iSHCT9Qk7hkC4RuN"

headers = {"Content-Type": "application/json"}
headers["Authorization"] = "Bearer {}".format(key)

data = {
    "data": [
        {
            "instant": 1,
            "date": "2013-01-01 00:00:00,000000",
            "season": 1,
            "yr": 0,
            "mnth": 1,
            "weekday": 6,
            "weathersit": 2,
            "temp": 0.344167,
            "atemp": 0.363625,
            "hum": 0.805833,
            "windspeed": 0.160446,
            "casual": 331,
            "registered": 654,
        },
    ]
	}

data_input = json.dumps(data)
with open("data_input.json", "w") as f:
	f.write(data_input)

resp = requests.post(url, data_input, headers=headers)
print(resp.json())
