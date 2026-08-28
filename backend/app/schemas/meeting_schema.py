from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ActionItem(BaseModel):
    assignee: str
    task: str
    priority: str = "Medium"

class MeetingSummarizeRequest(BaseModel):
    title: str = Field(default="Sprint Architecture Review", min_length=3)
    raw_transcript: str = Field(..., min_length=20, description="Speaker transcript or meeting dialog")

class MeetingSummaryResponse(BaseModel):
    meeting_id: str
    title: str
    executive_summary: str
    key_decisions: List[str]
    action_items: List[ActionItem]
    speakers_detected: List[str]
    duration_minutes_estimate: float
    timestamp: str
