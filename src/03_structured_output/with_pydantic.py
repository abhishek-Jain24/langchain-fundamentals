import warnings
warnings.filterwarnings("ignore")

import os
import sys
from typing import Literal

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from pydantic import BaseModel, Field, ValidationError


class StudyNote(BaseModel):
    topic: str = Field(description = "Topic name in a few words.")
    summary: str = Field(description = "ONe sentence a beginner can understand")
    difficulty: Literal["beginner", "intermidiate", "advanced"] = Field(descroption="How hard this is for a new programmer?")


def main():

    # note = StudyNote(
    #     topic = "variables in python",
    #     summary = "A variable stores a value",
    #     difficulty = "beginner",
    # )

    # print(f"Valid note: {note.topic} | {note.difficulty}")

    # try:
    #     StudyNote(
    #     topic = "variables in python",
    #     summary = "A variable stores a value",
    #     difficulty = "expert",
    #     )        
    # except ValidationError:
    #     print("Pydantic rejected an invalid difficulty.")

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if not api_key or api_key == "your_openai_api_key_here":
        sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")

    model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)
    # The provider returns a StudyNote. Read the fields instead of free text.
    structured_model = model.with_structured_output(StudyNote)
    result = structured_model.invoke("Explain a variable for a beginner.")

    print("Result type:", type(result).__name__)
    print("topic:", result.topic)
    print("summary:", result.summary)
    print("difficulty:", result.difficulty)    



if __name__ == "__main__":
    main()    