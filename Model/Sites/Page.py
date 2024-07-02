from Model.WebDriverManager import WebDriverManager

class Page:
    
    _driver_manager : WebDriverManager

    def __init__(self, driver : WebDriverManager):
        self._driver_manager = driver