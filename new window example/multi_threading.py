# import sys
# import platform
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
#     QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
#     QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
#     QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.ticker as ticker
# import queue
# import numpy as np

# from datetime import datetime

# import time

# import serial

# import sqlite3

# ## ==> MAIN WINDOW
# from ui_pages import Ui_MainWindow

# from crop_dialog import addCropWindow

# ## ==> Add New Crop

# #from addCrop import addCropWindow

# ## ==> LOGIN





# ## ==> DIALOGE



# # db = sqlite3.connect("agriculture.db")
# # cursor1 = db.cursor1()
# # command = ''' SELECT * from eto_values '''

# # result = cursor1.execute(command)
# # for row_number, data in enumerate(result):
# #     print(row_number, data)

# conn = sqlite3.connect("agriculture.db")
# conn.row_factory = sqlite3.Row

# ## eto values from database

# city = ''' SELECT * from eto_values '''
 
# cur = conn.cursor1()
# cur.execute(city)    
 
# cities = cur.fetchall()

# ## kc values from database
# crop = ''' SELECT * from kc_values '''
 
# cur = conn.cursor1()
# cur.execute(crop)    
 
# kc = cur.fetchall()

   
# ## Soil and its properties from database
# soil = ''' SELECT * from soil_and_properties '''
 
# cur = conn.cursor1()
# cur.execute(soil)    
 
# soil_type = cur.fetchall()

# ## Rooting Depth from database
# rootDepth = ''' SELECT * from rooting_depth '''
 
# cur = conn.cursor1()
# cur.execute(rootDepth)    
 
# rooting_depth = cur.fetchall()


# ## Durations from database
# c_duration = ''' SELECT * from crop_duration '''
 
# cur = conn.cursor1()
# cur.execute(c_duration)    
 
# duration_from_database = cur.fetchall()



# ## Add Crop Window



# class MplCanvas(FigureCanvas):
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)
#         fig.tight_layout()

#         self.axes.spines['top'].set_visible(False)
#         self.axes.spines['right'].set_visible(False)
#         self.axes.spines['bottom'].set_color('#1e1953')
#         self.axes.spines['left'].set_color('#1e1953')

#         self.axes.tick_params(axis='x', colors='#1e1953')
#         self.axes.tick_params(axis='y', colors='#1e1953')
#         # self.axes.spines['left'].set_visible(False)
#         # self.axes.spines['bottom'].set_visible(False)

        

    
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

#         self.shadow = QGraphicsDropShadowEffect()

#         self.shadow.setBlurRadius(30)

#         self.ui.frame_31.setGraphicsEffect(self.shadow)

#         self.shadow1 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_4.setGraphicsEffect(self.shadow1)

#         self.shadow2 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_5.setGraphicsEffect(self.shadow2)

#         self.shadow3 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_6.setGraphicsEffect(self.shadow3)

#         self.shadow4 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_7.setGraphicsEffect(self.shadow4)

#         self.shadow5 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_8.setGraphicsEffect(self.shadow5)

#         self.shadow6 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_9.setGraphicsEffect(self.shadow6)

#         self.shadow7 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
#         self.ui.frame_33.setGraphicsEffect(self.shadow7)


        
#         # self.ui.frame_6.setGraphicsEffect(self.shadow1)
#         # self.ui.frame_7.setGraphicsEffect(self.shadow1)


#         ## For QTABLE WIDGET

#         self.ui.tableWidget.resizeColumnsToContents()
#         self.ui.tableWidget.resizeRowsToContents()
#         self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        
#         ## ScrollBars

        

#         self.previous_value = [0]

        

        

#         # connet the scroll bar signle to our slot

#         self.ui.verticalScrollBar.setValue(0)
#         self.ui.verticalScrollBar.valueChanged.connect(lambda: self.__chnge_position())

        
        

    
        
        
#         ## EXIT BUTTON

#         self.ui.closeButton.clicked.connect(lambda: self.close())

