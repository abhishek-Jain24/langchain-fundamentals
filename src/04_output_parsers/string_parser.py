import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def main():
    parser = StrOutputParser()
    sample = AIMessage(content="A variable stores a value.")

    # print("Lesson: String output parser")
    # print("Parsed sample:", parser.invoke(sample))

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if not api_key or api_key == "your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")

    # The | operator runs the prompt, then the model, then the parser.
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a patient Python tutor. Answer in one sentence."),
        ("human", "{question}"),
    ])
    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)

    chain = prompt | model | parser
    print("Chain result:", chain.invoke({"question": "What is a variable?"}))

if __name__ == "__main__":
    main()    