# Logging-Alerts-and-Resource-Allocation
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


![image](https://github.com/user-attachments/assets/e40c4528-e463-47be-a345-c57d93a24c40)

