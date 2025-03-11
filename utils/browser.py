# from pathlib import Path
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service

# ROOT_DIR = Path(__file__).parent.parent
# CHROMEDRIVER_NAME = "geckodriver"
# CHROMEDRIVER_PATH = ROOT_DIR / "bin" / CHROMEDRIVER_NAME

# chrome_options = webdriver.FirefoxOptions()
# chrome_servise = Service(executable_path=CHROMEDRIVER_PATH)
# browser = webdriver.Firefox(service=chrome_servise, options=chrome_options)

# browser.get("https://www.google.com/")

from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from pathlib import Path
from dotenv import load_dotenv

import os

load_dotenv()

ROOT_DIR = Path(__file__).parent.parent
GECKODRIVER_NAME = "geckodriver"
GECKODRIVER_PATH = ROOT_DIR / "bin" / GECKODRIVER_NAME


def make_firefox_browser(*options):
    firefox_options = webdriver.FirefoxOptions()

    if options is not None:
        for option in options:
            firefox_options.add_argument(option)

    if os.environ.get("SELENIUM_HEADLESS") == "1":
        firefox_options.add_argument("--headless")

    firefox_service = Service(executable_path=str(GECKODRIVER_PATH))
    browser = webdriver.Firefox(service=firefox_service, options=firefox_options)  # noqa

    return browser


if __name__ == '__main__':
    browser = make_firefox_browser('--headless')
    browser.get("https://www.youtube.com/")
    browser.quit()
