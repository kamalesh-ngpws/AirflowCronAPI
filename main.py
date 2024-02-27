from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Priorities(BaseModel):
    id:int
    priority: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    pass

app = FastAPI()

@app.post('/cron')
def cron_payload(payload:Priorities):
    return payload 