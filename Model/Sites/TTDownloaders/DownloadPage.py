from abc import abstractmethod
from Model.Sites.Page import Page
from Model.Locators.TTDownloaders.Fliptok import * 
from Model.WebDriverManager import WebDriverManager
from Model.Locators.TikTok.FeedPage import *
from selenium.webdriver.common.keys import Keys

class DonwloadPage(Page):
    def __init__(self, driver : WebDriverManager):
        super().__init__(driver)
        self._driver_manager.get(R"https://fliptok.app/ru")

    @abstractmethod
    def get_dwnld_url(self,src : str) -> str:
        ...

    @abstractmethod
    def get_home_page(self):
        ...