from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import logging


def has_booking_started(url: str) -> bool:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(0.5)
    driver.get(url)
    try:
        if driver.find_elements(By.XPATH, '//button[@data-name="get-tickets"]'):
            logging.info("Ticket booking has started")
            return True
        else:
            logging.info("Ticket booking hasn't started yet")
            return False
    except NoSuchElementException:
        logging.info("Ticket booking hasn't started yet")
        return False
    finally:
        driver.close()
