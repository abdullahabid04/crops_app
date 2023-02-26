from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1371, 711)
        MainWindow.setMinimumSize(QSize(1371, 711))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_31 = QFrame(self.centralwidget)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(0, 0, 1343, 683))
        self.frame_31.setStyleSheet(u"QFrame{\n"
                                    "border: 1px solid rgb(163, 163, 163);\n"
                                    "\n"
                                    "}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.mainframe = QFrame(self.frame_31)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setGeometry(QRect(1, 1, 1341, 681))
        font = QFont()
        font.setFamily(u"Poppins")
        self.mainframe.setFont(font)
        self.mainframe.setStyleSheet(u"QFrame{\n"
                                     "background-color: rgb(246, 247, 249);\n"
                                     "color:rgb(30, 25, 83);\n"
                                     "border:none;\n"
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
                                     ""
                                     "	border-top-right-radius: 3px;\n"
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
        self.frame.setGeometry(QRect(0, 0, 61, 781))
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
        self.dashboard_side = QPushButton(self.frame)
        self.dashboard_side.setObjectName(u"dashboard_side")
        self.dashboard_side.setGeometry(QRect(0, 89, 61, 61))
        self.dashboard_side.setStyleSheet(u"QPushButton{\n"
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
        self.report_side = QPushButton(self.frame)
        self.report_side.setObjectName(u"report_side")
        self.report_side.setGeometry(QRect(0, 149, 61, 61))
        self.report_side.setStyleSheet(u"QPushButton{\n"
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
        self.database_side = QPushButton(self.frame)
        self.database_side.setObjectName(u"database_side")
        self.database_side.setGeometry(QRect(0, 210, 61, 61))
        self.database_side.setStyleSheet(u"QPushButton{\n"
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
        self.print_side = QPushButton(self.frame)
        self.print_side.setObjectName(u"print_side")
        self.print_side.setGeometry(QRect(0, 270, 61, 61))
        self.print_side.setStyleSheet(u"QPushButton{\n"
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
        self.login_side_menu = QPushButton(self.frame)
        self.login_side_menu.setObjectName(u"login_side_menu")
        self.login_side_menu.setGeometry(QRect(0, 392, 61, 61))
        self.login_side_menu.setStyleSheet(u"QPushButton{\n"
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
        self.settings_side = QPushButton(self.frame)
        self.settings_side.setObjectName(u"settings_side")
        self.settings_side.setGeometry(QRect(0, 331, 61, 61))
        self.settings_side.setStyleSheet(u"QPushButton{\n"
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
        self.stackedWidget = QStackedWidget(self.mainframe)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(61, 29, 1261, 781))
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.frame_5 = QFrame(self.dashboard_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(350, 140, 281, 161))
        self.frame_5.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 171, 16))
        font1 = QFont()
        font1.setFamily(u"Poppins SemiBold")
        font1.setPointSize(9)
        self.label_2.setFont(font1)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 130, 111, 16))
        font2 = QFont()
        font2.setFamily(u"Poppins SemiBold")
        font2.setPointSize(10)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color:rgb(34, 182, 49);")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 221, 41))
        font3 = QFont()
        font3.setFamily(u"Poppins SemiBold")
        font3.setPointSize(17)
        self.label_10.setFont(font3)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(220, 0, 61, 61))
        self.frame_12.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-timer-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.dashboard_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(651, 140, 281, 161))
        self.frame_6.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 151, 16))
        self.label_3.setFont(font1)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 60, 251, 41))
        self.label_15.setFont(font3)
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 130, 141, 16))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color:rgb(34, 182, 49);")
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setGeometry(QRect(220, 0, 61, 61))
        self.frame_13.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-corn-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.dashboard_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(951, 140, 281, 161))
        self.frame_7.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 211, 16))
        self.label_4.setFont(font1)
        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 130, 201, 16))
        font4 = QFont()
        font4.setFamily(u"Poppins SemiBold")
        font4.setPointSize(8)
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color:rgb(207, 206, 218);")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 60, 51, 41))
        self.label_19.setFont(font3)
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 130, 171, 16))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color:rgb(34, 182, 49);")
        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(220, 0, 61, 61))
        self.frame_14.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-timer-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.dashboard_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(49, 330, 581, 291))
        self.frame_8.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 111, 16))
        self.label_12.setFont(font1)
        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(520, 0, 61, 61))
        self.frame_15.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.widget_5 = QWidget(self.frame_8)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(20, 70, 541, 201))
        self.frame_18 = QFrame(self.frame_8)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(10, 60, 561, 221))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_18)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, 0, 561, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12.raise_()
        self.frame_15.raise_()
        self.frame_18.raise_()
        self.widget_5.raise_()
        self.frame_4 = QFrame(self.dashboard_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(49, 140, 281, 161))
        self.frame_4.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "\n"
                                   "}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 16))
        self.label.setFont(font1)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 60, 51, 41))
        self.label_5.setFont(font3)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(127, 20, 71, 16))
        font5 = QFont()
        font5.setFamily(u"Poppins")
        font5.setPointSize(9)
        self.label_6.setFont(font5)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 130, 201, 16))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color:rgb(207, 206, 218);")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 130, 31, 16))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color:rgb(34, 182, 49);")
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(220, 0, 61, 61))
        self.frame_11.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-irrigation-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.dashboard_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(649, 330, 581, 291))
        self.frame_9.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 20, 191, 16))
        self.label_23.setFont(font1)
        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(401, 13, 161, 27))
        self.tableWidget = QTableWidget(self.frame_9)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 541, 201))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(30, 25, 83, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(30, 25, 83, 128))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush5 = QBrush(QColor(30, 25, 83, 128))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(30, 25, 83, 128))
        brush7.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
                                       "	background-color: transparent;\n"
                                       "	\n"
                                       "	\n"
                                       "\n"
                                       "	\n"
                                       "}\n"
                                       "QTableView::item {\n"
                                       "border-bottom: 1px solid rgb(241, 243, 247);\n"
                                       "\n"
                                       "\n"
                                       "}\n"
                                       "QTableWidget::item{\n"
                                       "	\n"
                                       "	padding-left: 20px;\n"
                                       "\n"
                                       "	\n"
                                       "}\n"
                                       "QTableWidget::item:selected{\n"
                                       "	background-color: rgb(85, 170, 255);\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QTableWidget::horizontalHeader {	\n"
                                       "	background-color:transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section:vertical\n"
                                       "{\n"
                                       "   \n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.frame_10 = QFrame(self.dashboard_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(-1, 0, 1281, 41))
        self.frame_10.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "\n"
                                    "}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(879, 7, 92, 27))
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setIconSize(QSize(16, 16))
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(979, 7, 161, 27))
        self.login = QPushButton(self.frame_10)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(1150, 7, 92, 27))
        self.login.setStyleSheet(u"")
        self.login.setIconSize(QSize(16, 16))
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(49, 14, 111, 16))
        self.label_11.setFont(font2)
        self.frame_33 = QFrame(self.dashboard_page)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(49, 70, 581, 41))
        self.frame_33.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "color: rgb(30, 25, 83);\n"
                                    "border-radius:10px;\n"
                                    "}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.crop_data_select_2 = QComboBox(self.frame_33)
        self.crop_data_select_2.setObjectName(u"crop_data_select_2")
        self.crop_data_select_2.setGeometry(QRect(420, 7, 131, 27))
        self.crop_data_select_2.setStyleSheet(u"color:rgb(30, 25, 83)")
        self.label_53 = QLabel(self.frame_33)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(30, 11, 161, 20))
        self.label_53.setFont(font5)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.frame_17 = QFrame(self.report_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(49, 140, 581, 291))
        font6 = QFont()
        font6.setPointSize(8)
        self.frame_17.setFont(font6)
        self.frame_17.setStyleSheet(u"QFrame{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "\n"
                                    "}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.frame_17)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 20, 111, 16))
        self.label_41.setFont(font1)
        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(520, 0, 61, 61))
        self.frame_19.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_17)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 541, 201))
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 60, 561, 221))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_20)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(-1, 0, 561, 221))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_41.raise_()
        self.frame_19.raise_()
        self.frame_20.raise_()
        self.widget.raise_()
        self.frame_21 = QFrame(self.report_page)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(49, 70, 581, 41))
        self.frame_21.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "color: rgb(30, 25, 83);\n"
                                    "border-radius:10px;\n"
                                    "}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.crop_data_select = QComboBox(self.frame_21)
        self.crop_data_select.setObjectName(u"crop_data_select")
        self.crop_data_select.setGeometry(QRect(420, 7, 131, 27))
        self.crop_data_select.setStyleSheet(u"color:rgb(30, 25, 83)")
        self.label_49 = QLabel(self.frame_21)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(21, 13, 201, 20))
        self.label_49.setFont(font5)
        self.frame_23 = QFrame(self.report_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(49, 460, 581, 291))
        self.frame_23.setStyleSheet(u"QFrame{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "\n"
                                    "}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_50 = QLabel(self.frame_23)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(20, 20, 111, 16))
        self.label_50.setFont(font1)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(520, 0, 61, 61))
        self.frame_25.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.widget_3 = QWidget(self.frame_23)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 70, 541, 201))
        self.frame_22 = QFrame(self.frame_23)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(10, 60, 561, 221))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_22)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(-1, 0, 561, 221))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_50.raise_()
        self.frame_25.raise_()
        self.frame_22.raise_()
        self.widget_3.raise_()
        self.frame_26 = QFrame(self.report_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(649, 140, 581, 291))
        self.frame_26.setStyleSheet(u"QFrame{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "\n"
                                    "}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_51 = QLabel(self.frame_26)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(20, 20, 111, 16))
        self.label_51.setFont(font1)
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(520, 0, 61, 61))
        self.frame_28.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.frame_26)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 70, 541, 201))
        self.frame_24 = QFrame(self.frame_26)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(10, 60, 561, 221))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_24)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(-1, 0, 561, 221))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_51.raise_()
        self.frame_28.raise_()
        self.frame_24.raise_()
        self.widget_2.raise_()
        self.frame_29 = QFrame(self.report_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(649, 460, 581, 291))
        self.frame_29.setStyleSheet(u"QFrame{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "\n"
                                    "}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_52 = QLabel(self.frame_29)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(20, 20, 111, 16))
        self.label_52.setFont(font1)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(520, 0, 61, 61))
        self.frame_30.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-combo-chart-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.widget_4 = QWidget(self.frame_29)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 70, 541, 201))
        self.frame_27 = QFrame(self.frame_29)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(10, 60, 561, 221))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_27)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(-1, 0, 561, 221))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_52.raise_()
        self.frame_30.raise_()
        self.frame_27.raise_()
        self.widget_4.raise_()
        self.frame_32 = QFrame(self.report_page)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(-1, 0, 1281, 41))
        self.frame_32.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "\n"
                                    "}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_48 = QLabel(self.frame_32)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(49, 14, 111, 16))
        self.label_48.setFont(font2)
        self.stackedWidget.addWidget(self.report_page)
        self.print_page = QWidget()
        self.print_page.setObjectName(u"print_page")
        self.stackedWidget.addWidget(self.print_page)
        self.verticalScrollBar = QScrollBar(self.mainframe)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(1322, 30, 20, 631))
        self.verticalScrollBar.setMinimum(0)
        self.verticalScrollBar.setMaximum(150)
        self.verticalScrollBar.setSingleStep(150)
        self.verticalScrollBar.setPageStep(150)
        self.verticalScrollBar.setValue(0)
        self.verticalScrollBar.setSliderPosition(0)
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)
        self.frame.raise_()
        self.stackedWidget.raise_()
        self.frame_2.raise_()
        self.verticalScrollBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainframe.setAccessibleDescription("")
        self.dashboard_side.setText("")
        self.report_side.setText("")
        self.database_side.setText("")
        self.print_side.setText("")
        self.login_side_menu.setText("")
        self.settings_side.setText("")
        self.label_24.setText(
            QCoreApplication.translate("MainWindow", u"Agriculture Irrigation Desktop App | CARE IUB", None))
        self.closeButton_2.setText("")
        self.minimize_btn_2.setText("")
        self.minimize_btn.setText("")
        self.closeButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Next Irrigation Interval", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"See Full Report", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"4d 15h 13min", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Crop Status", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Initial Stage", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"See Full Report", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Days Remaining to Harvest", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"140", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"See Full Report", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Real-Time Data", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Estimated Water", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"134", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"(mm/day)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"increased compared to last month", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"14%", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Crops Being Monitored", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Manage Monitoring Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Crops", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Days Remaining", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"asdf", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Crops", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Days Remaining", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Crop", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Manage Monitoring Data", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Select crop to see its data:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Real-Time Data", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Select crop to see graphs:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Et0 Graph", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Kc Graph", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Etc Graph", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Real-Time Data", None))
