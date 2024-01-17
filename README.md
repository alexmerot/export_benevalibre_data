## Export data from the *Bénévalibre* web app to an Excel file

### Requirements

- Python version: ≥ 3.12
- pipenv version: ≥ 2023-11-15
- At least Windows 10 with Powershell
- An account on the [Bénévalibre](https://app.benevalibre.org) web app.
- A `.env` file in the root project directory with the environment variables `ID_ASSOCIATION`, `MAIL` and `PASSWORD`.

> [!note]
> - To get the id of the association:
>   1) In the [board](https://app.benevalibre.org/board/), click on the association.
>   2) Copy the id in the URL of the page after `/association/`.
>
>   Ex: in `https://app.benevalibre.org/association/1234/`, the id is "1234".
> - Example of the `.env` file:
>   ```
>   MAIL="elliot.alderson@association.org"
>   PASSWORD="strong password"
>   ID_ASSOCIATION="1234"
>   ```

### Setup to build from source and for development

1) Clone or download the private Github repo <https://github.com/alexmerot/extraction_benevalibre>.
2) Install the packages with `pipenv`:
    ```
    $Env:PLAYWRIGHT_BROWSERS_PATH='0'; pipenv install
    ```
3) Launch a subshell in virtual environment with `pipenv shell`.
4) Installing firefox browser for Playwright:
    ```
    $Env:PLAYWRIGHT_BROWSERS_PATH='0'; playwright install firefox
    ```
5) Run the Pyinstaller command:
    ```
    pyinstaller export_data.py
    ```

### Usage

1) Double-click the `export_data.exe` file in `.\dist\export_data\`.
2) Select the folder where to download the Excel file.
3) Wait, the Excel file will be downloaded.
