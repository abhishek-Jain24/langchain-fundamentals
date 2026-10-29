import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def main():
    system_message = SystemMessage(
        content="You are a patient Python tutor. Answer in one sentence."
    )
    human_message = HumanMessage(content="What is a variable?")

    print("Lesson: Message types")
    print(system_message.type + ":", system_message.content)
    print(human_message.type + ":", human_message.content)

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if not api_key or api_key == "your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")

    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)
    ai_message = model.invoke([system_message, human_message])
    print(ai_message.type + ":", ai_message.content)


if __name__ == "__main__":
    main()