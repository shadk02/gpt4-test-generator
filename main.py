import json
import sys
from generator.prompt_builder import build_prompt
from generator.gpt_client     import generate_test_script
from generator.code_validator  import validate_generated_code
from generator.file_writer     import save_test_file
from config                    import BASE_URL, OUTPUT_DIR
from utils.logger              import get_logger

log = get_logger("Main")


def generate_for_feature(name: str, description: str):

    log.info(f"Starting generation for: {name}")

    prompt = build_prompt(description, BASE_URL)
    log.info("Prompt built successfully")

    code = generate_test_script(prompt)

    validation_result = validate_generated_code(code)
    print(validation_result.summary())

    if not validation_result.passed:
        log.error(f"Not saving '{name}' — validation failed")
        return None

    filepath = save_test_file(code, name, OUTPUT_DIR)
    log.info(f"Done! File saved: {filepath}")
    return filepath


def main():

    log.info("GPT-4 Test Generator started")

    with open("sample_inputs/features.json", "r") as f:
        features = json.load(f)

    log.info(f"Found {len(features)} feature(s) to generate tests for")

    results = []

    for feature in features:
        filepath = generate_for_feature(
            name        = feature["name"],
            description = feature["description"]
        )
        results.append({
            "name":     feature["name"],
            "filepath": filepath
        })

    print("\n" + "=" * 50)
    print("GENERATION COMPLETE — SUMMARY")
    print("=" * 50)

    for r in results:
        if r["filepath"]:
            print(f"  ✅  {r['name']}")
            print(f"       → {r['filepath']}")
        else:
            print(f"  ❌  {r['name']} — FAILED validation")

    print("=" * 50)


if __name__ == "__main__":
    main()