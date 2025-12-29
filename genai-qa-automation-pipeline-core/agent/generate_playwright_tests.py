from pathlib import Path

def generate_playwright_tests() -> str:
    return """
import { test, expect } from '@playwright/test';

test('Valid Login', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.fill('#username', 'validUser');
  await page.fill('#password', 'validPassword');
  await page.click('#login');
  await expect(page).toHaveURL(/dashboard/);
});

test('Invalid Password', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.fill('#username', 'validUser');
  await page.fill('#password', 'invalidPassword');
  await page.click('#login');
  await expect(page.locator('.error')).toBeVisible();
});
"""


if __name__ == "__main__":
    # Resolve paths relative to THIS file (robust)
    BASE_DIR = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = BASE_DIR / "output"

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "playwright_tests.spec.ts"
    output_file.write_text(generate_playwright_tests(), encoding="utf-8")

    print("✅ Playwright test skeleton generated successfully.")
    print(f"📝 Output: {output_file}")