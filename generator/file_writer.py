import os
from datetime import datetime
from utils.logger import get_logger

log = get_logger("FileWriter")


def save_test_file(code: str, feature_name: str, output_dir: str = "generated_tests") -> str:

    os.makedirs(output_dir, exist_ok=True)

    clean_name = feature_name.lower().replace(" ", "_")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"test_{clean_name}_{timestamp}.py"

    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    log.info(f"File saved: {filepath}")
    return filepath