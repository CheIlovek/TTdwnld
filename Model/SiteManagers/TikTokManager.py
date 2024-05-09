import WebDriverManager
from Sites.Tiktok.FeedPage import FeedPage
from Sites.Page import Page
class TikTokManager:

    _driver_manger : WebDriverManager
    current_page   : Page

    def __init__(self, driver : WebDriverManager):
        self._driver_manger = driver
        self.current_page = FeedPage(driver)

    def login_via_google(self)-> bool:
        pass

    def get_video(self) -> tuple[str,str,str]:
        video_id_full   = self.current_page.get_video_id()
        channel_id      = self.current_page.get_channel_id()
        video_id = self.__parse_video_id(video_id_full)
        #https://www.tiktok.com/@CHANNEL_ID/video/VIDEO_ID
        video_url = f'https://www.tiktok.com/@{channel_id}/video/{video_id}'
        return video_url, video_id, channel_id
    
    def next_video(self) -> bool:
        pass


    def __parse_video_id(self,full_id):
        #xgwrapper-0-7332342275151760642 -> 7332342275151760642
        start = full_id.rfind('-') + 1
        return full_id[start::]