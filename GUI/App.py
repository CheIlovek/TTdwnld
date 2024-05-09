import sys
from enum import IntEnum

from PySide6.QtWidgets import QApplication, QMainWindow

from Widgets.window_service_choose      import UIServiceChoose
from Widgets.widget_analyze_progress    import UIAnalyzeProggess
from Widgets.widget_feed_settings       import UIFeedSettings
from Widgets.widget_result_screen       import UIResultScreen

class WindowsEnum(IntEnum):
    SERVICE_CHOOSE = 0
    FEED_SETTINGS = 1
    FEED_ANALYZE = 2
    RESULTS = 3


class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.switch_windows(WindowsEnum.SERVICE_CHOOSE)


    def switch_windows(self,window : WindowsEnum):
        match window:
            case WindowsEnum.SERVICE_CHOOSE:
                self.ui = UIServiceChoose()
                self.ui.setupUi(self)
            case WindowsEnum.FEED_SETTINGS:
                self.ui = UIFeedSettings()
                self.ui.setupUi(self)
            case WindowsEnum.FEED_ANALYZE:
                self.ui = UIAnalyzeProggess()
                self.ui.setupUi(self)
            case WindowsEnum.RESULTS:
                self.ui = UIResultScreen()
                self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())