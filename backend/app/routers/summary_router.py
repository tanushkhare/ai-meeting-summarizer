from fastapi import APIRouter, HTTPException
from backend.app.schemas.meeting_schema import MeetingSummarizeRequest, MeetingSummaryResponse
from backend.app.services.summary_service import summarizer_service

router = APIRouter(prefix="/api/v1/meetings", tags=["Meeting Summarizer Engine"])

@router.post("/summarize", response_model=MeetingSummaryResponse)
async def summarize_meeting(payload: MeetingSummarizeRequest):
    try:
        result = summarizer_service.summarize_transcript(payload.title, payload.raw_transcript)
        return MeetingSummaryResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
