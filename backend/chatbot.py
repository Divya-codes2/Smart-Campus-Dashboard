import os
from dotenv import load_dotenv


import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def ask_gemini(question: str) -> str:
    response = model.generate_content(question)
    return response.text
