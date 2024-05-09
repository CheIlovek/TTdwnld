import os

from Model.WebDriverManager import WebDriverManager
from Model.FaceAnalyzer import FaceAnalyzer
from Model.vid_to_frames import VidToFrames
from Model.downloader import Downloader
from Model.SiteManagers.Manager import ManagerType, Manager, get_manager_by_type
from Controller.LimitsChecker import LimitsChecker




class Main:

    driver_manager      : WebDriverManager
    site_manager        : Manager
    downloader          : Downloader
    video_to_frames     : VidToFrames
    face_analyzer       : FaceAnalyzer

    limit_video         : int
    current_video_count : int
    
    def __init__(self, delay : int):
        LimitsChecker.init_database()
        self.driver_manager     = WebDriverManager  (delay)
        self.downloader         = Downloader        (self.driver_manager)
        self.video_to_frames    = VidToFrames       ()
        self.face_analyzer      = FaceAnalyzer      ()


    def search_feed(self,limit = 0):
        is_no_limit = limit == 0
        self.current_video_count = 0
        self.limit_video = limit

        self.site_manager = get_manager_by_type(LimitsChecker.CURRENT_SITE_TYPE, self.driver_manager)

        while is_no_limit or self.current_video_count < limit:
            self.proccess()
            #6. Подготовка к след. кругу
            self.site_manager.next_video()

        



    def proccess(self):
        #1.     Найти видео
        video_url, channel, id = self.site_manager.get_video()
        
        #1.1    Проверить ЛИМИТ и настройки
        if not LimitsChecker.do_video_pass_limits(channel, id):
            return False
        #2.     Скачать видео
        file_name = str(LimitsChecker.CURRENT_SITE_TYPE) + '_' + channel + '_' + id
        video_path = self.downloader.dwnld(video_url, file_name)
        #3.     Разбить на кадры
        image_paths = self.video_to_frames.from_video_to_frames(video_path)
        #4.     Проверить процент
        isValid = self.face_analyzer.analyze(image_paths)
        #5.     Сохранить 
        if (isValid):
            self.current_video_count += 1
            os.rename(video_path, LimitsChecker.PATH_TO_SAVE_VIDEO + file_name)


        


def main():
    main = Main(150)
    main.search_feed(10)


if __name__ == '__main__':
    main()