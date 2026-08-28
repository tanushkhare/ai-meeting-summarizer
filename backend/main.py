from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import summary_router
import uvicorn

app = FastAPI(
    title="AI Meeting Summarizer & Executive Briefing API",
    description="Multi-speaker transcript extraction, decision tree mapping, and automated action item parsing.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summary_router.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ai-meeting-summarizer"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
