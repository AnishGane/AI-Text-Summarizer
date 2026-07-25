from google import genai
from google.genai import errors
from src.config import (
    GOOGLE_API_KEY, 
    MODEL_NAME, 
    TEMPERATURE, 
    MAX_OUTPUT_TOKENS)
from src.exceptions import GeminiAPIError
from src.logger import logger
import logging 

logger = logging.getLogger(__name__)

client = genai.Client(api_key=GOOGLE_API_KEY)

# List available models name from the Google GenAI API
def list_available_models():
    logger.info("Listing available models...")

    for model in client.models.list():
        print(model.name)

# Test the connection with the Google GenAI API by sending a simple prompt and if it returns a response then the connection is working properly
def test_connection():
    logger.info("Testing connection with Gemini API...")
    
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents="Say 'Hello, Anish! Your Gemini API is working.'"
        )
    
        logger.info("Received response from Gemini while testing connection.")

        return response.text

    except Exception as e:
        logger.exception("An error occurred while testing connection with Gemini API.")
        raise GeminiAPIError(f"An error occurred while testing connection: {e}") from e

# Generate response from the Google GenAI API based on the prompt provided by the user
def generate_response(prompt: str)->str:
    """Send the prompt to Gemini and return the generated response text"""
    
    logger.info("Sending prompt to Gemini API...")

    try:
        response = client.models.generate_content(
            model = MODEL_NAME,
            contents = prompt,
            config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_OUTPUT_TOKENS
            }
        )
        
        logger.info("Received response from Gemini.")
        
        return response.text
    
    except errors.ClientError as e:
        logger.error("Gemini API request failed.")
        raise GeminiAPIError(f"Gemini API error: {e}") from e
    
    except Exception as e:
        logger.exception("Unexpected error while communicating with Gemini.")
        raise GeminiAPIError(f"An error occurred: {e}") from e