import os

from Model.SiteManagers.Manager import ManagerType

class LimitsChecker:
    database               : dict           = {}
    CURRENT_SITE_TYPE      : ManagerType    = ManagerType.TIKTOK
    VIDEO_PER_CHANNEL      : int            = 10
    FACE_PERCENT_REQ       : int            = 15
    FRAMES_PER_SECOND      : int            = 1
    
    PATH_TO_DOWNLOAD       : str            = R"D:\Projects\TTdwnld\buff"
    PATH_TO_SAVE_IMAGES    : str            = R"D:\Projects\TTdwnld\buff"
    PATH_TO_SAVE_VIDEO     : str            = R"D:\Projects\TTdwnld\done"

    AI_TO_USE                               = []


    @classmethod
    def init_database(cls):
        dict_path = cls.PATH_TO_SAVE_VIDEO
        for type in ManagerType:
            cls.database[type] = {}
        
        for file in os.listdir(dict_path):
            filename = file[:-4] #remove '.mp4'
            site_type   = cls.__get_next_param(filename)
            channel_id  = cls.__get_next_param(filename)
            video_id    = cls.__get_next_param(filename)
 
            if channel_id in cls.database[site_type]:
                cls.database[channel_id].append(video_id)
            else:
                cls.database[channel_id] = [video_id]

    @classmethod
    def do_video_pass_limits(cls,channel_id, video_id):
        if not channel_id in cls.database[cls.CURRENT_SITE_TYPE]:
            return True
        current_video_per_channel = len(cls.database[cls.CURRENT_SITE_TYPE][channel_id])
        return not(current_video_per_channel >= cls.VIDEO_PER_CHANNEL 
                   or video_id in cls.database[cls.CURRENT_SITE_TYPE][channel_id])
    @classmethod
    def __get_next_param(cls,filename):
        separator = filename.rfind("_")
        if separator != -1:
            return filename[:separator]
        return filename
    