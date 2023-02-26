from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(963, 575)
        self.mainframe = QFrame(Dialog)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setGeometry(QRect(0, 0, 1341, 841))
        font = QFont()
        font.setFamily(u"Poppins")
        self.mainframe.setFont(font)
        self.mainframe.setStyleSheet(u"QFrame{\n"
                                     "background-color: rgb(246, 247, 249);\n"
                                     "color:rgb(30, 25, 83);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton {\n"
                                     "	border: 1px solid rgb(229, 229, 234);\n"
                                     "	border-radius: 5px;	\n"
                                     "	background-color:rgb(255, 255, 255);\n"
                                     "color:rgb(30, 25, 83);\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	\n"
                                     "	border: 2px solid rgb(229, 229, 234);\n"
                                     "}\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color:rgb(234, 234, 229);\n"
                                     "border: 2px solid  rgb(234, 234, 229);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "QComboBox{\n"
                                     "	background-color: rgb(255, 255, 255);\n"
                                     "	border-radius: 5px;\n"
                                     "	border: 1px solid rgb(229, 229, 234);\n"
                                     "	padding: 5px;\n"
                                     "	padding-left: 10px;\n"
                                     "\n"
                                     "}\n"
                                     "QComboBox:hover{\n"
                                     "	border: 2px solid  rgb(229, 229, 234);\n"
                                     "}\n"
                                     "QComboBox::drop-down {\n"
                                     "image : url(F:/books/gui - Copy/Youtube Downloader/asd.png);\n"
                                     "	subcontrol-origin: padding;\n"
                                     "	subcontrol-position: top right;\n"
                                     "	width: 25px; \n"
                                     "	\n"
                                     "	border-left-width: 1px;\n"
                                     "	border-left-color: rgb(229, 229, 234);\n"
                                     "	border-left-style: solid;\n"
                                     "	border-top-righ"
                                     "t-radius: 3px;\n"
                                     "	border-bottom-right-radius: 3px;	\n"
                                     "	\n"
                                     "	background-position: center;\n"
                                     "	background-repeat: no-reperat;\n"
                                     " }\n"
                                     "")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.mainframe)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 61, 841))
        self.frame.setStyleSheet(u"QFrame{\n"
                                 "background-color: rgb(30, 25, 83);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "background-color: rgb(30, 25, 83);\n"
                                 "border-radius:0px;\n"
                                 "border-color:none;\n"
                                 "	border: 0px;\n"
                                 "	\n"
                                 "\n"
                                 "\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "	\n"
                                 "	border: 0px;\n"
                                 "}\n"
                                 "QPushButton:pressed {	\n"
                                 "	background-color:rgb(36, 33, 97);\n"
                                 "border: 0px;\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 89, 61, 61))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-home-16(1).png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-home-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "\n"
                                        "	background-color:rgb(36, 33, 97);\n"
                                        "border: 0px;\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-home-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "}")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 149, 61, 61))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-16(1).png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "\n"
                                        "	background-color:rgb(36, 33, 97);\n"
                                        "border: 0px;\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-16(1).png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "}")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 210, 61, 61))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-database-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/database.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "\n"
                                        "	background-color:rgb(36, 33, 97);\n"
                                        "border: 0px;\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/database.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "}")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 270, 61, 61))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-print-16(1).png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-print-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "\n"
                                        "	background-color:rgb(36, 33, 97);\n"
                                        "border: 0px;\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-print-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "}")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(0, 392, 61, 61))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-login-16(1).png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-login-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "\n"
                                        "	background-color:rgb(36, 33, 97);\n"
                                        "border: 0px;\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-login-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "}")
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(0, 331, 61, 61))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-settings-16(1).png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-settings-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "\n"
                                        "	background-color:rgb(36, 33, 97);\n"
                                        "border: 0px;\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-settings-16.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "}")
        self.frame_2 = QFrame(self.mainframe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -1, 1341, 31))
        self.frame_2.setStyleSheet(u"QFrame{\n"
                                   "background-color:rgb(226, 226, 226);\n"
                                   "\n"
                                   "}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_icon_top_bar = QFrame(self.frame_2)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setGeometry(QRect(16, 2, 30, 30))
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image:  url(F:/books/agriculture project/desktop app/agri/watering-can.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(50, 7, 1191, 21))
        self.label_24.setFont(font)
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(1240, 0, 101, 31))
        self.frame_16.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(226, 226, 226);\n"
                                    "\n"
                                    "}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.closeButton_2 = QPushButton(self.frame_16)
        self.closeButton_2.setObjectName(u"closeButton_2")
        self.closeButton_2.setGeometry(QRect(1304, 0, 37, 31))
        self.closeButton_2.setStyleSheet(u"\n"
                                         "QPushButton {	\n"
                                         "	border: none;\n"
                                         "	background-color: transparent;\n"
                                         "\n"
                                         "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-close-window-20.png);\n"
                                         "\n"
                                         "background-repeat: no-repeat;\n"
                                         "background-position: center;\n"
                                         "border-radius: 0px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(255, 82, 76);\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color:rgb(255, 82, 76);\n"
                                         "border-radius: 0px;\n"
                                         "}")
        self.minimize_btn_2 = QPushButton(self.frame_16)
        self.minimize_btn_2.setObjectName(u"minimize_btn_2")
        self.minimize_btn_2.setGeometry(QRect(1267, 0, 37, 31))
        self.minimize_btn_2.setStyleSheet(u"\n"
                                          "QPushButton {	\n"
                                          "	border: none;\n"
                                          "	background-color: transparent;\n"
                                          "\n"
                                          "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-minimize-window-20.png);\n"
                                          "\n"
                                          "background-repeat: no-repeat;\n"
                                          "background-position: center;\n"
                                          "border-radius: 0px;\n"
                                          "\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "	background-color:rgb(191, 191, 191);\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:pressed {	\n"
                                          "	background-color:rgb(162, 162, 162);\n"
                                          "border-radius: 0px;\n"
                                          "}")
        self.minimize_btn = QPushButton(self.frame_16)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(30, 0, 37, 31))
        self.minimize_btn.setStyleSheet(u"\n"
                                        "QPushButton {	\n"
                                        "	border: none;\n"
                                        "	background-color: transparent;\n"
                                        "\n"
                                        "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-minimize-window-20.png);\n"
                                        "\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "border-radius: 0px;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color:rgb(191, 191, 191);\n"
                                        "border-radius: 0px;\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color:rgb(162, 162, 162);\n"
                                        "border-radius: 0px;\n"
                                        "}")
        self.closeButton = QPushButton(self.frame_16)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(67, 0, 37, 31))
        self.closeButton.setStyleSheet(u"\n"
                                       "QPushButton {	\n"
                                       "	border: none;\n"
                                       "	background-color: transparent;\n"
                                       "\n"
                                       "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-close-window-20.png);\n"
                                       "\n"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: center;\n"
                                       "border-radius: 0px;\n"
                                       "\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "	background-color: rgb(255, 82, 76);\n"
                                       "border-radius: 0px;\n"
                                       "}\n"
                                       "QPushButton:pressed {	\n"
                                       "	background-color:rgb(255, 82, 76);\n"
                                       "border-radius: 0px;\n"
                                       "}")
        self.label = QLabel(self.mainframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 210, 361, 171))
        font1 = QFont()
        font1.setPointSize(51)
        self.label.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.mainframe.setAccessibleDescription("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.label_24.setText(
            QCoreApplication.translate("Dialog", u"Agriculture Irrigation Desktop App | CARE IUB", None))
        self.closeButton_2.setText("")
        self.minimize_btn_2.setText("")
        self.minimize_btn.setText("")
        self.closeButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Next screen", None))
