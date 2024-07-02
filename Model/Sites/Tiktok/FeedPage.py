from Model.Sites.Page import Page
from Model.WebDriverManager import WebDriverManager
from Model.Locators.TikTok.FeedPage import *
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

    def press_like(self):
        video_elem = self._driver_manager.get_element(LIKE_BUTTON).click()
        


    def get_video_id(self):
        video_elem = self._driver_manager.get_element(CURRENT_VIDEO)
        if video_elem is None:
            return ""
        return video_elem.get_attribute("id")
    
    def get_preview(self):
        return self._driver_manager.get_element(PREVIEW_IMG).get_attribute("src")
    
    def get_channel_id(self):
        channel_elem = self._driver_manager.get_element(CURRENT_CHANNEL)
        return channel_elem.text
    
    def get_current_video_url(self):
        elem = self._driver_manager.get_element(CURRENT_VIDEO_URL)
        return elem.get_attribute("src")
        
        
    

    def click_login_via_google(self):
        pass

    def is_captcha_presented(self):
        pass