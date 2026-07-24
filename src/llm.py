from google import genai
from src.config import GOOGLE_API_KEY, MODEL_NAME

client = genai.Client(api_key=GOOGLE_API_KEY)

def list_available_models():
    for model in client.models.list():
        print(model.name)

def test_connection():
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Say 'Hello, Anish! Your Gemini API is working.'"
    )
    
    return response.text