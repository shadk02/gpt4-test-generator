import openai
from config import GITHUB_TOKEN, GPT_MODEL, MAX_TOKENS, TEMPERATURE
from utils.logger import get_logger

log = get_logger("GPTClient")


def generate_test_script(prompt: str) -> str:

    log.info("Calling GPT-4o via GitHub... please wait 5-10 seconds")

    try:
        client = openai.OpenAI(
            api_key  = GITHUB_TOKEN,
            base_url = "https://models.inference.ai.azure.com"
        )

        response = client.chat.completions.create(
            model    = GPT_MODEL,
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a senior SDET. "
                        "Generate clean, production-ready Pytest + Selenium code. "
                        "Output raw Python only — no markdown, no backticks."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens  = MAX_TOKENS,
            temperature = TEMPERATURE
        )

        code = response.choices[0].message.content.strip()

        if code.startswith("```"):
            lines = code.split("\n")
            code  = "\n".join(lines[1:-1])

        log.info(f"GPT-4o finished — generated {len(code.splitlines())} lines of code")
        return code

    except openai.AuthenticationError:
        log.error("GitHub token is wrong — check your .env file")
        raise

    except openai.RateLimitError:
        log.error("Rate limit — wait 60 seconds and try again")
        raise

    except Exception as e:
        log.error(f"Something went wrong: {e}")
        raise