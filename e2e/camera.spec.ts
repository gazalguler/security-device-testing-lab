import { test, expect } from "@playwright/test";

test("camera dashboard loads status from API", async ({ page }) => {
    const apiResponse = page.waitForResponse(
        response =>
            response.url().endsWith("/camera/status") &&
            response.request().method() === "GET"
    );

    await page.goto("http://127.0.0.1:5500");

    const response = await apiResponse;

    expect(response.status()).toBe(200);
    expect(await response.json()).toEqual({
        camera_id: "CAM-001",
        status: "online"
    });

    await expect(
        page.getByRole("heading", { name: "Security Camera Dashboard" })
    ).toBeVisible();

    await expect(
        page.locator("#camera-status")
    ).toHaveText("Online");
});

test("dashboard displays error when camera API is unavailable", async ({ page }) => {
    await page.route("**/camera/status", async route => {
        await route.abort("failed");
    });

    await page.goto("http://127.0.0.1:5500");

    await expect(
        page.locator("#camera-status")
    ).toHaveText("Error");
});
