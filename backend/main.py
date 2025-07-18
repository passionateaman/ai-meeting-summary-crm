from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize/")
async def summarize_meeting(transcript: str = Form(...)):
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")
        prompt = (
            "You are a CRM assistant.\n"
            "Summarize this meeting transcript and extract:\n"
            "- Client pain points\n"
            "- Objections and resolutions\n"
            "- Action items / next steps\n\n"
            f"{transcript}"
        )

        headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "CRM Note Generator",
            "Content-Type": "application/json",
        }

        data = {
            "model": "mistralai/mistral-7b-instruct",  # You can change to claude/haiku or others
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        res_json = response.json()

        return {
            "summary": res_json["choices"][0]["message"]["content"]
        }

    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}