#         #minimize 

#         self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        
#         ## PAGES

#         self.ui.dashboard_side.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page))

#         self.ui.report_side.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report_page))

#         #self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database_page))

#         #self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signin_page))
#         # crops comboBox

#         ## real-time dashboad graph

#         # self.real_time_canvas = MplCanvas(self, width=10, height=4, dpi=100)
#         # self.ui.gridLayout.addWidget(self.real_time_canvas)
        
#         # x_axis = [0, 2, 1, 4, 7]
#         # y_axis = [0, 3, 7, 2, 9]

#         # self.real_time_canvas.axes.yaxis.grid(True,linestyle='--')

        
#         # self.real_time_canvas.axes.plot(x_axis, y_axis , '.--')

#         ## real-time report page graph

#         self.real_time_canvas = MplCanvas(self, width=10, height=4, dpi=100)
#         self.ui.gridLayout_2.addWidget(self.real_time_canvas)
        
#         x_axis = [0, 2, 1, 4, 7]
#         y_axis = [0, 3, 7, 2, 9]

#         self.real_time_canvas.axes.yaxis.grid(True,linestyle='--')
#         self.real_time_canvas.axes.plot(x_axis, y_axis , '*--')


#         ## et0 graph

#         self.eto_canvas = MplCanvas(self, width=10, height=4, dpi=100)
#         self.ui.gridLayout_3.addWidget(self.eto_canvas)
        
#         x_axis = [0, 2, 1, 4, 7]
#         y_axis = [0, 3, 7, 2, 9]

#         self.eto_canvas.axes.yaxis.grid(True,linestyle='--')
#         self.eto_canvas.axes.plot(x_axis, y_axis , '*--')


#         ## etc graph

#         self.etc_canvas = MplCanvas(self, width=10, height=4, dpi=100)
#         self.ui.gridLayout_5.addWidget(self.etc_canvas)
        
#         x_axis = [0, 2, 1, 4, 7]
#         y_axis = [0, 3, 7, 2, 9]

#         self.etc_canvas.axes.yaxis.grid(True,linestyle='--')
#         self.etc_canvas.axes.plot(x_axis, y_axis , '*--')

#         ## kc graph

#         self.kc_canvas = MplCanvas(self, width=10, height=4, dpi=100)
#         self.ui.gridLayout_4.addWidget(self.kc_canvas)
        
#         x_axis = [0, 2, 1, 4, 7]
#         y_axis = [0, 3, 7, 2, 9]

#         self.kc_canvas.axes.yaxis.grid(True,linestyle='--')
#         self.kc_canvas.axes.plot(x_axis, y_axis , '*--')
        
#         for crop in kc:
#             kc_data = dict(crop)

#             print(kc_data['Crops'])         
            
            
#             #self.ui.co.addItem(kc_data['Crops'])

#         # cities comboBox

                
#         for city in cities:
#             eto_data = dict(city)

#             print(eto_data['City'])         
            
            
            
#             #self.ui.comboBox_4.addItem(eto_data['City'])

#         # SOIL COMBOBOX

#         #for soil in soil_types:
#             #self.ui.comboBox_3.addItem(soil)

        
#         # add crop button

#         #self.ui.pushButton.clicked.connect(lambda: self.add_crop())

#         self.ui.pushButton.clicked.connect(lambda: self.edit_messages())

#         self.ui.pushButton.setIcon(QIcon('F:/books/agriculture project/desktop app/agri/icons8-plus-16(1).png'))

        
        

        
        

        

#         #self.ui.pushButton_2.clicked.connect(lambda: self.anim())

#         #self.ui.pushButton.clicked.connect(lambda: self.anim())

        
#         def moveWindow(e):
#             # Detect if the window is  normal size
#             # ###############################################  
            
#             if e.buttons() == Qt.LeftButton:  
#                 #Move window 
#                 self.move(self.pos() + e.globalPos() - self.clickPosition)
#                 self.clickPosition = e.globalPos()
#                 e.accept()
        
