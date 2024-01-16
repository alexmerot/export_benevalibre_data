from playwright.async_api import async_playwright
import asyncio
from datetime import date
import os

async def download_data(folder_path, mail, password):
    """Télécharge au format JSON la table des bénévolats sur Bénévalibre."""

    today = date.isoformat(date.today())
    if not os.path.exists(f"{folder_path}/{today}"):
        os.makedirs(f"{folder_path}/{today}")

    async with async_playwright() as p:
        print("Launching browser...")

        browser = await p.firefox.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0")
        page = await context.new_page()

        print("Going to the Bénévalibre web app to login...")
        await page.goto('https://app.benevalibre.org/account/login/')
        await page.wait_for_timeout(100)

        await page.get_by_label("Adresse mail").fill(mail)
        await page.get_by_label("Mot de passe").fill(password)
        await page.get_by_role("button", name="Se connecter").click()

        print("Successful login. Download is starting...")

        async with page.expect_download() as download_info:
            try:
                await page.goto("https://app.benevalibre.org/associations/1236/benevalo/?_export=json")
            except:
                pass
        
        download = await download_info.value
        await download.save_as(f"{folder_path}/{today}/benevalibre_{today}.json")

        await browser.close()

async def main():
    await download_data()
    if os.path.exists(f"./output/{date.isoformat(date.today())}"):
        print("Successful download")
    else:
        print("Error")

if __name__ == '__main__':
    asyncio.run(main())
