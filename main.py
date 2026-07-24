# from src.llm import test_connection, list_available_models
from src.summarizer import summarize_text

sample_text = """
Artificial Intelligence is transforming healthcare by improving
medical diagnosis, drug discovery, patient monitoring,
and personalized treatment.
"""

if __name__ == "__main__":
    # list_available_models()
    # print(test_connection())
    
    summary = summarize_text(sample_text)
    print("\n Generated Summary:\n")
    print(summary)
