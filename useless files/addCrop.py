import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from datetime import datetime

from ui_add_crop import Ui_MainWindow

import sqlite3

conn = sqlite3.connect("agriculture.db")
conn.row_factory = sqlite3.Row

## eto values from database

city = ''' SELECT * from eto_values '''
 
cur = conn.cursor()
cur.execute(city)    
 
cities = cur.fetchall()

## kc values from database
crop = ''' SELECT * from kc_values '''
 
cur = conn.cursor()
cur.execute(crop)    
 
kc = cur.fetchall()

   
## Soil and its properties from database
soil_database = ''' SELECT * from soil_and_properties '''
 
cur = conn.cursor()
cur.execute(soil_database)    
 
soil_type = cur.fetchall()


class addCropWindow(QtWidgets.QMainWindow):
    submitted = QtCore.Signal(str, str, str, str, str, str, str)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect()

        self.shadow.setBlurRadius(30)

        self.shadow1 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1) 
        self.ui.frame_4.setGraphicsEffect(self.shadow1)
        
        self.ui.frame.setGraphicsEffect(self.shadow)

        # Current Date as defualt date

        
        
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        #self.ui.add_crop_cnfrm.clicked.connect(lambda: self.add_crop())
        self.ui.cancel_btn.pressed.connect(lambda: self.close())

        for crop in kc:
            kc_data = dict(crop)

            print(kc_data['Crops'])         
            
            
            self.ui.crop_comboBox.addItem(kc_data['Crops'])

        # cities comboBox

                
        for city in cities:
            eto_data = dict(city)

            print(eto_data['City'])         
            
            
            
            self.ui.city_comboBox.addItem(eto_data['City'])

        # SOIL COMBOBOX

        for soil in soil_type:
            soil_data = dict(soil)

            print(soil_data['Soil'])
            self.ui.soil_comboBox.addItem(soil_data['Soil'])

        self.ui.add_crop_cnfrm.clicked.connect(self.on_submit)
        self.ui.cancel_btn.clicked.connect(self.close)


        ## EXIT BUTTON

        self.ui.closeButton.clicked.connect(lambda: self.close())

        #minimize 

        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())


        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            
            if e.buttons() == Qt.LeftButton:  
                #Move window 
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        
        self.ui.title_label.mouseMoveEvent = moveWindow

        
        
        # WIDGET TO MOVE
    
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()

    

    def on_submit(self):

        month = self.ui.dateEdit.date().toString("MM")
        day = self.ui.dateEdit.date().toString("dd")
        year = self.ui.dateEdit.date().toString("yyyy")
        self.submitted.emit(
            self.ui.crop_comboBox.currentText(),
            self.ui.dateEdit.date().toString("dd/MM/yyyy"),
            self.ui.city_comboBox.currentText(),
            self.ui.soil_comboBox.currentText(),
            month,
            day,
            year
            )
        self.close()

    # def add_crop (self):
    #     crop_selected = self.ui.crop_comboBox.currentText()
    #     date_selected = self.ui.dateEdit.date().toString("dd/MM/yyyy")
    #     city_selected = self.ui.city_comboBox.currentText()

        # month = self.ui.dateEdit.date().toString("MM")
        # day = self.ui.dateEdit.date().toString("dd")
        # year = self.ui.dateEdit.date().toString("yyyy")
        
    #     if month=='01':
    #         month_name = 'Jan'
    #     if month =='02':
    #         month_name='Feb'
    #     if month =='03':
    #         month_name= 'Mar'
    #     if month == '04':
    #         month_name= 'Apr'
    #     if month == '05':
    #         month_name = 'May'
    #     if month =='06':
    #         month_name = 'Jun'
    #     if month == '07':
    #         month_name= 'Jul'
    #     if month == '08':
    #         month_name = 'Aug'
    #     if month == '09':
    #         month_name = 'Sep'
    #     if month == '10':
    #         month_name = 'Oct'
    #     if month == '11':
    #         month_name = 'Nov'
    #     if month== '12':
    #         month_name = 'Dec'

        
              
            
            
            
            
        
    #     current_mon = int(datetime.today().strftime('%m'))
    #     current_day = int(datetime.today().strftime('%d'))
    #     current_year =int( datetime.today().strftime('%Y'))

    #     # if int(year) > current_year or int(month) > current_mon and :
    #     #     if int(month) > current_mon:
    #     #         if 

    #     # if date_selected > datetime.today().strftime('%d/%m/%Y'):
    #     #     self.ui.label_25.setStyleSheet(u"\n"
    #     #     "color:rgb(255, 102, 82); ")
    #     #     self.ui.label_25.setText('Error: Entered Date is greater than the current date.')
    #     # else:
    #     #     self.ui.label_25.setStyleSheet(u"\n"
    #     #     "color:rgb(34, 182, 49); ")

    #     #     self.ui.label_25.setText('Crop successfully entered.')

        

    #     ## eto value from database

    #     for m in cities:
    #         eto_data = dict(m)
    #         if eto_data['City'] == city_selected and eto_data[month_name]:

    #             eto = eto_data[month_name]

    #             print('et0 = ')
    #             print( eto_data[month_name])   


    #     ## Kc value from database

    #     for c in kc:
    #         kc_data = dict(c)
    #         if kc_data['Crops'] == crop_selected and kc_data[month_name]:

    #             kc_value = kc_data[month_name]

    #             print('kc = ')
    #             print( kc_data[month_name])  
            
                
        
        
    #     #self.ui.label_5.setText(str("{:.2f}".format(eto*kc_value)))

    #     print(crop_selected)
    #     print(date_selected)
    #     print(city_selected)
        
    #     # Create a empty row at bottom of table
    #     # numRows = self.ui.tableWidget.rowCount()
    #     # self.ui.tableWidget.insertRow(numRows)
    #     # # Add text to the row
    #     # self.ui.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(crop_selected))
    #     # self.ui.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(date_selected))
    #     # self.ui.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(city_selected))
    #     # self.ui.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem("Initial"))        

    #     return eto*kc_value