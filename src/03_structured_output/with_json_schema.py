import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def main():

    schema = {
        "title": "GlossaryEntry",
        "description": "One programming term explained for beginner.",
        "type": "object",
        "properties": {
            "term": {"type": "string", "description": "The programming term"},
            "definition": {"type": "string", "description": "A one-sentence definition"},
        },
        "required": ["term", "definition"],
    }

    
    print("Lesson: Structured output with a JSON schema")
    print("Required fields:", schema["required"])

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if not api_key or api_key == "your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")

    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)
    
    structured_model = model.with_structured_output(schema)
    entry = structured_model.invoke("Define the term list for a beginner.")

    print("Result type:", type(entry).__name__)
    print("term:", entry["term"])
    print("definition:", entry["definition"])


if __name__ == "__main__":
    main()