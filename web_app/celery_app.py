from celery import Celery
from influxdb import InfluxDBClient
import datetime
import requests

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@app.task
def log_interaction(data):
    client = InfluxDBClient(host='influxdb', port=8086, database='logs')
    timestamp = datetime.datetime.utcnow().isoformat()

    point = {
        "measurement": "interactions",
        "tags": {
            "user": data.get("user_id", "unknown"),
        },
        "time": timestamp,
        "fields": {
            "payload": str(data)
        }
    }

    client.write_points([point])

    # Send suspicious data to alert engine (if SSN is detected)
    if "ssn" in str(data).lower():
        requests.post("http://logger:5001/alert", json={"time": timestamp, "event": "PII", "description": str(data)})
