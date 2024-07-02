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
        Form.setStyleSheet(u"\n"
"QLabel[objectName*=\"b_\"] {\n"
"	Font-weight: 600;\n"
"	vertical-align:top\n"
"}\n"
"QSplitter {\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}\n"
"* {\n"
"   	padding: 5px;\n"
"	\n"
"	Font-weight: 500;\n"
"	font-family:Montserrat;\n"
"	font-size:14px;\n"
"}\n"
"QLabel {\n"
"padding: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.splitter_4 = QSplitter(Form)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(0, -10, 801, 601))
        self.splitter_4.setMaximumSize(QSize(2000, 16777215))
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.b_label = QLabel(self.splitter_4)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setMaximumSize(QSize(2000, 16777215))
        self.b_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_4.addWidget(self.b_label)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setMaximumSize(QSize(16777215, 119))
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
        self.progressBar_general.setInvertedAppearance(False)
        self.splitter_3.addWidget(self.progressBar_general)
        self.splitter_4.addWidget(self.splitter_3)
        self.splitter = QSplitter(self.splitter_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMaximumSize(QSize(16777215, 119))
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
        self.splitter_4.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.splitter_2.addWidget(self.label_3)
        self.textEdit_log = QTextEdit(self.splitter_2)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setMaximumSize(QSize(16777215, 300))
        self.textEdit_log.setReadOnly(True)
        self.splitter_2.addWidget(self.textEdit_log)
        self.splitter_4.addWidget(self.splitter_2)
        self.button_stop = QPushButton(self.splitter_4)
        self.button_stop.setObjectName(u"button_stop")
        self.splitter_4.addWidget(self.button_stop)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b_label.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0438\u0439 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
        self.progressBar_general.setFormat("")
        self.label_status.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u0432\u0438\u0434\u0435\u043e\u0440\u043e\u043b\u0438\u043a\u0430...", None))
        self.progressBar_current.setFormat("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433:", None))
        self.textEdit_log.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Montserrat'; font-size:14px; font-weight:500; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">============================================================</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u041f\u0420\u041e\u0412\u0415\u0420\u041a\u0410 \u2116423</span></p>\n"
"<p align=\"center\" style=\" m"
                        "argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u041f\u0420\u041e\u0428\u041b\u041e \u211614</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\"> \u041f\u0440\u0435\u0432\u044c\u044e \u043e\u0442\u043a\u043e\u043b\u043d\u0435\u043d\u043e - 0  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430: 05:38:38.582382</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u0412\u0440\u0435\u043c\u044f \u0441\u0435\u0439\u0447\u0430\u0441: 07:30:44.786177  </span></p"
                        ">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\"> \u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438: 15.900709219858156</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">============================================================</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">        \u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0432\u0438\u0434\u0435\u043e:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">                URL:     https://www"
                        ".tiktok.com/@rodgri/video/7353926527614078213</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">                \u041a\u0430\u043d\u0430\u043b:   rodgri</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">                ID:      7353926527614078213</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">        \u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435 \u0447\u0435\u0440\u0435\u0437 \u0441\u0435\u0440\u0432\u0438\u0441\u044b...\u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u0435...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"
                        "14px;\">                \u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">                         0 %                     100 %          \u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u0423\u0421\u041f\u0415\u0428\u041d\u041e - 0_rodgri_7353926527614078213.mp4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">        \u0420\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u0435 \u043d\u0430 \u043a\u0430\u0434\u0440\u044b... 57  \u043a\u0430\u0434\u0440\u0430(\u043e\u0432)</span></p>\n"
"<p style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">        \u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u043e\u0432...\u041d\u0415\u0423\u0421\u041f\u0415\u0428\u041d\u041e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">        \u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e...\u0423\u0421\u041f\u0415\u0428\u041d\u041e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">        \u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043a\u0430\u0434\u0440\u043e\u0432...\u0423\u0421\u041f\u0415\u0428\u041d\u041e</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">============================================================</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u041f\u0420\u041e\u0412\u0415\u0420\u041a\u0410 \u2116423</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u041f\u0420\u041e\u0428\u041b\u041e \u211614</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\"> \u041f\u0440\u0435\u0432\u044c\u044e \u043e\u0442\u043a\u043e\u043b\u043d\u0435\u043d\u043e - 0  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430: 05:38:38.582382  </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u0412\u0440\u0435\u043c\u044f \u0441\u0435\u0439\u0447\u0430\u0441: 07:31:08.883189 </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438: 15.882352941176471<br />============================================================</span></p></body></html>", None))
        self.button_stop.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
    # retranslateUi

