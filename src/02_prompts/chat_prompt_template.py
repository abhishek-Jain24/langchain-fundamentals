import os
import sys

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def main():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a patient Python tutor. Answer in one sentence."),
        ("human", "Explain: {topic}"),
    ])

    messages = prompt.format_messages(topic = "lambda function")

    # for message in messages:
    #     print(message.type + ":", message.content)

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if not api_key or api_key == "your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")

    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)
    response = model.invoke(messages)
    print("Answer:", response.content)    


if __name__ == "__main__":
    main()        