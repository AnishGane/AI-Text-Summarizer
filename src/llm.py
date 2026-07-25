from google import genai
from google.genai import errors
from src.config import (
    GOOGLE_API_KEY, 
    MODEL_NAME, 
    TEMPERATURE, 
    MAX_OUTPUT_TOKENS)
from src.exceptions import GeminiAPIError

client = genai.Client(api_key=GOOGLE_API_KEY)

# List available models name from the Google GenAI API
def list_available_models():
    for model in client.models.list():
        print(model.name)

# Test the connection with the Google GenAI API by sending a simple prompt and if it returns a response then the connection is working properly
def test_connection():
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Say 'Hello, Anish! Your Gemini API is working.'"
    )
    
    return response.text

# Generate response from the Google GenAI API based on the prompt provided by the user
def generate_response(prompt: str)->str:
    """Send the prompt to Gemini and return the generated response text"""

    try:
        response = client.model.generate_content(
            model = MODEL_NAME,
            contents = prompt,
            config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_OUTPUT_TOKENS
            }
        )
        
        return response.text
    
    except errors.ClientError as e:
        raise GeminiAPIError(f"Gemini API error: {e}") from e
    
    except Exception as e:
        raise GeminiAPIError(f"An error occurred: {e}") from e
    
    return response.text