from Sites.Page import Page
import WebDriverManager
from Locators.TikTok.FeedPage import *
from selenium.webdriver.common.keys import Keys

class FeedPage(Page):

    def __init__(self, driver : WebDriverManager):
        super().__init__(driver)
        self._driver_manager.get(R"https://www.tiktok.com/foryou")
    

    def click_login(self):
        #super()._driver_manager 
        pass

    def next_video(self):
        self._driver_manager.send_keys_to_site(Keys.ARROW_DOWN)
        
        pass

    def get_video_id(self):
        video_elem = self._driver_manager.get_element(CURRENT_VIDEO)
        return video_elem.get_attribute("id")
    
    def get_channel_id(self):
        channel_elem = self._driver_manager.get_element(CURRENT_CHANNEL)
        return channel_elem.text
        
    

    def click_login_via_google(self):
        pass

    def is_captcha_presented(self):
        pass