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
        MainWindow.resize(1444, 846)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainframe = QFrame(self.centralwidget)
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
        self.frame_3 = QFrame(self.mainframe)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(61, 29, 821, 61))
        self.frame_3.setStyleSheet(u"QFrame{\n"
                                   "background-color:rgb(255, 255, 255);\n"
                                   "color: rgb(30, 25, 83)\n"
                                   "}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.frame_17 = QFrame(self.mainframe)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(320, 140, 651, 41))
        self.frame_17.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "color:rgb(255, 102, 82);\n"
                                    "}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.frame_17.hide()

        self.closeButton_3 = QPushButton(self.frame_17)
        self.closeButton_3.setObjectName(u"closeButton_3")
        self.closeButton_3.setGeometry(QRect(620, 11, 18, 18))
        self.closeButton_3.setStyleSheet(u"\n"
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
                                         "\n"
                                         "")
        label_25_font = QFont()
        label_25_font.setFamily(u"Poppins SemiBold")
        label_25_font.setPointSize(9)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(19, 12, 571, 20))
        self.label_25.setFont(label_25_font)

        self.label_25.setText(
            QCoreApplication.translate("MainWindow", u"Error: Entered date cannot be greater than current date.", None))
        self.closeButton_3.setText("")

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 18, 91, 27))
        self.comboBox.setStyleSheet(u"color:rgb(30, 25, 83)")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 24, 31, 16))
        self.label_13.setFont(font)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(250, 24, 71, 16))
        self.label_17.setFont(font)
        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(522, 18, 91, 27))
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(460, 24, 61, 16))
        self.label_21.setFont(font)
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(640, 24, 31, 16))
        self.label_22.setFont(font)
        self.comboBox_4 = QComboBox(self.frame_3)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(674, 18, 91, 27))
        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(330, 18, 91, 27))
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
                                    "border: 1px solid rgb(229, 229, 234);\n"
                                    "border-radius: 5px;\n"
                                    "color: rgb(30, 25, 83)\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit::drop-down {\n"
                                    "image : url(F:/books/gui - Copy/Youtube Downloader/asd.png);\n"
                                    "	subcontrol-origin: padding;\n"
                                    "	subcontrol-position: top right;\n"
                                    "	width: 25px; \n"
                                    "	\n"
                                    "	border-left-width: 1px;\n"
                                    "	border-left-color: rgb(229, 229, 234);\n"
                                    "	border-left-style: solid;\n"
                                    "	border-top-right-radius: 3px;\n"
                                    "	border-bottom-right-radius: 3px;	\n"
                                    "	\n"
                                    "	background-position: center;\n"
                                    "	background-repeat: no-reperat;\n"
                                    " }")
        self.dateEdit.setCalendarPopup(True)
        self.frame_4 = QFrame(self.mainframe)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(110, 160, 281, 161))
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
        font1 = QFont()
        font1.setFamily(u"Poppins SemiBold")
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 60, 51, 41))
        font2 = QFont()
        font2.setFamily(u"Poppins SemiBold")
        font2.setPointSize(17)
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(127, 20, 71, 16))
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(9)
        self.label_6.setFont(font3)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 130, 201, 16))
        font4 = QFont()
        font4.setFamily(u"Poppins SemiBold")
        font4.setPointSize(8)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color:rgb(207, 206, 218);")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 130, 31, 16))
        font5 = QFont()
        font5.setFamily(u"Poppins SemiBold")
        font5.setPointSize(10)
        self.label_8.setFont(font5)
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
        self.frame_5 = QFrame(self.mainframe)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(411, 160, 281, 161))
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
        self.label_2.setFont(font1)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 130, 111, 16))
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color:rgb(34, 182, 49);")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 221, 41))
        self.label_10.setFont(font2)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(220, 0, 61, 61))
        self.frame_12.setStyleSheet(u"background: transparent;\n"
                                    "background-image: url(F:/books/agriculture project/desktop app/agri/icons8-timer-30.png);\n"
                                    "background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.mainframe)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(712, 160, 281, 161))
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
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(50, 130, 201, 16))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color:rgb(207, 206, 218);")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 60, 251, 41))
        self.label_15.setFont(font2)
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 130, 141, 16))
        self.label_16.setFont(font5)
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
        self.frame_7 = QFrame(self.mainframe)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(1012, 160, 281, 161))
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
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color:rgb(207, 206, 218);")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 60, 51, 41))
        self.label_19.setFont(font2)
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 130, 171, 16))
        self.label_20.setFont(font5)
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
        self.frame_8 = QFrame(self.mainframe)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(110, 360, 581, 291))
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
        self.frame_9 = QFrame(self.mainframe)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(710, 360, 581, 291))
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
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter);
        self.tableWidget.setItem(2, 3, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 70, 581, 191))
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
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label_11 = QLabel(self.mainframe)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(110, 120, 111, 16))
        self.label_11.setFont(font5)
        self.frame_10 = QFrame(self.mainframe)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(884, 29, 457, 61))
        self.frame_10.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "\n"
                                    "}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.deleteButton = QPushButton()
        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 18, 92, 27))
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setIconSize(QSize(16, 16))
        self.pushButton.setIcon(QIcon('F:/books/agriculture project/desktop app/agri/icons8-plus-16(1).png'))
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 18, 161, 27))
        self.frame_3.raise_()
        self.frame_10.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.label_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainframe.setAccessibleDescription("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.label_24.setText(
            QCoreApplication.translate("MainWindow", u"Agriculture Irrigation Desktop App | CARE IUB", None))
        self.closeButton_2.setText("")
        self.minimize_btn_2.setText("")
        self.minimize_btn.setText("")
        self.closeButton.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Crop:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sowing Date:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Soil Type:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"City:", None))
        self.dateEdit.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"sadf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Estimated Water", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"134", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"(mm/day)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"increased compared to last month", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"14%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Next Irrigation Interval", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"See Full Report", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"4d 15h 13min", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Crop Status", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Initial Stage", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"See Full Report", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Days Remaining to Harvest", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"140", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"See Full Report", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Real-Time Data", None))
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
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Crops", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Days Remaining", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Wheat", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"12/10/2021", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Initial", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"143", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Corn", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"12/10/2021", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Initial", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"143", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Crop", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Manage Monitoring Data", None))
