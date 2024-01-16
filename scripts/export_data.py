from datetime import date
import asyncio
import pandas as pd
import tkinter
from tkinter import filedialog
from download_data import download_data
import os
from dotenv import load_dotenv, find_dotenv

async def export_data():
    """Exporte en CSV les données des bénévolats de Bénévalibre."""

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
