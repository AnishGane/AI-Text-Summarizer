from src.llm import test_connection, list_available_models

if __name__ == "__main__":
    list_available_models()
    print(test_connection())
    
