import os
import sys

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

# Change this one word to switch providers.
# The choices are "openai", "google", "anthropic", and "ollama".
PROVIDER = "openai"

QUESTION = "Say hello in one short sentence."


def main():
    load_dotenv()
    provider = PROVIDER.strip().lower()

    print("Lesson: Multiple model providers")
    print("Selected provider:", provider)
    print('To switch, change PROVIDER to "google", "anthropic", or "ollama".')

    # Only the setup changes. Every branch ends with a chat model object.
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        if not api_key or api_key == "your_openai_api_key_here":
            sys.exit("OPENAI_API_KEY is missing. Copy .env.example to .env and add your key.")
        model = ChatOpenAI(model=model_name, api_key=api_key, temperature=0)

    elif provider == "google":
        api_key = os.getenv("GOOGLE_API_KEY", "").strip()
        model_name = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
        if not api_key or api_key == "your_google_api_key_here":
            sys.exit("GOOGLE_API_KEY is missing. Add it to .env, or set PROVIDER back to openai.")
        # Some newer Gemini models reject temperature. Delete temperature=0 if this call fails.
        model = ChatGoogleGenerativeAI(model=model_name, api_key=api_key, temperature=0)

    elif provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY", "").strip()
        model_name = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")
        if not api_key or api_key == "your_anthropic_api_key_here":
            sys.exit("ANTHROPIC_API_KEY is missing. Add it to .env, or set PROVIDER back to openai.")
        model = ChatAnthropic(model=model_name, api_key=api_key, temperature=0)

    elif provider == "ollama":
        model_name = os.getenv("OLLAMA_MODEL", "llama3.2")
        print("Ollama has no API key. The app must be running, and the model must be downloaded:")
        print(f"    ollama pull {model_name}")
        model = ChatOllama(model=model_name, temperature=0)

    else:
        sys.exit('PROVIDER must be "openai", "google", "anthropic", or "ollama".')

    print("Model:", model_name)
    print("Question:", QUESTION)

    # This call is identical for OpenAI, Gemini, Claude, and Ollama.
    try:
        response = model.invoke([HumanMessage(content=QUESTION)])
    except Exception as error:
        sys.exit(
            f"Could not get a response from {provider}.\n"
            f"Check your API key, model name, and provider availability.\n"
            f"Details: {error}"
        )

    print("Answer:", response.content)


if __name__ == "__main__":
    main()
