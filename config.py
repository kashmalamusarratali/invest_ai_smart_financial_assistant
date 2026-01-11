import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("Gemini_API_KEY")

MODEL_CHAT = "gemini-2.5-flash"
MODEL_TTS = "gemini-2.5-flash-preview-tts"

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

DB_PATH = "investai.db"
