from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    open_ai_key = os.getenv("OPEN_AI_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")

    print("Hello from langchain-course!")
    print(f"OpenAI Key: {open_ai_key}")
    print(f"Google API Key: {google_api_key}")


if __name__ == "__main__":
    main()
