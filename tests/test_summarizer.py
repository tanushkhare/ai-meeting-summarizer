import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_summarize_meeting():
    payload = {
        "title": "Backend Engineering Sync",
        "raw_transcript": "Marcus: I will handle the database migrations. Elena: Decision: We standardize on PostgreSQL."
    }
    res = client.post("/api/v1/meetings/summarize", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "MTG-" in data["meeting_id"]
    assert len(data["key_decisions"]) > 0
    assert len(data["action_items"]) > 0
