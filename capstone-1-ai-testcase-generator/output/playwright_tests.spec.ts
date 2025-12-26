
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
