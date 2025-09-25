from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os
import requests

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")

class Incident(BaseModel):
    description: str
    location: Optional[str] = None
    # Add more fields as needed

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/incidents")
def create_incident(incident: Incident):
    if not DATABASE_URL:
        raise HTTPException(status_code=500, detail="DATABASE_URL not set")
    # Insert into Supabase (using REST API for simplicity)
    headers = {
        "apikey": DATABASE_URL,
        "Authorization": f"Bearer {DATABASE_URL}",
        "Content-Type": "application/json"
    }
    data = incident.dict()
    # Replace 'incidents' with your Supabase table name
    resp = requests.post(f"{DATABASE_URL}/rest/v1/incidents", json=data, headers=headers)
    if resp.status_code not in (200, 201):
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()

@app.post("/plan/{incident_id}")
def plan_assignment(incident_id: int = Path(...)):
    # Dummy greedy assignment logic
    # In real use, fetch incident and resources, assign resources
    assignment = {"incident_id": incident_id, "assigned": True}
    return assignment
