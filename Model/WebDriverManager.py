import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class WebDriverManager:

    delay : int
    __driver : webdriver

    def __init__(self : webdriver, delay=10, path=""):
        self.delay = delay
        self._set_driver()

    def get(self,url : str):
        self.__driver.get(url)

    def wait_for_element(self):
        pass

    def get_element(self, locator : str):
        try:
            elem = WebDriverWait(self.__driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, locator)))

        except TimeoutException:
            #ERROR
            elem = None
        return elem

    def send_keys_to_site(self, key):
        ActionChains(self.__driver).send_keys(key).perform()
        pass

    def send_keys_to_elem(self):
        pass

    def _set_driver(self):
        work_dir = os.path.dirname(os.path.abspath(__file__))
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-profiles-outside-user-dir')
        options.add_argument('--enable-profile-shortcut-manager')
        options.add_argument(r"user-data-dir=" + work_dir + r"\User_Data")
        options.add_argument('--profile-directory=Profile 1')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.__driver = webdriver.Chrome(options=options)
        self.__driver.maximize_window()