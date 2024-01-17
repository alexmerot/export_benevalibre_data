from playwright.async_api import async_playwright
import asyncio

import tkinter
from tkinter import filedialog

import pandas as pd
from datetime import date

import os
from dotenv import load_dotenv, find_dotenv
import sys

async def export_data(folder_path: str, mail: str, password: str, id_organisation: str) -> None:
    """Download the data of all volunteer actions from Bénévalibre.

    The data of volunteer actions are exported from Bénévalibre
    (https://app.benevalibre.org/) to a JSON file, then it is converted to an
    Excel file.

    :param folder_path: Output folder path.
    :type folder_path: str
    :param mail: Email to login to Bénévalibre.
    :type mail: str
    :param password: Password to login to Bénévalibre.
    :type password: str
    :param id_organisation: Bénévalibre ID of the organisation.
    :type id_organisation: str

    """

    # Create the output folder.
    today = date.isoformat(date.today())
    if not os.path.exists(f"{folder_path}/{today}"):
        os.makedirs(f"{folder_path}/{today}")

    file = f"{folder_path}/{today}/benevalibre_{today}"

    print(f'The Excel file will be downloaded in the folder "{folder_path}/{today}/".')
    print("Loading, please wait...")

    # Go to the Bénévalibre web app then download the data.
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
                await page.goto(f"https://app.benevalibre.org/associations/{id_organisation}/benevalo/?_export=json")
            except:
                pass
        
        download = await download_info.value
        await download.save_as(f"{file}.json")

        await browser.close()
    
    # Import the JSON file then convert it to an Excel file.
    data = pd.read_json(f"{file}.json")
    data.to_excel(f"{file}.xlsx", index=False)
    os.remove(f"{file}.json")

def get_inputs() -> list:
    """Get credentials from the ``.env`` file and the output folder path from user input.


    :returns: The output folder path, the email, the password ans the organisation ID.

    :rtype: list

    """

    load_dotenv(find_dotenv(raise_error_if_not_found=True))

    MAIL = os.environ.get("MAIL")
    PASSWORD = os.environ.get("PASSWORD")
    ID_ORGANISATION = os.environ.get("ID_ORGANISATION")

    tkinter.Tk().withdraw()
    folder_path = filedialog.askdirectory(title="Select output folder")

    os.system("cls")

    if folder_path:
        return [folder_path, MAIL, PASSWORD, ID_ORGANISATION]
    else:
        sys.exit("No folder selected.")

if __name__ == '__main__':
    print("Loading, please wait...")
    print("Please select the folder where to export the Excel file.")

    inputs = get_inputs()

    asyncio.run(export_data(*inputs))
