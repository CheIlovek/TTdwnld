
from Model.WebDriverManager import WebDriverManager
from Model.FaceAnalyzer import FaceAnalyzer
from Model.VideoConvertor import VidToFrames
from Model.Downloader import Downloader
from Model.SiteManagers.Manager import ManagerType, Manager, get_manager_by_type
from Controller.LimitsChecker import LimitsChecker
from Model.ModelMain import Main
import time


def main():
    main = Main(20)
    main.search_feed()


if __name__ == '__main__':
    main()