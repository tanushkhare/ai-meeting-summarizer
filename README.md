# ⚡ AI Meeting Summarizer

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://ai-meeting-summarizer-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://ai-meeting-summarizer-web.vercel.app](https://ai-meeting-summarizer-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Speech-to-text transcript parser and NLP summarization pipeline extracting actionable meeting minutes, speaker attributions, and deadlines.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** OpenAI Whisper, FastAPI, Pydantic v2
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🚀 API Contracts
```http
POST /api/v1/meeting/summarize
GET /health
```

---

## 💻 Local Quickstart
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v
```
