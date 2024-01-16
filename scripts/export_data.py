from datetime import date
import asyncio
import pandas as pd
import tkinter
from tkinter import filedialog
from download_data import download_data
import os

async def export_data():
    """Exporte en CSV les données des bénévolats de Bénévalibre."""

    print("Loading, please wait...")
    
    tkinter.Tk().withdraw()
    folder_path = filedialog.askdirectory()

    today = date.isoformat(date.today())
    file = f"{folder_path}/{today}/benevalibre_{today}.json"

    os.system("cls")

    print(f'The Excel file will be downloaded in the folder "{folder_path}/{today}/".')
    print("Loading, please wait...")

    await download_data(folder_path)
    df = pd.read_json(file)

    df.to_excel(f"{folder_path}/{today}/benevalibre_{today}.xlsx", index=False)

    os.remove(f"{folder_path}/{today}/benevalibre_{today}.json")

if __name__ == '__main__':
    asyncio.run(export_data())
