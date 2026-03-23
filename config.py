import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN   = os.getenv("GITHUB_TOKEN")
GPT_MODEL      = "gpt-4o"
MAX_TOKENS     = 2000
TEMPERATURE    = 0.2
BASE_URL       = "https://the-internet.herokuapp.com"
OUTPUT_DIR     = "generated_tests"