from PySide6.QtCore import *

from GUI.Widgets.widget_feed_settings import *

from GUI.App import App, WindowsEnum
from LimitsChecker import LimitsChecker

class ServiceChooserController:

    ui : object
    app : App

    def __init__(self, model, ui : object, app : App):
        self.ui = ui
        self.model = model
        self.app = app

    #определить нажатую кнопку??