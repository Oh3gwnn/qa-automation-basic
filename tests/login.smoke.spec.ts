import { test } from '@playwright/test';
import { LoginPage } from '../pages/login.page';

test.describe('Login Smoke Test', () => {
  test('S1: valid user can login successfully', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');
    await loginPage.expectLoginSuccess();
  });

  test('S2: invalid user cannot login', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login('standard_user', 'wrong_password');
    await loginPage.expectLoginFailure();
  });
});