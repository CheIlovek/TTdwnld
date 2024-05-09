from PySide6.QtCore import *

from GUI.Widgets.widget_feed_settings import *

from GUI.App import App, WindowsEnum
from LimitsChecker import LimitsChecker

class FeedSettingsController:

    ui : object
    app : App

    def __init__(self, model, ui : object, app : App):
        self.ui = ui
        self.model = model
        self.app = app

    def save_settings(self):

        buff_path = self.ui.lineEdit_buff_path.text()
        save_path = self.ui.lineEdit_save_path.text()
        LimitsChecker.PATH_TO_DOWNLOAD      = buff_path + R"\buffVid\"
        LimitsChecker.PATH_TO_SAVE_IMAGES   = buff_path + R"\buffImg\"
        LimitsChecker.PATH_TO_SAVE_VIDEO    = save_path

        if self.ui.checkBox_OpenCV.isChecked():
            pass
        if self.ui.checkBox_dlib.isChecked():
            pass

        if self.ui.check_search_glasses.isChecked():
            pass
        if self.ui.check_search_hat.isChecked():
            pass


        self.ui.radio_no_limit

        self.ui.radio_time_limit
        self.ui.timeEdit_time_limit

        self.ui.radio_add_limit
        self.ui.spinBox_add_limit

        self.ui.radio_check_limit
        self.ui.spinBox_check_limit
        self.app.switch_window(WindowsEnum.FEED_ANALYZE)
        



    def test_login(self):
        login =     self.ui.lineEdit_login      .text()
        password =  self.ui.lineEdit_password   .text()
        result = False
        #result = model.test_login(login,password)
        if (result):
            self.ui.label_login_error.setText("Успешный вход.")
        else:
            self.ui.label_login_error.setText("Вход невозможен.")

