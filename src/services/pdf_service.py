from io import BytesIO
from pypdf import PdfReader
from src.exceptions import PDFExtractionError
from src.logger import logger

def extract_text_from_pdf(file) -> str:
    """
    Extract the text from the uploaded pdf
    """
    
    try:
        reader = PdfReader(BytesIO(file.read()))
        
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            
            if page_text:
                text += page_text + "\n"
                
        logger.info("PDF text extracted successfully.")
        
        return text.strip()

    except Exception as e:
        logger.exception("Failed to extract PDF text.")
        raise PDFExtractionError(
            "Unable to extract text from the uploaded PDF."
        ) from e