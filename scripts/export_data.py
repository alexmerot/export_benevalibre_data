from playwright.async_api import async_playwright
import asyncio

import tkinter
from tkinter import filedialog

import pandas as pd
from datetime import date

import os
from dotenv import load_dotenv, find_dotenv

async def download_data(folder_path, mail, password, id_association):
    """Télécharge au format JSON la table des bénévolats depuis Bénévalibre."""

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
                await page.goto(f"https://app.benevalibre.org/associations/{id_association}/benevalo/?_export=json")
            except:
                pass
        
        download = await download_info.value
        await download.save_as(f"{folder_path}/{today}/benevalibre_{today}.json")

        await browser.close()


async def export_data():
    """Exporte et converti en Excel les données des bénévolats de Bénévalibre."""

    load_dotenv(find_dotenv(raise_error_if_not_found=True))
    MAIL = os.environ.get("MAIL")
    PASSWORD = os.environ.get("PASSWORD")
    ID_ASSOCIATION = os.environ.get("ID_ASSOCIATION")

    tkinter.Tk().withdraw()
    folder_path = filedialog.askdirectory()

    today = date.isoformat(date.today())
    file = f"{folder_path}/{today}/benevalibre_{today}.json"

    os.system("cls")

    print(f'The Excel file will be downloaded in the folder "{folder_path}/{today}/".')
    print("Loading, please wait...")

    await download_data(folder_path, MAIL, PASSWORD, ID_ASSOCIATION)
    df = pd.read_json(file)

    df.to_excel(f"{folder_path}/{today}/benevalibre_{today}.xlsx", index=False)

    os.remove(f"{folder_path}/{today}/benevalibre_{today}.json")

if __name__ == '__main__':
    print("Loading, please wait...")
    asyncio.run(export_data())
