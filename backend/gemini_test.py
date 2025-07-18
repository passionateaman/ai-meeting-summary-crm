import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads your GOOGLE_API_KEY from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Say hello like a friendly robot.")
    print("✅ Gemini Response:", response.text)
except Exception as e:
    print("❌ Gemini Error:", e)
