from openai import OpenAI
from config import GEMINI_API_KEY, BASE_URL

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)
