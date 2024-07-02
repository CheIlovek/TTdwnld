# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultScreen.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 337)
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

        self.verticalSpacer = QSpacerItem(20, 72, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.splitter_7 = QSplitter(Form)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_7.setHandleWidth(50)
        self.splitter_7.setChildrenCollapsible(False)
        self.splitter_5 = QSplitter(self.splitter_7)
        self.splitter_5.setObjectName(u"splitter_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy)
        self.splitter_5.setMaximumSize(QSize(705, 16777215))
        self.splitter_5.setOrientation(Qt.Orientation.Vertical)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Horizontal)
        self.label_10 = QLabel(self.splitter_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(350, 16777215))
        self.splitter_4.addWidget(self.label_10)
        self.label_12 = QLabel(self.splitter_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(350, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.splitter_4.addWidget(self.label_12)
        self.splitter_5.addWidget(self.splitter_4)
        self.splitter_3 = QSplitter(self.splitter_5)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.label_11 = QLabel(self.splitter_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(350, 16777215))
        self.splitter_3.addWidget(self.label_11)
        self.label_13 = QLabel(self.splitter_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(350, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.splitter_3.addWidget(self.label_13)
        self.splitter_5.addWidget(self.splitter_3)
        self.splitter_2 = QSplitter(self.splitter_5)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.label_8 = QLabel(self.splitter_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(350, 16777215))
        self.splitter_2.addWidget(self.label_8)
        self.label_14 = QLabel(self.splitter_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(350, 16777215))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.splitter_2.addWidget(self.label_14)
        self.splitter_5.addWidget(self.splitter_2)
        self.splitter = QSplitter(self.splitter_5)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label_9 = QLabel(self.splitter)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(350, 16777215))
        self.splitter.addWidget(self.label_9)
        self.label_15 = QLabel(self.splitter)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(350, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.splitter.addWidget(self.label_15)
        self.splitter_5.addWidget(self.splitter)
        self.splitter_7.addWidget(self.splitter_5)

        self.verticalLayout.addWidget(self.splitter_7)

        self.verticalSpacer_2 = QSpacerItem(20, 72, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.splitter_6 = QSplitter(Form)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_6.setHandleWidth(200)
        self.button_next_2 = QPushButton(self.splitter_6)
        self.button_next_2.setObjectName(u"button_next_2")
        self.button_next_2.setMaximumSize(QSize(10000, 50))
        self.button_next_2.setStyleSheet(u"Font-weight: bold;")
        self.splitter_6.addWidget(self.button_next_2)
        self.button_next = QPushButton(self.splitter_6)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setMaximumSize(QSize(10000, 50))
        self.button_next.setStyleSheet(u"Font-weight: bold;")
        self.splitter_6.addWidget(self.button_next)

        self.verticalLayout.addWidget(self.splitter_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u" 05:38:38", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"04:30:23", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0435\u043e\u0440\u043e\u043b\u0438\u043a\u043e\u0432 \u043f\u0440\u043e\u0432\u0435\u0440\u0435\u043d\u043e:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"1500", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0435\u043e\u0440\u043e\u043b\u0438\u043a\u043e\u0432 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043e:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"50", None))
        self.button_next_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043f\u043e\u0438\u0441\u043a \u0437\u0430\u043d\u043e\u0432\u043e", None))
        self.button_next.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443", None))
    # retranslateUi

