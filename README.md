# GPT-4 Test Case Generator

Automatically generates complete, ready-to-run Pytest + Selenium test scripts
from plain English feature descriptions using GPT-4o API.

## What It Does
- Takes plain English feature descriptions as input
- Sends them to GPT-4o via GitHub Models API
- Validates generated code with hallucination detection gate
- Saves ready-to-run .py test files automatically

## Tech Stack
Python | GPT-4o API | Pytest | Selenium | GitHub Actions

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Project Structure
- `generator/prompt_builder.py` — builds GPT-4o question
- `generator/gpt_client.py` — calls GPT-4o API
- `generator/code_validator.py` — hallucination detection gate
- `generator/file_writer.py` — saves generated test files
- `sample_inputs/features.json` — your feature descriptions
- `.github/workflows/ci.yml` — GitHub Actions CI/CD

## Setup
Copy `.env.example` to `.env` and add your GitHub token.

## Built By
Mohd Shad Khan | SDET at LTIMindtree | github.com/shadk02
