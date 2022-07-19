import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from selenium.webdriver.common.action_chains import ActionChains


class Downloader:
    __sites = []
    __site_id = 0
    path = ""
    delay = 10
    driver = None

    def __init__(self, driver, delay=10, path=""):
        print("created!")
        self.driver = driver
        self.delay = delay
        self.__sites = [
            self.__snaptik,
            self.__ssstik
        ]
        if path == "":
            self.path = os.path.dirname(__file__) + "\\data\\analyzing.mp4"
        else:
            self.path = path

    def dwnld(self, src):
        v_url = ""
        if src.find("www.tiktok.com/") != -1:
            for num in range(len(self.__sites)):
                try:
                    v_url = self.__sites[self.__site_id](src)
                except Exception as e:
                    print(str(e))
                    if self.__site_id < len(self.__sites) - 1:
                        self.__site_id += 1
                    else:
                        self.__site_id = 0
                else:
                    if v_url != "":
                        break
        else:
            v_url = src

        if v_url == "":
            return ""
        v_path = self.__downloading(v_url)
        return v_path # Есть ли в этом смысл?

    def __ssstik(self, src):
        error = None
        self.driver.get('https://ssstik.io/en')
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.ID, "main_page_text")))
        except Exception:
            raise Exception("Registration wasnt loaded")

        search = self.driver.find_element(By.ID, "main_page_text")
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(search).send_keys(src).send_keys(Keys.RETURN).perform()

        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.CLASS_NAME, "pure-button")))
        except TimeoutException:
            try:
                error = self.driver.find_element(By.ID, "alert-error")
            finally:
                if error is not None:
                    raise Exception(error.text)
                raise Exception("Loading took too much time!")
        search = self.driver.find_element(By.CLASS_NAME, "pure-button")
        url = ""
        try:
            url = search.get_attribute('href')
        except Exception:
            url = -1
        finally:
            return url

    def __snaptik(self, src):
        error = None
        url = ""
        self.driver.get("https://snaptik.app/en")
        elem = self.driver.find_element(By.ID, "url")
        elem.send_keys(src)
        elem.send_keys(Keys.RETURN)
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "download-block")))
        except TimeoutException:
            try:
                error = self.driver.find_element(By.ID, "alert-error")
            finally:
                if error is not None:
                    raise Exception(error.text)
                raise Exception("Loading took too much time!")
        elems = self.driver.find_element(By.CLASS_NAME, "download-block").find_elements(By.CLASS_NAME, "abutton")
        error = True
        for elem in elems:
            url = elem.get_attribute("href")
            r = requests.get(url)
            if r.text.find("Please complete the security check to access") != -1:
                continue
            if r.text.find("Error get link") == -1:
                error = False
                break
        if error:
            return -1
        else:
            return url

    def __downloading(self, src):
        filename = "analyzing.mp4"
        r = requests.get(src, allow_redirects=True)
        with open(self.path, "wb") as f:
            f.write(r.content)
        return self.path
