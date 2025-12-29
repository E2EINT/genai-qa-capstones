import { test, expect } from '@playwright/test';

test('Invalid Email Format', async ({ page }) => {
  await page.fill('#username', 'invalid_email');
  await page.fill('#password', 'Password123');
});

test('No Password Input', async ({ page }) => {
  await page.fill('#username', 'student');
});

test('Common Password', async ({ page }) => {
  await page.fill('#username', 'student');
  await page.fill('#password', 'Password123');
});

test('Sequential Characters', async ({ page }) => {
  await page.fill('#username', 'abc123');
  await page.fill('#password', 'Password123');
});

test('Character Requirements', async ({ page }) => {
  await page.fill('#username', 'abc');
});

test('No Username Input', async ({ page }) => {
  await page.fill('#password', 'Password123');
});

test('Invalid Password Format', async ({ page }) => {
  await page.fill('#username', 'student');
  await page.fill('#password', 'abc');
});
