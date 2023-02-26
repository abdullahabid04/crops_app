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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1, 1, 530, 31))
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
        self.title_label = QLabel(self.frame_2)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(50, 7, 381, 21))
        font = QFont()
        font.setFamily(u"Poppins")
        self.title_label.setFont(font)
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(430, 0, 101, 31))
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 532, 341))
        self.frame.setStyleSheet(u"QFrame{\n"
                                 "background-color: rgb(246, 247, 249);\n"
                                 "color:rgb(30, 25, 83);\n"
                                 "border: 1px solid rgb(163, 163, 163);\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(3, 31, 528, 301))
        self.frame_3.setStyleSheet(u"QFrame{\n"
                                   "border:none;\n"
                                   "}\n"
                                   "\n"
                                   "QLineEdit{\n"
                                   "border: 1px solid rgb(215, 215, 219);\n"
                                   "border-radius: 5px;\n"
                                   "color:rgb(30, 25, 83);\n"
                                   "}\n"
                                   "QLineEdit:hover {\n"
                                   "	\n"
                                   "	border: 2px solid rgb(229, 229, 234);\n"
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
                                   "	"
                                   "width: 25px; \n"
                                   "	\n"
                                   "	border-left-width: 1px;\n"
                                   "	border-left-color: rgb(229, 229, 234);\n"
                                   "	border-left-style: solid;\n"
                                   "	border-top-right-radius: 3px;\n"
                                   "	border-bottom-right-radius: 3px;	\n"
                                   "	\n"
                                   "	background-position: center;\n"
                                   "	background-repeat: no-reperat;\n"
                                   " }\n"
                                   "")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.add_crop_cnfrm = QPushButton(self.frame_3)
        self.add_crop_cnfrm.setObjectName(u"add_crop_cnfrm")
        self.add_crop_cnfrm.setGeometry(QRect(271, 240, 92, 27))
        self.add_crop_cnfrm.setStyleSheet(u"")
        self.add_crop_cnfrm.setIconSize(QSize(16, 16))
        self.cancel_btn = QPushButton(self.frame_3)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(160, 240, 92, 27))
        self.cancel_btn.setStyleSheet(u"")
        self.cancel_btn.setIconSize(QSize(16, 16))
        self.frame_32 = QFrame(self.frame_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(-1, 0, 529, 41))
        self.frame_32.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(255, 255, 255);\n"
                                    "\n"
                                    "}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_48 = QLabel(self.frame_32)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(49, 14, 111, 16))
        font1 = QFont()
        font1.setFamily(u"Poppins SemiBold")
        font1.setPointSize(10)
        self.label_48.setFont(font1)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(120, 70, 281, 211))
        self.frame_4.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius:10px;\n"
                                   "\n"
                                   "\n"
                                   "}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 20, 113, 27))
        self.cancel_btn_2 = QPushButton(self.frame_4)
        self.cancel_btn_2.setObjectName(u"cancel_btn_2")
        self.cancel_btn_2.setGeometry(QRect(162, 110, 91, 27))
        self.cancel_btn_2.setStyleSheet(u"QPushButton{\n"
                                        "background-color:transparent;\n"
                                        "border:none;\n"
                                        "color: rgb(0, 108, 162);\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "	\n"
                                        "color: rgb(0, 170, 255);\n"
                                        "}")
        self.cancel_btn_2.setIconSize(QSize(16, 16))
        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 80, 113, 27))
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(34, 86, 61, 16))
        self.label_21.setFont(font)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 25, 61, 20))
        self.label_13.setFont(font)
        self.frame_4.raise_()
        self.add_crop_cnfrm.raise_()
        self.cancel_btn.raise_()
        self.frame_32.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.frame_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(
            QCoreApplication.translate("MainWindow", u"Agriculture Irrigation Desktop App | CARE IUB | Login", None))
        self.closeButton_2.setText("")
        self.minimize_btn_2.setText("")
        self.minimize_btn.setText("")
        self.closeButton.setText("")
        self.add_crop_cnfrm.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit.setText("")
        self.cancel_btn_2.setText(QCoreApplication.translate("MainWindow", u"Forgot Password.", None))
        self.lineEdit_2.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
