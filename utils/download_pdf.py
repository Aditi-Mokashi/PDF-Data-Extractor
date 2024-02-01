from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import logger


def download_file(url: str, dir: str) -> bool:
    # TODO: Remove nested try-except blocks
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {
            'plugins.always_open_pdf_externally': True,
            "directory_upgrade": True,
            "safebrowsing.enabled": False,
            "download.default_directory": dir
        })

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        logger.log_message(
                            message='URL fetched successfully', level=0)
        try:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                (By.XPATH, r"/html/body/pdf-viewer/viewer-toolbar/div/div[3]/viewer-download-controls/cr-icon-button"))).click()
            logger.log_message(
                            message='File downladed successfully', level=0)
        except Exception as e:
            logger.log_message(
                            message='File not downloaded: ' + str(e.args), level=1)
        driver.close()
        return True
    except:
        return False
