import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#from Controller.LimitsChecker import LimitsChecker

class WebDriverManager:

    delay : int
    __driver : webdriver
    

    def __init__(self,path : str, delay=10, is_hidden=False):
        self.delay = delay
        if is_hidden:
            self._set_driver_hidden(path)
        else:
            self._set_driver(path)

    def get(self,url : str):
        self.__driver.get(url)

    def save_tab(self):
        self.orig_tab = self.__driver.current_window_handle

    def open_new_tab(self):
        self.__driver.switch_to.new_window('tab')

    def open_exitsting_tab(self,handler):
        self.__driver.switch_to.window(handler)
    
    def get_current_tab_handler(self):
        return self.__driver.current_window_handle
    
    def close_tab(self):
        self.__driver.close()
        self.__driver.switch_to.window(self.orig_tab)

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

    def send_keys_to_elem(self,elem,key : str):
        elem.send_keys(key)

    def _set_driver(self,path : str):
        work_dir = os.path.dirname(os.path.abspath(__file__))
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-profiles-outside-user-dir')
        options.add_argument('--enable-profile-shortcut-manager')
        options.add_argument(r"user-data-dir=" + work_dir + r"\User_Data")
        options.add_argument('--profile-directory=Profile 1')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("prefs", {
            "download.default_directory": path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.__driver = webdriver.Chrome(options=options)
        self.__driver.maximize_window()

    def _set_driver_hidden(self,path):
        work_dir = os.path.dirname(os.path.abspath(__file__))
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-profiles-outside-user-dir')
        options.add_argument('--enable-profile-shortcut-manager')
        options.add_argument(r"user-data-dir=" + work_dir + r"\User_Data_2")
        options.add_argument('--profile-directory=Profile 1')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("prefs", {
            "download.default_directory": path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        options.add_argument('--headless=new')
        self.__driver = webdriver.Chrome(options=options)

    def getDownLoadedFileName(self):
        self.__driver.execute_script("window.open()")
        self.__driver.switch_to.window(self.__driver.window_handles[-1])
        self.__driver.get('chrome://downloads')
        print("\t\tЗагрузка...")
        antiblock = 0
        prev_dwlnd_perc = -1
        while antiblock < 5:
            try:
                dwlnd_perc = self.__driver.execute_script(
                    "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
                print("\t\t\t",dwlnd_perc,"% ",end='')
                if dwlnd_perc == prev_dwlnd_perc:
                    antiblock += 1
                prev_dwlnd_perc = dwlnd_perc
                if dwlnd_perc == 100:
                    print("\t\tЗагрузка завершена!")
                    name = self.__driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
                    time.sleep(1)
                    self.__driver.close()
                    return name
            except:
                antiblock += 1
            time.sleep(1)
        return ""
        