from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.common.by import By
import time


class TextIdentification(object):

    def identification(self):
        url = "https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have"
        chrome_options = Options();
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)

        # text identification

        try:
            textCheck = driver.find_element(By.XPATH,     '//div[@class="judgment judgment-good"]');
            versionCheck = driver.find_element(By.XPATH, "//div[@id='detected_value']/u");
            consentBtn = driver.find_element(By.XPATH, "//button[@aria-label='Consent']")
            versionShown = driver.find_element(By.XPATH, '//div[@class="content-block-main"]/p/b')
        except NoSuchElementException:
            print('element identification textCheck/versionCheck or consentBtn not successfull')
        if textCheck:
            print('Chrome version has been checked')
        if versionShown:
            print('Chrome version has been shown and is '+ versionShown.text)
        if consentBtn:
            consentBtn.click()


        time.sleep(3)
        driver.quit()

TextIdentification().identification()