#         self.ui.label_24.mouseMoveEvent = moveWindow

        
        
#         # WIDGET TO MOVE
    
#     def mousePressEvent(self, event):
#         # ###############################################
#         # Get the current position of the mouse
#         self.clickPosition = event.globalPos()



#     ## Add New Crop

#     # def add_crop_btn (self):
#     #     self.crop_window = addCropWindow()
#     #     self.crop_window.show()

#     @QtCore.Slot(str, str)
#     def update_messages(self, crop_selected, date_selected, city_selected, soil_selected, month, day, year):
        
#         self.crop_selected = crop_selected
#         self.date_selected = date_selected
#         self.city_selected = city_selected
#         self.soil_selected = soil_selected
#         self.month = month
#         self.day = day
#         self.year = year
        
#         month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#         eto_for_plot = []
#         if self.month=='01':
#             month_name = 'Jan'
#         if self.month =='02':
#             month_name='Feb'
#         if self.month =='03':
#             month_name= 'Mar'
#         if self.month == '04':
#             month_name= 'Apr'
#         if self.month == '05':
#             month_name = 'May'
#         if self.month =='06':
#             month_name = 'Jun'
#         if self.month == '07':
#             month_name= 'Jul'
#         if self.month == '08':
#             month_name = 'Aug'
#         if self.month == '09':
#             month_name = 'Sep'
#         if self.month == '10':
#             month_name = 'Oct'
#         if self.month == '11':
#             month_name = 'Nov'
#         if self.month== '12':
#             month_name = 'Dec'

        
              
            
            
            
            
        
#         current_mon = int(datetime.today().strftime('%m'))
#         current_day = int(datetime.today().strftime('%d'))
#         current_year =int( datetime.today().strftime('%Y'))

#         # if int(year) > current_year or int(month) > current_mon and :
#         #     if int(month) > current_mon:
#         #         if 

#         # if date_selected > datetime.today().strftime('%d/%m/%Y'):
#         #     self.ui.label_25.setStyleSheet(u"\n"
#         #     "color:rgb(255, 102, 82); ")
#         #     self.ui.label_25.setText('Error: Entered Date is greater than the current date.')
#         # else:
#         #     self.ui.label_25.setStyleSheet(u"\n"
#         #     "color:rgb(34, 182, 49); ")

#         #     self.ui.label_25.setText('Crop successfully entered.')

        

#         ## eto value from database

#         for m in cities:
#             eto_data = dict(m)
#             if eto_data['City'] == self.city_selected and eto_data[month_name]:

#                 eto = eto_data[month_name]

#                 print('et0 = ')
#                 print( eto_data[month_name])   



#         ## real-time dashboad graph

#         self.real_time_canvas = MplCanvas(self, width=10, height=4, dpi=100)
#         self.ui.gridLayout.addWidget(self.real_time_canvas)

#         # i = 0
#         # for m_ in cities:
#         #     eto_data = dict(m_)
#         #     if eto_data['City'] == self.city_selected:
#         #         eto_for_plot.append(eto_data[month_list[i]])
#         #     i+=1
#         x_axis = month_list
        
#         y_axis = [0.8, 1.1, 2, 3.1, 4.2, 5.1, 5.1, 4.7, 3.8, 2.5, 1.4, 0.8]
#         self.real_time_canvas.axes.yaxis.grid(True,linestyle='--')

        
#         self.real_time_canvas.axes.plot(x_axis, y_axis , '.--')
#         ## Kc value from database

#         for c in kc:
#             kc_data = dict(c)
#             if kc_data['Crops'] == self.crop_selected:
                
#                 if kc_data[month_name] == None:
#                     kc_value = 1
#                     mad_value = 1
#                     print('null') 
#                 else:
#                     print('kc = ')
#                     print( kc_data[month_name]) 

