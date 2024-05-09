# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnalyzeProgress.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSplitter, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(799, 602)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 70, 151, 41))
        self.splitter_3 = QSplitter(Form)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(130, 130, 581, 45))
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.label_4 = QLabel(self.splitter_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.splitter_3.addWidget(self.label_4)
        self.progressBar_general = QProgressBar(self.splitter_3)
        self.progressBar_general.setObjectName(u"progressBar_general")
        self.progressBar_general.setEnabled(True)
        self.progressBar_general.setValue(50)
        self.progressBar_general.setTextVisible(False)
        self.splitter_3.addWidget(self.progressBar_general)
        self.button_stop = QPushButton(Form)
        self.button_stop.setObjectName(u"button_stop")
        self.button_stop.setGeometry(QRect(360, 540, 121, 31))
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(130, 210, 581, 45))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label_status = QLabel(self.splitter)
        self.label_status.setObjectName(u"label_status")
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.label_status)
        self.progressBar_current = QProgressBar(self.splitter)
        self.progressBar_current.setObjectName(u"progressBar_current")
        self.progressBar_current.setValue(25)
        self.progressBar_current.setTextVisible(False)
        self.splitter.addWidget(self.progressBar_current)
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(130, 270, 581, 231))
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.splitter_2.addWidget(self.label_3)
        self.textEdit_log = QTextEdit(self.splitter_2)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setReadOnly(True)
        self.splitter_2.addWidget(self.textEdit_log)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0438\u0439 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
        self.progressBar_general.setFormat("")
        self.button_stop.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430", None))
        self.progressBar_current.setFormat("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433:", None))
    # retranslateUi

