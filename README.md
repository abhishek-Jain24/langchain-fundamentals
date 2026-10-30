# LangChain Fundamentals

A small, beginner-friendly Python project for a  GenAI . Each lesson is one script. The scripts introduce chat models, prompts, structured output, output parsers, messages, conversation memory, chains, and runnables. The last two scripts are a tiny learning assistant.

The lessons use current LangChain APIs from `langchain-core` and `langchain-openai`. Conversation history is kept in a normal Python list and passed into a chain with `MessagesPlaceholder`. That list lives only in the running program. It is not stored in a database, and it is gone when the program exits.

LangChain 1.7 deprecates `RunnableWithMessageHistory` and `InMemoryChatMessageHistory`. These lessons do not use those helpers. The history list stays visible in the script so each turn is easy to explain.

## Prerequisites

- Windows PowerShell, or a macOS/Linux terminal
- Python 3.11 or newer. This project was checked with Python 3.12.
- An OpenAI API key only if you want live model replies

Model access depends on your OpenAI account. `.env.example` uses `gpt-4.1-mini`. That model id still works, and OpenAI has announced its shutdown for January 14, 2027. You can put another chat model your account can access in `OPENAI_MODEL`. The temperature lesson expects a model that accepts `temperature`. Some reasoning models do not.

## Project layout

```text
langchain-fundamentals/
├── src/
│   ├── lesson_setup/          Shared API-key check and offline practice model
│   ├── 01_models/
│   ├── 02_prompts/
│   ├── 03_structured_output/
│   ├── 04_output_parsers/
│   ├── 05_messages/
│   ├── 06_memory/
│   ├── 07_chains/
│   ├── 08_runnables/
│   └── 09_mini_project/
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

Suggested class order: models, prompts, structured output, output parsers, messages, memory, chains, runnables, then the mini project.

Structured output asks the model provider for specific fields. Output parsers read text the model has already written. The lessons keep those two ideas separate.

## 1. Create and activate a virtual environment

Open PowerShell in the `langchain-fundamentals` folder.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, allow it for the current window and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

From the project root, with the virtual environment active:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` installs LangChain, Pydantic, python-dotenv, and pytest. The last line installs this project's small `lesson_setup` helper so every lesson can import it.

## 3. Configure the API key

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace `your_openai_api_key_here` with your real key. Leave `OPENAI_MODEL=gpt-4.1-mini`, or change it to a model your account can call.

macOS/Linux: `cp .env.example .env`

Do not commit `.env`. It is listed in `.gitignore`.

Anthropic and Google keys are optional. They are documented in `.env.example` and printed by `src/01_models/multiple_providers.py`. The lessons do not install or call those providers.

### Offline practice

Every model lesson can run with no key and no API charge:

```powershell
$env:TUTORIAL_OFFLINE = "1"
python src/01_models/openai_chat_model.py
```

macOS/Linux: `export TUTORIAL_OFFLINE=1`

Offline mode uses a fake chat model with the fixed replies shown in each script. Live replies will not match that wording exactly. Turn offline mode off before a live demonstration:

```powershell
Remove-Item Env:TUTORIAL_OFFLINE
```

## 4. Run a lesson

Run commands from the project root. This is the command shape for every script:

```powershell
python src/01_models/openai_chat_model.py
```

### Models

```powershell
python src/01_models/openai_chat_model.py
python src/01_models/model_parameters.py
python src/01_models/multiple_providers.py
```

### Prompts

```powershell
python src/02_prompts/prompt_template.py
python src/02_prompts/chat_prompt_template.py
python src/02_prompts/few_shot_prompt.py
```

`PromptTemplate` fills one string. `ChatPromptTemplate` builds system and human messages.

### Structured output

```powershell
python src/03_structured_output/with_pydantic.py
python src/03_structured_output/with_json_schema.py
```

### Output parsers

```powershell
python src/04_output_parsers/string_parser.py
python src/04_output_parsers/json_parser.py
python src/04_output_parsers/pydantic_parser.py
```

### Messages and memory

```powershell
python src/05_messages/message_types.py
python src/05_messages/message_history.py
python src/06_memory/conversation_without_history.py
python src/06_memory/conversation_with_history.py
python src/06_memory/session_based_memory.py
```

`message_history.py` does not call a model. The memory scripts keep history in Python lists. Two session ids in `session_based_memory.py` do not share messages.

### Chains

```powershell
python src/07_chains/simple_chain.py
python src/07_chains/sequential_processing.py
python src/07_chains/chain_with_output_parser.py
```

Chains use the `|` operator. They do not use the older `LLMChain` class.

### Runnables

```powershell
python src/08_runnables/runnable_sequence.py
python src/08_runnables/runnable_parallel.py
python src/08_runnables/runnable_lambda.py
```

`runnable_parallel.py` and `runnable_lambda.py` do not call a model. Their input and output are fixed.

### Mini project

```powershell
python src/09_mini_project/learning_assistant.py
python src/09_mini_project/learning_assistant_with_memory.py
```

## 5. Run the offline tests

From the project root:

```powershell
python -m pytest
```

The default suite does not call OpenAI. It checks prompt formatting, parser validation, runnable results, history, session separation, and it runs every lesson script in offline mode.

## 6. Optional live API check

This makes one small paid call. Use it only after `.env` contains a real key and your account can access `OPENAI_MODEL`.

```powershell
$env:RUN_LIVE_API_TESTS = "1"
python -m pytest -m live
```

macOS/Linux: `RUN_LIVE_API_TESTS=1 python -m pytest -m live`

If the variable is unset, or the key is missing, the live test is skipped. `python -m pytest` without the variable does not run the paid call.

## Troubleshooting

**`OPENAI_API_KEY is missing`**

Copy `.env.example` to `.env`, add a real key, and run the command from the project root. For a free practice run, set `TUTORIAL_OFFLINE` to `1`.

**The key is rejected or the model is unavailable**

Check the key in the OpenAI dashboard. If the model name is not enabled for the account, change `OPENAI_MODEL` in `.env`. If a model reports that `temperature` is unsupported, use a chat model that accepts temperature for `model_parameters.py`.

**`No module named 'lesson_setup'`**

Install from the project root again:

```powershell
pip install -r requirements.txt
```

The install includes the local helper. Do not set `PYTHONPATH` by hand.

**`No module named 'src'`**

Run the script path:

```powershell
python src/01_models/openai_chat_model.py
```

Do not run `python -m src.01_models...`. Folder names that start with numbers are not Python packages.

**Dependency install errors**

Create a new virtual environment with Python 3.11 or newer and install `requirements.txt` again. Do not mix these packages with an older global LangChain install in the same environment.
