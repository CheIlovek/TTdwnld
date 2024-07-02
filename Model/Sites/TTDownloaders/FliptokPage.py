from Model.Locators.TTDownloaders.Fliptok import * 
from Model.Sites.TTDownloaders.DownloadPage import DonwloadPage
from Model.WebDriverManager import WebDriverManager
from Model.Locators.TikTok.FeedPage import *
from selenium.webdriver.common.keys import Keys

class FliptokPage(DonwloadPage):
    def __init__(self, driver : WebDriverManager):
        super().__init__(driver)
        self._driver_manager.get(R"https://fliptok.app/ru")
    
    def get_dwnld_url(self,src : str) -> str:
        if self.__send_url(src) and self.__press_conf_button():
            return self.__get_true_url()
        return ""
    
    def get_home_page(self):
        self._driver_manager.get(R"https://fliptok.app/ru")

    def __press_conf_button(self) -> bool:
        elem = self._driver_manager.get_element(CONFIRM_INPUT_BUTTON)
        if elem is None:
            return False
        elem.click()
        return True

    def __send_url(self,src : str) -> str:
        elem = self._driver_manager.get_element(URL_INPUT)
        if elem is None:
            return False
        self._driver_manager.send_keys_to_elem(elem,src)
        self._driver_manager.send_keys_to_elem(elem,Keys.ENTER)
        return True
        
    def __get_true_url(self):
        elem = self._driver_manager.get_element(DOWNLOAD_BUTTON_2)
        if elem is None:
            elem = self._driver_manager.get_element(DOWNLOAD_BUTTON_1)
            if elem is None:
                return ""
        return elem.get_attribute("href")