## Export data from the *Bénévalibre* web app to an Excel file

### Requirements

- Python version: ≥ 3.12
- pipenv version: ≥ 2023-11-15
- At least Windows 10 with Powershell
- An account on the [Bénévalibre](https://app.benevalibre.org) web app.
- An `.env` file in the root project directory with the environment variables `ID_ASSOCIATION`, `MAIL` and `PASSWORD`.

> [!note]
> - To get the ID of the association:
>   1) In [board](https://app.benevalibre.org/board/), click on the association you want.
>   2) Copy the ID in the URL of the page after `/association/`.
>
>   Ex: in `https://app.benevalibre.org/association/1234/`, the ID is "1234".
> - Example of an `.env` file:
>   ```
>   MAIL="elliot.alderson@association.org"
>   PASSWORD="strong password"
>   ID_ASSOCIATION="1234"
>   ```

### Setup for development or to build from source

1) Clone or download the Github repo <https://github.com/alexmerot/extraction_benevalibre>.
2) Install the packages with `pipenv`:
    ```
    $Env:PLAYWRIGHT_BROWSERS_PATH='0'; pipenv install
    ```
3) Launch a subshell in virtual environment with `pipenv shell`.
4) Install firefox browser for Playwright:
    ```
    $Env:PLAYWRIGHT_BROWSERS_PATH='0'; playwright install firefox
    ```
5) Run the Pyinstaller command:
    ```
    pyinstaller export_data.py
    ```

> [!note]
> Setting the environment variable `PLAYWRIGHT_BROWSERS_PATH` to 0 enables to
> download browsers under the `site-packages/playwright` folder. It is necessary
> for the executable file created by Pyinstaller to work.

### Usage

1) Double-click the `export_data.exe` file in `.\dist\export_data\`.
2) Wait for file explorer to launch, then select the folder where to download the Excel file.
3) Wait, the Excel file will be downloaded.
