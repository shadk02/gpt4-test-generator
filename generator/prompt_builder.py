def build_prompt(feature_description: str, base_url: str) -> str:
    return f"""
You are an expert SDET. Generate a complete, runnable Python test script
using Pytest and Selenium WebDriver for the feature described below.

RULES YOU MUST FOLLOW:
1. Use Page Object Model - page class and test class in same file
2. Use explicit waits - WebDriverWait - NEVER use time.sleep()
3. Use By.ID, By.CSS_SELECTOR, or By.XPATH for locators
4. Include: valid scenario, invalid scenario, and 2 edge cases
5. Add a pytest fixture for browser setup and teardown using yield
6. Add assertions with clear failure messages
7. Output ONLY raw Python code - NO markdown, NO backticks, NO explanation
8. Put all imports at the top
9. The website base URL is: {base_url}

FEATURE TO TEST:
{feature_description}

Write the complete test script now:
"""