#                     kc_value = kc_data[month_name]
#                     mad_value = kc_data['MAD']

#                     print('MAD = ')
#                     print( kc_data['MAD']) 
                    


#         ## Available Water AW mm/m

#         for aw in soil_type:
#             aw_data = dict(aw)
#             if aw_data['Soil'] == self.soil_selected:

#                 aw_value = aw_data['AW mm/m']

#                 print('AW mm/m = ')
#                 print(aw_value)  

#         ## Available Water AW mm/m

#         for depth_ in rooting_depth:

            
#             root_data = dict(depth_)
            
#             if root_data['Crops_'] == self.crop_selected:

#                 depth_value = root_data['Depth']

#                 print('Rooting Depth = ')
#                 print(depth_value)      
                
        
#         ETc = eto*kc_value

#         irrigation_depth = (aw_value*depth_value*mad_value)/100000
#         if ETc != 0:
#             irrigation_interval = irrigation_depth/ETc
#         else:
#             irrigation_depth = 0

#         print(irrigation_depth)

#         print(irrigation_interval)

#         self.ui.label_5.setText(str("{:.2f}".format(ETc)))
#         self.ui.label_10.setText(str("{:.2f}".format(irrigation_interval)))


        
        
#         # Create a empty row at bottom of table
#         numRows = self.ui.tableWidget.rowCount()
#         self.ui.tableWidget.insertRow(numRows)
#         # Add text to the row
#         self.ui.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.crop_selected))
#         self.ui.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.date_selected))
#         self.ui.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.city_selected))
#         # self.ui.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem("Initial")) 

        
#     def __chnge_position(self):
#         #slot to change the scroll bar  position of all table
#         scrollBarValue_ = self.ui.verticalScrollBar.value()

        
#         value_before = self.ui.stackedWidget.y()

#         len_of_previous = len(self.previous_value)
#         if scrollBarValue_ == 0 or scrollBarValue_ == 150:
#             if scrollBarValue_ > self.previous_value[len_of_previous-1]:

#                 increasing = True
#                 decreasing = False
#                 self.previous_value.append(scrollBarValue_)
#             if scrollBarValue_ < self.previous_value[len_of_previous-1]:
#                 decreasing = True
#                 increasing = False
#                 self.previous_value.append(scrollBarValue_)
#         else:
#             decreasing = False
#             increasing = False
#         if value_before <= 29 and value_before >=-121:
#             if increasing:
#                 self.ui.stackedWidget.setGeometry(self.ui.stackedWidget.x(), value_before - scrollBarValue_, self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
#             if decreasing:
#                 self.ui.stackedWidget.setGeometry(self.ui.stackedWidget.x(), value_before + scrollBarValue_ + 150, self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
#         print(self.previous_value)
        

#     def edit_messages(self):
#         self.dialog = addCropWindow()
#         #self.dialog.set_messages(self.message_a, self.message_b)
#         self.dialog.submitted.connect(self.update_messages)
#         self.dialog.exec_()

#     def anim(self):

        
#         self.ui.frame_17.setHidden(True)

#         self.card_1 = QPropertyAnimation(self.ui.frame_4, b'geometry')

#         self.card_1.setDuration(500)
#         self.card_1.setStartValue(QRect(110, 160, 281, 161))
#         self.card_1.setEndValue(QRect(110, 210, 281, 161))

#         self.card_1.start()

#         self.card_2 = QPropertyAnimation(self.ui.frame_5, b'geometry')

#         self.card_2.setDuration(500)
#         self.card_2.setStartValue(QRect(411, 160, 281, 161))
#         self.card_2.setEndValue(QRect(411, 210, 281, 161))

#         self.card_2.start()

#         self.card_3 = QPropertyAnimation(self.ui.frame_6, b'geometry')

#         self.card_3.setDuration(500)
#         self.card_3.setStartValue(QRect(712, 160, 281, 161))
#         self.card_3.setEndValue(QRect(712, 210, 281, 161))

