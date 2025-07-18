# AI Meeting Summary + CRM Note Generator

Automatically summarize meeting transcripts, extract client pain points, objections, and action items — ready for CRM logging.

![screenshot](https://via.placeholder.com/900x200?text=AI+CRM+Summarizer+Demo)

---

## ✨ Features

* ✏️ Paste or upload your meeting transcript (text)
* 🧠 AI-powered summary generation
* ✅ Extracts:

  * Client pain points
  * Objections and resolutions
  * Action items and follow-ups
* 📦 Export-ready output for CRM systems
* 🌐 Frontend: React + Axios
* ⚙️ Backend: FastAPI + OpenRouter (Mistral / Claude)
* 💡 Free & Open Source (no paid GPT-4 key needed)

---

## 🛠 Tech Stack

| Layer    | Technology                          |
| -------- | ----------------------------------- |
| Frontend | React.js                            |
| Backend  | FastAPI (Python)                    |
| AI Model | Mistral 7B via OpenRouter API       |
| Hosting  | Vercel (frontend), Render (backend) |

---

## 📦 Project Structure

```
ai-meeting-summary-crm/
├── frontend/       # React app (Vercel deploy)
├── backend/        # FastAPI app (Render deploy)
│   ├── main.py
│   ├── .env.example
│   └── requirements.txt
```

---

## ⚙️ Environment Variables

**Frontend**

```
REACT_APP_BACKEND_URL=https://your-backend-url
```

**Backend**

```
OPENROUTER_API_KEY=org-xxxxxxxxxx  # from https://openrouter.ai/keys
```

---

## 🧪 Local Setup

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-meeting-summary-crm.git
cd ai-meeting-summary-crm
```

### 2. Install backend (FastAPI)

```bash
cd backend
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Install frontend (React)

```bash
cd ../frontend
npm install
npm start
```

---

## 🧠 Free AI Models Supported

This project uses [OpenRouter](https://openrouter.ai) to access:

* `mistralai/mistral-7b-instruct`
* `claude-3-haiku`
* `openchat/openchat-7b`

> Create your free API key here: [https://openrouter.ai/keys](https://openrouter.ai/keys)

---

## 🤩 To-Do Features

* [ ] 🔄 Export to CSV/JSON
* [ ] 📧 Email summaries
* [ ] 🔊 Audio file + Whisper STT
* [ ] 📈 Timeline/topic visualization

---
