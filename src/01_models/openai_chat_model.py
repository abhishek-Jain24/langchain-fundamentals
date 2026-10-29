import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip()

    if not api_key or api_key=="your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing...add it to your .env")

    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)

    msg = [
        SystemMessage(content = "You are a patient Python tutor. Answer in one short sentence."),
        HumanMessage(content = "What is a variable in Python?")
    ]
    response = model.invoke(msg)

    print(f"Model: {model_name}") 
    print(f"Answer: {response.content}")

if __name__=="__main__":
    main()