#         self.card_3.start()

#         self.card_4 = QPropertyAnimation(self.ui.frame_7, b'geometry')

#         self.card_4.setDuration(500)
#         self.card_4.setStartValue(QRect(1012, 160, 281, 161))
#         self.card_4.setEndValue(QRect(1012, 210, 281, 161))

#         self.card_4.start()

#         self.card_5 = QPropertyAnimation(self.ui.frame_8, b'geometry')

#         self.card_5.setDuration(500)
#         self.card_5.setStartValue(QRect(110, 360, 581, 291))
#         self.card_5.setEndValue(QRect(110, 410, 581, 291))

#         self.card_5.start()

#         self.card_6 = QPropertyAnimation(self.ui.frame_9, b'geometry')

#         self.card_6.setDuration(500)
#         self.card_6.setStartValue(QRect(710, 360, 581, 291))
#         self.card_6.setEndValue(QRect(710, 410, 581, 291))

#         self.card_6.start()

#         self.ui.frame_17.show()

            
        
        

#         # time.sleep(2)

#         # self.ui.frame_17.hide()

#         # self.card_1 = QPropertyAnimation(self.ui.frame_4, b'geometry')

#         # self.card_1.setDuration(500)
#         # self.card_1.setStartValue(QRect(110, 210, 281, 161))
#         # self.card_1.setEndValue(QRect(110, 160, 281, 161))
        

#         # self.card_1.start()

#         # self.card_2 = QPropertyAnimation(self.ui.frame_5, b'geometry')

#         # self.card_2.setDuration(500)
#         # self.card_2.setStartValue(QRect(411, 160, 281, 161))
#         # self.card_2.setEndValue(QRect(411, 210, 281, 161))

#         # self.card_2.start()

#         # self.card_3 = QPropertyAnimation(self.ui.frame_6, b'geometry')

#         # self.card_3.setDuration(500)
#         # self.card_3.setStartValue(QRect(712, 160, 281, 161))
#         # self.card_3.setEndValue(QRect(712, 210, 281, 161))

#         # self.card_3.start()

#         # self.card_4 = QPropertyAnimation(self.ui.frame_7, b'geometry')

#         # self.card_4.setDuration(500)
#         # self.card_4.setStartValue(QRect(1012, 160, 281, 161))
#         # self.card_4.setEndValue(QRect(1012, 210, 281, 161))

#         # self.card_4.start()

#         # self.card_5 = QPropertyAnimation(self.ui.frame_8, b'geometry')

#         # self.card_5.setDuration(500)
#         # self.card_5.setStartValue(QRect(110, 360, 581, 291))
#         # self.card_5.setEndValue(QRect(110, 410, 581, 291))

#         # self.card_5.start()

#         # self.card_6 = QPropertyAnimation(self.ui.frame_9, b'geometry')

#         # self.card_6.setDuration(500)
#         # self.card_6.setStartValue(QRect(710, 360, 581, 291))
#         # self.card_6.setEndValue(QRect(710, 410, 581, 291))

#         # self.card_6.start()

            

            

#         # self.notification = QPropertyAnimation(self.ui.frame_17, b'geometry')

#         # self.notification.setDuration(500)
#         # self.notification.setStartValue(QRect(61, -31, 821, 61))
#         # self.notification.setEndValue(QRect(320, 140, 651, 41))

#         # self.notification.start()

    

    

        
        
        

#         # Row Delete button
        

      

    



    
    
# if __name__ == "__main__":
#     app= QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# from datetime import datetime, timedelta


# date_now_more_5_days = (datetime.now() + timedelta(days=140) ).strftime('%Y-%m-%d')

# print(date_now_more_5_days)


from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import time
import traceback, sys


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)




class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done



class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n*100/4)

        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def oh_no(self):
        # Pass the function to execute
        worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)


    def recurring_timer(self):
        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec_()