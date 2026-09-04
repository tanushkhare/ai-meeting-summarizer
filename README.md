# ⚡ AI Meeting Summarizer

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://ai-meeting-summarizer-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://ai-meeting-summarizer-web.vercel.app](https://ai-meeting-summarizer-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Speech-to-text transcript parser and NLP summarization pipeline extracting actionable meeting minutes, speaker attributions, and deadline-tracked action items.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** OpenAI Whisper, FastAPI, Pydantic v2
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Purged Legacy Code:** Replaced misfiled ETL code with genuine meeting summarization logic.
* **Speaker Attribution:** Action items are tied directly to participant identities.
* **Temporal Extraction:** Automatically captures target completion dates.

---

## 🚀 API Contracts
```http
POST /api/v1/meeting/summarize
Request:
{
  "transcript": "Alex: We need to deploy auth by Friday. Jordan: I will update K8s manifests by Wednesday."
}

Response (200 OK):
{
  "summary": "Team agreed to complete authentication service rollout by Friday.",
  "action_items": [
    {"assignee": "Jordan", "task": "Update K8s manifests", "deadline": "Wednesday"},
    {"assignee": "Alex", "task": "Coordinate auth deployment", "deadline": "Friday"}
  ]
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v