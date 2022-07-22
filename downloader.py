import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


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
            self.__ssstik,
            self.__tikmate,
            self.__fliptok,
        ]
        if path == "":
            self.path = os.path.dirname(__file__) + "\\data\\analyzing.mp4"
        else:
            self.path = path

    def next_site(self):
        if self.__site_id < len(self.__sites) - 1:
            self.__site_id += 1
        else:
            self.__site_id = 0


    def dwnld(self, src):
        v_url = ""
        if src.find("www.tiktok.com/") != -1:
            for num in range(len(self.__sites)):
                try:
                    v_url = self.__sites[self.__site_id](src)
                except Exception as e:
                    print(str(e))
                    self.next_site()
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
        self.driver.get('https://ssstik.io/en')
        try:
            search = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "input-lg"))
            )
        except TimeoutException:
            raise Exception("SSSTIK cannot be loaded!")
        search.send_keys(src)
        search.send_keys(Keys.RETURN)

        try:
            search = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pure-button"))
            )
        except TimeoutException:
            raise Exception("SSSTIK cannot process URL")
        url = search.get_attribute('href')
        return url

    def __snaptik(self, src):
        url = ""
        self.driver.get("https://snaptik.app/en")
        try:
            elem = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.ID, "url"))
            )
        except TimeoutException:
            raise Exception("SNAPTIK cannot be loaded!")
        elem.send_keys(src)
        elem.send_keys(Keys.RETURN)
        try:
            elem = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "download-block")))
        except TimeoutException:
            raise Exception("SNAPTIK cannot process URL")
        elems = elem.find_elements(By.CLASS_NAME, "abutton")
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
            return ""
        else:
            return url

    def __fliptok(self, url):
        self.driver.get("https://fliptok.app/ru")
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "link-input")))
        except TimeoutException:
            raise Exception("FLIPTOK cannot be loaded")
        inp = self.driver.find_element(By.CLASS_NAME, "link-input")
        inp.send_keys(url)
        self.driver.find_element(By.ID, "download-btn").click()
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
        except TimeoutException:
            raise Exception("FLIPTOK cannot process URL")

        elem = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        url = elem.get_attribute("href")
        return url

    def __tikmate(self, src):
        url = ""
        self.driver.get("https://tikmate.online/?lang=ru")
        try:
            elem = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.ID, "url"))
            )
        except TimeoutException:
            raise Exception("TIKMATE cannot be loaded!")
        elem.send_keys(src)
        elem.send_keys(Keys.RETURN)
        try:
            elem = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "abuttons")))
        except TimeoutException:
            raise Exception("TIKMATE cannot process URL")
        elems = elem.find_elements(By.CLASS_NAME, "abutton")
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
            return ""
        else:
            return url

    def __downloading(self, src):
        r = requests.get(src, allow_redirects=True)
        with open(self.path, "wb") as f:
            f.write(r.content)
        return self.path
