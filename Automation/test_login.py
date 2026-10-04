from playwright.sync_api import Page, expect


def test_valid_login(page: Page):
    page.goto("https://careconnect.example.com/login")

    page.fill("#username", "testuser")
    page.fill("#password", "Password123!")
    page.click("#login-button")

    expect(page).to_have_url("https://careconnect.example.com/dashboard")


def test_invalid_password(page: Page):
    page.goto("https://careconnect.example.com/login")

    page.fill("#username", "testuser")
    page.fill("#password", "WrongPassword")
    page.click("#login-button")

    expect(page.locator("#error-message")).to_have_text(
        "Invalid username or password"
    )
