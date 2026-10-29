import os
import sys

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def main():
    # {topic} is filled in by format(). This step does not call the model.
    prompt = PromptTemplate.from_template("Explain {topic} to a beginner in one sentence.")
    text = prompt.format(topic="a loop")

    print("Lesson: Prompt template")
    print("Formatted prompt:", text)

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if not api_key or api_key == "your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")

    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)
    # A chat model accepts a plain string as one human message.
    response = model.invoke(text)
    print("Answer:", response.content)


if __name__ == "__main__":
    main() 