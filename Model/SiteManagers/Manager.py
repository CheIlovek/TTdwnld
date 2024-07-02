from enum import IntEnum

from Model.SiteManagers.TikTokManager import TikTokManager
from Model.WebDriverManager import WebDriverManager


class ManagerType(IntEnum):
    TIKTOK = 0
    YOUTUBE_SHORTS = 1


def get_manager_by_type(type : ManagerType, driver : WebDriverManager):
    match type:
        case ManagerType.TIKTOK:
            return TikTokManager(driver)


class Manager:
    pass
    