# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FeedSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QSplitter, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 602)
        Form.setStyleSheet(u"QSplitter[objectName*=\"b_\"] {\n"
"	padding: 10px;\n"
"	border: 1px solid #000000;\n"
"	border-radius: 4px;\n"
"}\n"
"QLabel[objectName*=\"b_\"] {\n"
"	Font-weight: 600;\n"
"	vertical-align:top\n"
"}\n"
"* {\n"
"	font-family:Montserrat;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        Form.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"Font-weight: bold;\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.label_4)

        self.splitter_11 = QSplitter(Form)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_11.setOpaqueResize(True)
        self.splitter_11.setHandleWidth(50)
        self.splitter_11.setChildrenCollapsible(False)
        self.b_splitter_account = QSplitter(self.splitter_11)
        self.b_splitter_account.setObjectName(u"b_splitter_account")
        self.b_splitter_account.setOrientation(Qt.Orientation.Vertical)
        self.b_label_3 = QLabel(self.b_splitter_account)
        self.b_label_3.setObjectName(u"b_label_3")
        self.b_label_3.setMaximumSize(QSize(16777215, 30))
        self.b_splitter_account.addWidget(self.b_label_3)
        self.splitter = QSplitter(self.b_splitter_account)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.lineEdit_login = QLineEdit(self.splitter)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setMaximumSize(QSize(250, 16777215))
        self.splitter.addWidget(self.lineEdit_login)
        self.b_splitter_account.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.b_splitter_account)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.lineEdit_password = QLineEdit(self.splitter_2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMaximumSize(QSize(250, 16777215))
        self.splitter_2.addWidget(self.lineEdit_password)
        self.b_splitter_account.addWidget(self.splitter_2)
        self.label_login_error = QLabel(self.b_splitter_account)
        self.label_login_error.setObjectName(u"label_login_error")
        self.label_login_error.setMaximumSize(QSize(16777215, 30))
        self.b_splitter_account.addWidget(self.label_login_error)
        self.button_login_test = QPushButton(self.b_splitter_account)
        self.button_login_test.setObjectName(u"button_login_test")
        self.b_splitter_account.addWidget(self.button_login_test)
        self.splitter_11.addWidget(self.b_splitter_account)
        self.b_splitter_search_settings = QSplitter(self.splitter_11)
        self.b_splitter_search_settings.setObjectName(u"b_splitter_search_settings")
        self.b_splitter_search_settings.setOrientation(Qt.Orientation.Vertical)
        self.b_label_6 = QLabel(self.b_splitter_search_settings)
        self.b_label_6.setObjectName(u"b_label_6")
        self.b_splitter_search_settings.addWidget(self.b_label_6)
        self.splitter_5 = QSplitter(self.b_splitter_search_settings)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.spinBox)

        self.splitter_5.addWidget(self.layoutWidget)
        self.b_splitter_search_settings.addWidget(self.splitter_5)
        self.splitter_11.addWidget(self.b_splitter_search_settings)

        self.verticalLayout.addWidget(self.splitter_11)

        self.splitter_12 = QSplitter(Form)
        self.splitter_12.setObjectName(u"splitter_12")
        self.splitter_12.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_12.setHandleWidth(50)
        self.b_splitter_AI = QSplitter(self.splitter_12)
        self.b_splitter_AI.setObjectName(u"b_splitter_AI")
        self.b_splitter_AI.setMaximumSize(QSize(16777215, 106))
        self.b_splitter_AI.setOrientation(Qt.Orientation.Vertical)
        self.b_label_5 = QLabel(self.b_splitter_AI)
        self.b_label_5.setObjectName(u"b_label_5")
        self.b_label_5.setMaximumSize(QSize(16777215, 30))
        self.b_splitter_AI.addWidget(self.b_label_5)
        self.splitter_3 = QSplitter(self.b_splitter_AI)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.checkBox_OpenCV = QCheckBox(self.splitter_3)
        self.checkBox_OpenCV.setObjectName(u"checkBox_OpenCV")
        self.splitter_3.addWidget(self.checkBox_OpenCV)
        self.checkBox_dlib = QCheckBox(self.splitter_3)
        self.checkBox_dlib.setObjectName(u"checkBox_dlib")
        self.splitter_3.addWidget(self.checkBox_dlib)
        self.b_splitter_AI.addWidget(self.splitter_3)
        self.splitter_12.addWidget(self.b_splitter_AI)
        self.b_splitter_10 = QSplitter(self.splitter_12)
        self.b_splitter_10.setObjectName(u"b_splitter_10")
        self.b_splitter_10.setMaximumSize(QSize(16777215, 16777215))
        self.b_splitter_10.setOrientation(Qt.Orientation.Vertical)
        self.b_label_7 = QLabel(self.b_splitter_10)
        self.b_label_7.setObjectName(u"b_label_7")
        self.b_label_7.setStyleSheet(u"")
        self.b_splitter_10.addWidget(self.b_label_7)
        self.splitter_8 = QSplitter(self.b_splitter_10)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_4 = QSplitter(self.splitter_8)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.radio_no_limit = QRadioButton(self.splitter_4)
        self.radio_no_limit.setObjectName(u"radio_no_limit")
        self.splitter_4.addWidget(self.radio_no_limit)
        self.radio_time_limit = QRadioButton(self.splitter_4)
        self.radio_time_limit.setObjectName(u"radio_time_limit")
        self.splitter_4.addWidget(self.radio_time_limit)
        self.radio_add_limit = QRadioButton(self.splitter_4)
        self.radio_add_limit.setObjectName(u"radio_add_limit")
        self.splitter_4.addWidget(self.radio_add_limit)
        self.radio_check_limit = QRadioButton(self.splitter_4)
        self.radio_check_limit.setObjectName(u"radio_check_limit")
        self.splitter_4.addWidget(self.radio_check_limit)
        self.splitter_8.addWidget(self.splitter_4)
        self.splitter_6 = QSplitter(self.splitter_8)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setStyleSheet(u"QSplitter {\n"
"	padding-top: 20px\n"
"}")
        self.splitter_6.setOrientation(Qt.Orientation.Vertical)
        self.timeEdit_time_limit = QTimeEdit(self.splitter_6)
        self.timeEdit_time_limit.setObjectName(u"timeEdit_time_limit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_time_limit.sizePolicy().hasHeightForWidth())
        self.timeEdit_time_limit.setSizePolicy(sizePolicy)
        self.timeEdit_time_limit.setMaximumSize(QSize(100, 16777215))
        self.timeEdit_time_limit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.timeEdit_time_limit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.timeEdit_time_limit.setKeyboardTracking(False)
        self.timeEdit_time_limit.setCurrentSection(QDateTimeEdit.Section.HourSection)
        self.timeEdit_time_limit.setDisplayFormat(u"HH:mm:ss")
        self.splitter_6.addWidget(self.timeEdit_time_limit)
        self.spinBox_add_limit = QSpinBox(self.splitter_6)
        self.spinBox_add_limit.setObjectName(u"spinBox_add_limit")
        self.spinBox_add_limit.setMaximumSize(QSize(100, 16777215))
        self.splitter_6.addWidget(self.spinBox_add_limit)
        self.spinBox_check_limit = QSpinBox(self.splitter_6)
        self.spinBox_check_limit.setObjectName(u"spinBox_check_limit")
        self.spinBox_check_limit.setMaximumSize(QSize(100, 16777215))
        self.splitter_6.addWidget(self.spinBox_check_limit)
        self.splitter_8.addWidget(self.splitter_6)
        self.b_splitter_10.addWidget(self.splitter_8)
        self.splitter_12.addWidget(self.b_splitter_10)

        self.verticalLayout.addWidget(self.splitter_12)

        self.b_spliter_paths = QSplitter(Form)
        self.b_spliter_paths.setObjectName(u"b_spliter_paths")
        self.b_spliter_paths.setMaximumSize(QSize(855, 80))
        self.b_spliter_paths.setOrientation(Qt.Orientation.Vertical)
        self.b_spliter_paths.setHandleWidth(10)
        self.b_spliter_paths.setChildrenCollapsible(True)
        self.splitter_7 = QSplitter(self.b_spliter_paths)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Orientation.Horizontal)
        self.label_8 = QLabel(self.splitter_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(350, 16777215))
        self.splitter_7.addWidget(self.label_8)
        self.lineEdit_buff_path = QLineEdit(self.splitter_7)
        self.lineEdit_buff_path.setObjectName(u"lineEdit_buff_path")
        self.lineEdit_buff_path.setMaximumSize(QSize(500, 16777215))
        self.splitter_7.addWidget(self.lineEdit_buff_path)
        self.b_spliter_paths.addWidget(self.splitter_7)
        self.splitter_9 = QSplitter(self.b_spliter_paths)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Orientation.Horizontal)
        self.label_9 = QLabel(self.splitter_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(350, 16777215))
        self.splitter_9.addWidget(self.label_9)
        self.lineEdit_save_path = QLineEdit(self.splitter_9)
        self.lineEdit_save_path.setObjectName(u"lineEdit_save_path")
        self.lineEdit_save_path.setMaximumSize(QSize(500, 16777215))
        self.splitter_9.addWidget(self.lineEdit_save_path)
        self.b_spliter_paths.addWidget(self.splitter_9)

        self.verticalLayout.addWidget(self.b_spliter_paths)

        self.label_general_error = QLabel(Form)
        self.label_general_error.setObjectName(u"label_general_error")
        self.label_general_error.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label_general_error)

        self.button_next = QPushButton(Form)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setMaximumSize(QSize(10000, 50))
        self.button_next.setStyleSheet(u"Font-weight: bold;")

        self.verticalLayout.addWidget(self.button_next)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430 \u0432 \u043b\u0435\u043d\u0442\u0435", None))
        self.b_label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430 \u0441\u0435\u0440\u0432\u0438\u0441\u0430:", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_login_error.setText("")
        self.button_login_test.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.b_label_6.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043b\u0438\u0446\u0430", None))
        self.b_label_5.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0435 \u043d\u0435\u0439\u0440\u043e\u0441\u0435\u0442\u0438", None))
        self.checkBox_OpenCV.setText(QCoreApplication.translate("Form", u"OpenCV", None))
        self.checkBox_dlib.setText(QCoreApplication.translate("Form", u"Face Recognition (dlib)", None))
        self.b_label_7.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u043b\u043e\u0432\u0438\u0435 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.radio_no_limit.setText(QCoreApplication.translate("Form", u"\u0414\u043e \u0440\u0443\u0447\u043d\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.radio_time_limit.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.radio_add_limit.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0445 \u0432 \u0411\u0414 \u0432\u0438\u0434\u0435\u043e", None))
        self.radio_check_limit.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0445 \u0432\u0438\u0434\u0435\u043e", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u0447\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430:", None))
        self.label_general_error.setText("")
        self.button_next.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
    # retranslateUi

