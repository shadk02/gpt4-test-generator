import ast
import re
from utils.logger import get_logger

log = get_logger("Validator")

REQUIRED_PATTERNS = [
    r"def test_",
    r"WebDriverWait",
    r"assert ",
    r"driver\.quit\(\)",
]

FORBIDDEN_PATTERNS = [
    r"time\.sleep\(",
    r"find_element_by_",
]


class ValidationResult:
    def __init__(self):
        self.passed   = True
        self.errors   = []
        self.warnings = []

    def add_error(self, msg):
        self.passed = False
        self.errors.append(msg)

    def add_warning(self, msg):
        self.warnings.append(msg)

    def summary(self):
        status = "PASSED ✅" if self.passed else "FAILED ❌"
        lines  = [f"\nValidation Result: {status}"]
        for e in self.errors:
            lines.append(f"  ERROR  : {e}")
        for w in self.warnings:
            lines.append(f"  WARNING: {w}")
        return "\n".join(lines)


def validate_generated_code(code: str) -> ValidationResult:
    result = ValidationResult()
    log.info("Checking generated code for mistakes...")

    try:
        ast.parse(code)
        log.info("✅ Syntax is valid Python")
    except SyntaxError as e:
        result.add_error(f"Syntax error on line {e.lineno}: {e.msg}")
        log.error("❌ Syntax error found")
        return result

    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, code):
            result.add_error(f"Missing required element: '{pattern}'")
            log.error(f"❌ Not found: {pattern}")

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, code):
            result.add_warning(f"Bad practice detected: '{pattern}'")
            log.warning(f"⚠️  Found bad practice: {pattern}")

    if result.passed:
        log.info("✅ All checks passed — safe to save")
    else:
        log.error(f"❌ {len(result.errors)} error(s) found — will NOT save")

    return result