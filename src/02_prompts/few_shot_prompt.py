import os
import sys

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

def main():

    my_examples = [
        {"word": "happy", "description": "a smiling face"},
        {"word": "sad", "description": "a frowning face"},
        {"word": "tired", "description": "a yawing face"},
    ]

    my_example_prompt = ChatPromptTemplate.from_messages([
        ("human", "{word}"),
        ("ai", "{description}"),
    ])

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt = my_example_prompt,
        examples = my_examples,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Describe one feeling as a face. Follow the examples: "),
        few_shot_prompt,
        ("human", "{word}"),
    ])

    word = "surprised"
    messages = prompt.format_messages(word=word)

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
    