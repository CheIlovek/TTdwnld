from statistics import LinearRegression
import time
from tqdm import tqdm
import os

import requests
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.common.by       import By
from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.support         import expected_conditions      as EC
from selenium.common.exceptions         import TimeoutException

from Model.Sites.TTDownloaders.DownloadPage import DonwloadPage
from Model.WebDriverManager                 import WebDriverManager
from Model.Sites.TTDownloaders.SnaptikPage  import SnaptikPage
from Model.Sites.TTDownloaders.SsstikPage   import SsstikPage
from Model.Sites.TTDownloaders.FliptokPage  import FliptokPage
from Controller.LimitsChecker               import LimitsChecker


class Downloader:
    __pages : list[DonwloadPage]
    __tab_handlers = []
    __site_id = 1
    driver : WebDriverManager

    def __init__(self,delay : int):
        
        self.driver = WebDriverManager(LimitsChecker.PATH_TO_DOWNLOAD,delay,True)
        

        snaptik_page = SnaptikPage(self.driver)
        snaptik_handler = self.driver.get_current_tab_handler()

        self.driver.open_new_tab()
        ssstik_page = SsstikPage(self.driver)
        ssstik_handler = self.driver.get_current_tab_handler()

        self.driver.open_new_tab()
        fliptok_page = FliptokPage(self.driver)
        fliptok_handler = self.driver.get_current_tab_handler()

        self.__tab_handlers = [
            snaptik_handler,
            #ssstik_handler,
            fliptok_handler,
        ]

        self.__pages = [
            snaptik_page,
            #ssstik_page,
            fliptok_page,
        ]


    def forward_dwnld(self, src : str, name = "") -> str:
        return self.__downloading(src, name)
    
    def download_image(self,src : str,name : str = "prev.jpeg") -> str:
        response = requests.get(src, stream=True, allow_redirects=True)
        full_name = os.path.join(LimitsChecker.PATH_TO_DOWNLOAD,name)
        with open(full_name, "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)
        return full_name

    def dwnld(self, src, name):
        len_arr_sites = len(self.__pages)
        for num in range(len_arr_sites):
            self.__site_id = (self.__site_id + 1) % len_arr_sites
            v_url = self.__get_url_from_service(src)
            if v_url != "":
                break
        
        #self.driver.close_tab()
        if v_url == "":
            print("\tURL не найден")
            return ""
        print("скачивание...")
        v_path = self.__downloading(v_url, name)
        return v_path 

    def __get_url_from_service(self,src : str) -> str:
        self.driver.open_exitsting_tab(self.__tab_handlers[self.__site_id])
        url = self.__pages[self.__site_id].get_dwnld_url(src)
        self.__pages[self.__site_id].get_home_page()
        return url


    def __downloading(self, src, name):
        self.driver.get(src)
        true_name = self.driver.getDownLoadedFileName()
        if (true_name == ""):
            return ""
        true_full_name = os.path.join(LimitsChecker.PATH_TO_DOWNLOAD,true_name)
        if (name == ""):
            return true_full_name
        full_dst_name = os.path.join(LimitsChecker.PATH_TO_DOWNLOAD,name)
        time.sleep(1)
        os.rename(
            true_full_name,
            full_dst_name )
        return full_dst_name
            