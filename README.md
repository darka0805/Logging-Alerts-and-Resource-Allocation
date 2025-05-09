# Logging-Alerts-and-Resource-Allocation

### Project Overview
This project is a microservice-based logging and alerting system built with FastAPI, Celery, Redis, InfluxDB, and Docker. It allows asynchronous processing of user interactions, logs structured data into a time-series database, and triggers alerts for sensitive information (e.g., PII) through a dedicated alerting service.

### Structure

```
HW7/
├── influxdb_data/
│   ├── data/
│   ├── meta/
│   └── wal/
├── logger_alert_engine/
│   └── error_reports/
│   ├── Dockerfile
│   ├── monitor.py
│   └── requirements.txt
└── web_app/
│    ├── celery_app.py
│    ├── Dockerfile
│    ├── main.py
│    └── requirements.txt
├── docker-compose.yml
├── README.md
└── task 3-4 AIT.pdf
```


### Run app

<pre lang="markdown">docker-compose up --build</pre>

### Test app

<pre lang="markdown">curl -X POST http://localhost:8000/submit/ \
     -H "Content-Type: application/json" \
     -d '{"user_id": "123", "message": "this is a test log"}'</pre>

### Expected output

![image](https://github.com/user-attachments/assets/e40c4528-e463-47be-a345-c57d93a24c40)

