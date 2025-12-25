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
    output_file = Path("../output/playwright_tests.spec.ts")
    output_file.write_text(generate_playwright_tests(), encoding="utf-8")
    print("Playwright test skeleton generated.")
