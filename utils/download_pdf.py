from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import logger


def download_file(url: str, dir: str) -> bool:
    """
    Download file from URL

    Args:
        url (str): Link to the file
        dir (str): path of the destination directory
    """

    try:
        chrome_options = webdriver.ChromeOptions()

        # preferences required to download file
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
        
        # fetching download button to click
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, r"/html/body/pdf-viewer/viewer-toolbar/div/div[3]/viewer-download-controls/cr-icon-button"))).click()
        logger.log_message(
                        message='File downladed successfully', level=0)
        driver.close()
    except Exception as e:
        logger.log_message(
                            message='Exception while downloading file: ' + str(e.args), level=1)