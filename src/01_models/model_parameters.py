import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from langchain_openai import ChatOpenAI

def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip()

    if not api_key or api_key=="your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing...add it to your .env")

    question = [HumanMessage(content="Explain a python list in short.")]

    focused = ChatOpenAI(model=model_name, api_key=api_key, temperature=0, max_tokens=50)
    creative = ChatOpenAI(model=model_name, api_key=api_key, temperature=0.9, max_tokens=50)

    print("temperature=0, max_tokens=50")
    print(focused.invoke(question).content)

    print("temperature=0.9, max_tokens=50")
    print(creative.invoke(question).content)


if __name__=="__main__":
    main()    