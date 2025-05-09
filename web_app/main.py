from fastapi import FastAPI, Request
from celery_app import log_interaction
import datetime

app = FastAPI()

@app.post("/submit/")
async def submit_data(request: Request):
    data = await request.json()
    log_interaction.delay(data)
    return {"message": "Task received and is being processed"}
