from selenium.webdriver.common.keys import Keys

from Model.WebDriverManager import WebDriverManager
from Model.Sites.Tiktok.FeedPage import FeedPage
from Model.Sites.Page import Page
class TikTokManager:

    _driver_manger : WebDriverManager
    current_page   : Page

    def __init__(self, driver : WebDriverManager):
        self._driver_manger = driver
        self.current_page = FeedPage(driver)

    def login_via_google(self)-> bool:
        pass

    def reload_page(self):
        self.current_page = FeedPage(self._driver_manger)

    def get_video(self) -> tuple[str,str,str]:
        video_id_full = ""
        try:
            video_id_full   = self.current_page.get_video_id()
        except:
            pass
        if video_id_full == "":
            return "", "", "", ""
        channel_id      = self.current_page.get_channel_id()
        video_id = self.__parse_video_id(video_id_full)
        true_url = self.current_page.get_current_video_url()
        #https://www.tiktok.com/@CHANNEL_ID/video/VIDEO_ID
        video_url = f'https://www.tiktok.com/@{channel_id}/video/{video_id}'
        return video_url, video_id, channel_id, true_url
    
    def get_preview_url(self):
        return self.current_page.get_preview()
    
    def press_like(self):
        self.current_page.press_like()

    def next_video(self) -> bool:
        self._driver_manger.send_keys_to_site(Keys.ARROW_DOWN)
        return True


    def __parse_video_id(self,full_id):
        #xgwrapper-0-7332342275151760642 -> 7332342275151760642
        start = full_id.rfind('-') + 1
        return full_id[start::]