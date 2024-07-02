from datetime import datetime
import os
import time
from loguru import logger

from Model.WebDriverManager import WebDriverManager
from Model.FaceAnalyzer import FaceAnalyzer
from Model.VideoConvertor import VidToFrames
from Model.Downloader import Downloader
from Model.SiteManagers.Manager import Manager, get_manager_by_type
from Controller.LimitsChecker import LimitsChecker

class Main:

    driver_manager      : WebDriverManager
    site_manager        : Manager
    downloader          : Downloader
    video_to_frames     : VidToFrames
    face_analyzer       : FaceAnalyzer

    limit_video         : int
    current_video_count : int
    preview_checked     : int 

    previous_id         : str   = ""
    
    def __init__(self, delay : int):
        LimitsChecker.init_database()
        self.driver_manager     = WebDriverManager  (LimitsChecker.PATH_TO_DOWNLOAD,delay)
        self.downloader         = Downloader        (delay)
        self.video_to_frames    = VidToFrames       ()
        self.face_analyzer      = FaceAnalyzer      ()
        logger.add("res.log",format="{time} {level} {message}",level="INFO")


    def search_feed(self,limit = 0):
        is_no_limit = limit == 0
        self.current_video_count = 0
        self.limit_video = limit
        checked_count = 0
        self.preview_checked = 0
        start_in_sec = int(time.time())

        start = datetime.now().time()
        self.site_manager = get_manager_by_type(LimitsChecker.CURRENT_SITE_TYPE, self.driver_manager)
        print("Время начала:", start)
        while is_no_limit or self.current_video_count < limit:
            
            checked_count += 1
            logger.success  ("ПРОВЕРКА №"            + str(checked_count))
            logger.success  ("ПРОШЛО №"              + str(self.current_video_count))
            logger.success  ("Превью отколнено -"    + str(self.preview_checked))
            logger.debug    ("Время начала:"         + str(start))
            logger.debug    ("Время сейчас:"         + str(datetime.now().time()))
            if (checked_count != 0):
                avg_check_time = (int(time.time()) - start_in_sec) / int(checked_count)
                logger.debug ("Среднее время проверки: " + str(avg_check_time))
            self.proccess()

    def proccess(self):
        time_start = time.time()
        #1.     Найти видео
        try:
            video_url, id, channel, true_url = self.site_manager.get_video()
        except:
            video_url = ""
        if video_url == "":
            print("Видео не может быть загружено.")
            self.site_manager.next_video()
            return False
        logger.debug("\tНайдено видео:")
        logger.debug("\t\tURL:\t",video_url)
        logger.debug("\t\tКанал:\t",channel)
        logger.debug("\t\tID:\t",id)
        if (id == self.previous_id):
            logger.warning("Видеоролики не прогружаются, перезагрузка страницы...")
            self.site_manager.reload_page()
            return
        else:
            self.previous_id = id
        #1.1    Проверить ЛИМИТ и настройки
        if not LimitsChecker.do_video_pass_limits(channel, id):
            return False
       
        #1.5 Получить превью
        
        preview_url = self.site_manager.get_preview_url()
        if not(preview_url is None or preview_url == ""):
            #3.1 Проверить превью
            logger.debug("\tПроверка превью...",end="")
            try:
                preview_file = self.downloader.download_image(preview_url)
            except:
                logger.debug("НЕУДАЧНО")
                preview_file = ""
        if not(preview_file == ""):
            preview_res = self.face_analyzer.analyze([preview_file])
            
            os.remove(preview_file)
            if not preview_res:
                self.preview_checked += 1
                logger.debug("НЕУДАЧНО")
                logger.debug("ПРОВЕРКА ПРЕРВАНА")  
                self.site_manager.next_video()
                time.sleep(1)  
                return False
            logger.debug("УДАЧНО")
            try:
                self.site_manager.press_like()
            except:
                logger.debug("Не лайкается!")

        #2.1. Подготовка к след. кругу
        self.site_manager.next_video()
        #2.     Скачать видео
        time_dwnld_start = time.time()
        file_name = str(LimitsChecker.CURRENT_SITE_TYPE) + '_' + channel + '_' + id + '.mp4'

        logger.info("\tЗагрузка через сервисы...",end='')
        video_path = self.downloader.dwnld(video_url, file_name)
        
        if video_path == "":
            logger.info("НЕУСПЕШНО.")
            logger.info("ПРОВЕРКА ПРЕРВАНА")
            return False
        logger.info("УСПЕШНО -", file_name)

        time_dwnld_end = time.time()
        #3.     Разбить на кадры
        logger.debug("\tРазбиение на кадры... ",end='')
        image_paths = self.video_to_frames.from_video_to_frames(video_path)
        logger.debug(len(image_paths)," кадра(ов)")
        if image_paths == "":
            logger.debug("ПРОВЕРКА ПРЕРВАНА")
            logger.debug("\tУдаление видео...",end='')
            os.remove(video_path)   
            logger.debug("УСПЕШНО")  
            return False
        #4.     Проверить процент
        logger.debug("\tПроверка процентов...",end='')
        isValid = self.face_analyzer.analyze(image_paths)
        time_end = time.time()
        full_time = time_end - time_start
        dwnld_time = time_dwnld_end - time_dwnld_start
        analyze_time = full_time - dwnld_time
        logger.info("ПОЛНЫЙ КРУГ:"  + str(full_time))
        logger.info("ЗАГРУЗКА:"     + str(dwnld_time))
        logger.info("АНАЛИЗ:"       + str(analyze_time))
        logger.info("ОТНОШЕНИЕ(З):" + str(dwnld_time/full_time))
        logger.info("ОТНОШЕНИЕ(А):" + str(analyze_time/full_time))

        #5.     Сохранить 
        if (isValid):
            logger.debug("УСПЕШНО")
            self.current_video_count += 1
            logger.debug("\tСохранение в " + LimitsChecker.PATH_TO_SAVE_VIDEO + "\\" + file_name)
            try:
                os.rename(video_path, LimitsChecker.PATH_TO_SAVE_VIDEO + "\\" + file_name)
            except:
                pass
        else:
            logger.debug("НЕУСПЕШНО")
            logger.debug("\tУдаление видео...",end='')
            os.remove(video_path)   
            logger.debug("УСПЕШНО")  
        
        logger.debug("\tУдаление кадров...",end='')
        for path in image_paths:
            os.remove(path)
        logger.debug("УСПЕШНО")
        

