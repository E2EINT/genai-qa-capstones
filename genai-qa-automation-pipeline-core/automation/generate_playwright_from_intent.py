from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]

INTENT_FILE = PROJECT_ROOT / "intents" / "test_intent.json"
OUTPUT_FILE = PROJECT_ROOT / "playwright" / "tests" / "generated.spec.ts"

def generate_playwright_tests():
    if not INTENT_FILE.exists():
        print("❌ test_intent.json not found")
        return

    intent = json.loads(INTENT_FILE.read_text())

    lines = []
    lines.append("import { test, expect } from '@playwright/test';\n")

    base_url = intent.get("base_url", "")

    for test_case in intent.get("tests", []):
        lines.append(f"test('{test_case['name']}', async ({{ page }}) => {{")

        for step in test_case.get("steps", []):
            action = step["action"]

            if action == "navigate":
                lines.append(f"  await page.goto('{base_url}{step['value']}');")

            elif action == "fill":
                lines.append(
                    f"  await page.fill('{step['selector']}', '{step['value']}');"
                )

            elif action == "click":
                lines.append(
                    f"  await page.click('{step['selector']}');"
                )

            elif action == "assert_url_contains":
                lines.append(
                    f"  await expect(page).toHaveURL(/" + step["value"] + "/);"
                )

            elif action == "assert_text_visible":
                lines.append(
                    f"  await expect(page.locator('{step['selector']}')).toContainText('{step['value']}');"
                )

        lines.append("});\n")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("✅ generated.spec.ts created successfully")

if __name__ == "__main__":
    generate_playwright_tests()