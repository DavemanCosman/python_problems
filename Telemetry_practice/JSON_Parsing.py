# Given the following:
# * device {id: value}
# * timestamp
# * engine_temp {temp: value}
# * gps [lat, long]
# Return a clean Pandas data frame
# 
# e.g. input
# logs = [
#   '{"device": {"id": "A12"},
#       "ts": "2024-01-01T10:00:00Z",
#       "metrics": {"engine": {"temp": 87}},
#       "gps": [43.7, -79.4]}',
#   '{"device": {"id": "A12"},
#       "ts": "2024-01-01T10:01:00Z",
#       "metrics": {"engine": {"temp": 90}},
#       "gps": [43.71, -79.41]}'
#]

import json
import pandas as pd

sef parse_logs(logs):
records = []
for entry in logs:
  data = json.loads(entry)
  records.append({
    "device_id": data["device"]["id"],
    "timestamp": pd.to_datetime(data["ts"]),
    "engine_temp": data["metrics"]["engine"],
    "lat": data["gps"][0],
    "lon": data["gps"][1]
  })
return pd.DataFrame(records)

int(df)
