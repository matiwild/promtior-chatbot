import os
from dotenv import load_dotenv
from google import generativeai as genai

# Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load context document
def load_document(path: str) -> str:
    with open(path, encoding="utf-8") as file:
        return file.read()

DOCUMENT_PATH = os.getenv("DOCUMENT_PATH")
document_text = load_document(DOCUMENT_PATH)


def query_gemini(question: str, model_name="models/gemini-1.5-pro-latest") -> str:
    prompt = f"""Based on the following text, answer the question:
\"\"\"{document_text}\"\"\"
Question: {question.strip()}"""

    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text.strip()
