from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file
API_KEY = os.getenv("GEMINI_API_KEY")
print("API_KEY =", API_KEY)
