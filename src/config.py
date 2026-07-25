from dotenv import load_dotenv
import os

# Load env variables from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME="gemini-3.6-flash"

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing. Please check your .env file.")

MAX_OUTPUT_TOKENS = 512
TEMPERATURE = 0.3

MIN_INPUT_LENGTH = 10
MAX_INPUT_LENGTH = 50_000