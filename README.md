## Create an EXE file to download data from the *Bénévalibre* web app 

### Requirements

- Python version: ≥3.12
- pipenv version: ≥2023-11-15
- Windows 10 or more with Powershell
- An account on the [Bénévalibre](https://app.benevalibre.org) web app.
- A `.env` file on the root of the project with the environment variables `ID_ASSOCIATION`, `MAIL` and `PASSWORD`.

> [!note]
> To get the id of the association:
> 1) In the [board](https://app.benevalibre.org/board/), click on the association.
> 2) Copy the id in the URL of the page after `/association/`.
> Ex: in `https://app.benevalibre.org/association/1234/`, the id is "1234".

### Setup

1) Install the packages with `pipenv`:
    ```
    $Env:PLAYWRIGHT_BROWSERS_PATH='0'; pipenv install
    ```
2) Launch a subshell in virtual environment with `pipenv shell`.
3) Installing firefox browser for Playwright:
    ```
    $Env:PLAYWRIGHT_BROWSERS_PATH='0'; playwright install firefox
    ```
4) Run the Pyinstaller command:
    ```
    pyinstaller scripts/export_data.py
    ```

### Usage

1) Double-click the `export_data.exe` file in `.\dist\export_data\`.
2) Select the folder where to download the Excel file.
3) Wait, the Excel file will be downloaded.
