import sys
import platform
import traceback
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import queue
import numpy as np
from datetime import datetime, timedelta
import time
import serial
import sqlite3
from Projects.CropsProject.ui_pages import Ui_MainWindow
from Projects.CropsProject.crop_dialog import addCropWindow

conn = sqlite3.connect("agriculture.db")
conn.row_factory = sqlite3.Row

city = ''' SELECT * from eto_values '''

cur = conn.cursor()
cur.execute(city)

cities = cur.fetchall()

crop = ''' SELECT * from kc_values '''

cur = conn.cursor()
cur.execute(crop)

kc = cur.fetchall()

soil = ''' SELECT * from soil_and_properties '''

cur = conn.cursor()
cur.execute(soil)

soil_type = cur.fetchall()

rootDepth = ''' SELECT * from rooting_depth '''

cur = conn.cursor()
cur.execute(rootDepth)

rooting_depth = cur.fetchall()

c_duration = ''' SELECT * from crop_duration '''

cur = conn.cursor()
cur.execute(c_duration)

duration_from_database = cur.fetchall()


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()

        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_color('#1e1953')
        self.axes.spines['left'].set_color('#1e1953')

        self.axes.tick_params(axis='x', colors='#1e1953')
        self.axes.tick_params(axis='y', colors='#1e1953')


time_now = datetime.now()
dateFromAddedDays = (datetime(2021, 4, 4, 20, 10, 9) + timedelta(days=35))
bySubtractingDays = (dateFromAddedDays - datetime.now())


class WorkerSignals(QObject):
    finished = QtCore.Signal()
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(int)


class Worker(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)


        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        worker = Worker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.threadpool.start(worker)

        self.shadow = QGraphicsDropShadowEffect()

        self.shadow.setBlurRadius(30)

        self.ui.frame_31.setGraphicsEffect(self.shadow)

        self.shadow1 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_4.setGraphicsEffect(self.shadow1)

        self.shadow2 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_5.setGraphicsEffect(self.shadow2)

        self.shadow3 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_6.setGraphicsEffect(self.shadow3)

        self.shadow4 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_7.setGraphicsEffect(self.shadow4)

        self.shadow5 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_8.setGraphicsEffect(self.shadow5)

        self.shadow6 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_9.setGraphicsEffect(self.shadow6)

        self.shadow7 = QGraphicsDropShadowEffect(blurRadius=30, xOffset=1, yOffset=1)
        self.ui.frame_33.setGraphicsEffect(self.shadow7)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.previous_value = [0]

        self.ui.verticalScrollBar.setValue(0)
        self.ui.verticalScrollBar.valueChanged.connect(lambda: self.__chnge_position())

        self.ui.closeButton.clicked.connect(lambda: self.close())

        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())

        self.ui.dashboard_side.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page))

        self.ui.report_side.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report_page))

        self.real_time_canvas = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.gridLayout_2.addWidget(self.real_time_canvas)

        x_axis = [0, 2, 1, 4, 7]
        y_axis = [0, 3, 7, 2, 9]

        self.real_time_canvas.axes.yaxis.grid(True, linestyle='--')
        self.real_time_canvas.axes.plot(x_axis, y_axis, '*--')

        self.eto_canvas = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.gridLayout_3.addWidget(self.eto_canvas)

        x_axis = [0, 2, 1, 4, 7]
        y_axis = [0, 3, 7, 2, 9]

        self.eto_canvas.axes.yaxis.grid(True, linestyle='--')
        self.eto_canvas.axes.plot(x_axis, y_axis, '*--')

        self.etc_canvas = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.gridLayout_5.addWidget(self.etc_canvas)

        x_axis = [0, 2, 1, 4, 7]
        y_axis = [0, 3, 7, 2, 9]

        self.etc_canvas.axes.yaxis.grid(True, linestyle='--')
        self.etc_canvas.axes.plot(x_axis, y_axis, '*--')

        self.kc_canvas = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.gridLayout_4.addWidget(self.kc_canvas)

        x_axis = [0, 2, 1, 4, 7]
        y_axis = [0, 3, 7, 2, 9]

        self.kc_canvas.axes.yaxis.grid(True, linestyle='--')
        self.kc_canvas.axes.plot(x_axis, y_axis, '*--')

        for crop in duration_from_database:
            kc_data = dict(crop)

            print(kc_data['Crop'])

        for city in cities:
            eto_data = dict(city)

            print(eto_data['City'])

        self.ui.pushButton.clicked.connect(lambda: self.edit_messages())

        self.ui.pushButton.setIcon(QIcon('F:/books/agriculture project/desktop app/agri/icons8-plus-16(1).png'))

        def moveWindow(e):

            if e.buttons() == Qt.LeftButton:
                # Move window
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.label_24.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    @QtCore.Slot(str, str)
    def update_messages(self, crop_selected, date_selected, city_selected, soil_selected, month, day, year):

        self.crop_selected = crop_selected
        self.date_selected = date_selected
        self.city_selected = city_selected
        self.soil_selected = soil_selected
        self.month = month
        self.day = day
        self.year = year

        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        eto_for_plot = []
        if self.month == '01':
            month_name = 'Jan'
        if self.month == '02':
            month_name = 'Feb'
        if self.month == '03':
            month_name = 'Mar'
        if self.month == '04':
            month_name = 'Apr'
        if self.month == '05':
            month_name = 'May'
        if self.month == '06':
            month_name = 'Jun'
        if self.month == '07':
            month_name = 'Jul'
        if self.month == '08':
            month_name = 'Aug'
        if self.month == '09':
            month_name = 'Sep'
        if self.month == '10':
            month_name = 'Oct'
        if self.month == '11':
            month_name = 'Nov'
        if self.month == '12':
            month_name = 'Dec'

        current_mon = int(datetime.today().strftime('%m'))
        current_day = int(datetime.today().strftime('%d'))
        current_year = int(datetime.today().strftime('%Y'))

        for m in cities:
            eto_data = dict(m)
            if eto_data['City'] == self.city_selected and eto_data[month_name]:
                eto = eto_data[month_name]

                print('et0 = ')
                print(eto_data[month_name])

        self.real_time_canvas = MplCanvas(self, width=10, height=4, dpi=100)
        self.ui.gridLayout.addWidget(self.real_time_canvas)

        x_axis = month_list

        y_axis = [0.8, 1.1, 2, 3.1, 4.2, 5.1, 5.1, 4.7, 3.8, 2.5, 1.4, 0.8]
        self.real_time_canvas.axes.yaxis.grid(True, linestyle='--')

        self.real_time_canvas.axes.plot(x_axis, y_axis, '.--')

        for c in kc:
            kc_data = dict(c)
            if kc_data['Crops'] == self.crop_selected:
                print('kc = ')

                mad_value = kc_data['MAD']

                print('MAD = ')
                print(kc_data['MAD'])

        for aw in soil_type:
            aw_data = dict(aw)
            if aw_data['Soil'] == self.soil_selected:
                aw_value = aw_data['AW mm/m']

                print('AW mm/m = ')
                print(aw_value)

        for depth_ in rooting_depth:

            root_data = dict(depth_)

            if root_data['Crops_'] == self.crop_selected:
                depth_value = root_data['Depth']

                print('Rooting Depth = ')
                print(depth_value)

        ETc = eto

        irrigation_depth = (aw_value * depth_value * mad_value) / 100000
        if ETc != 0:
            irrigation_interval = irrigation_depth / ETc
        else:
            irrigation_depth = 0

        print(irrigation_depth)

        print(irrigation_interval)

        self.ui.label_5.setText(str("{:.2f}".format(ETc)))
        self.ui.label_10.setText(str("{:.2f}".format(irrigation_interval)))

        numRows = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(numRows)
        self.ui.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.crop_selected))
        self.ui.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.date_selected))
        self.ui.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.city_selected))

    def __chnge_position(self):
        scrollBarValue_ = self.ui.verticalScrollBar.value()

        value_before = self.ui.stackedWidget.y()

        len_of_previous = len(self.previous_value)
        if scrollBarValue_ == 0 or scrollBarValue_ == 150:
            if scrollBarValue_ > self.previous_value[len_of_previous - 1]:
                increasing = True
                decreasing = False
                self.previous_value.append(scrollBarValue_)
            if scrollBarValue_ < self.previous_value[len_of_previous - 1]:
                decreasing = True
                increasing = False
                self.previous_value.append(scrollBarValue_)
        else:
            decreasing = False
            increasing = False
        if 29 >= value_before >= -121:
            if increasing:
                self.ui.stackedWidget.setGeometry(self.ui.stackedWidget.x(), value_before - scrollBarValue_,
                                                  self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
            if decreasing:
                self.ui.stackedWidget.setGeometry(self.ui.stackedWidget.x(), value_before + scrollBarValue_ + 150,
                                                  self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
        print(self.previous_value)

    def edit_messages(self):
        self.dialog = addCropWindow()
        self.dialog.submitted.connect(self.update_messages)
        self.dialog.exec_()

    def anim(self):

        self.ui.frame_17.setHidden(True)

        self.card_1 = QPropertyAnimation(self.ui.frame_4, b'geometry')

        self.card_1.setDuration(500)
        self.card_1.setStartValue(QRect(110, 160, 281, 161))
        self.card_1.setEndValue(QRect(110, 210, 281, 161))

        self.card_1.start()

        self.card_2 = QPropertyAnimation(self.ui.frame_5, b'geometry')

        self.card_2.setDuration(500)
        self.card_2.setStartValue(QRect(411, 160, 281, 161))
        self.card_2.setEndValue(QRect(411, 210, 281, 161))

        self.card_2.start()

        self.card_3 = QPropertyAnimation(self.ui.frame_6, b'geometry')

        self.card_3.setDuration(500)
        self.card_3.setStartValue(QRect(712, 160, 281, 161))
        self.card_3.setEndValue(QRect(712, 210, 281, 161))

        self.card_3.start()

        self.card_4 = QPropertyAnimation(self.ui.frame_7, b'geometry')

        self.card_4.setDuration(500)
        self.card_4.setStartValue(QRect(1012, 160, 281, 161))
        self.card_4.setEndValue(QRect(1012, 210, 281, 161))

        self.card_4.start()

        self.card_5 = QPropertyAnimation(self.ui.frame_8, b'geometry')

        self.card_5.setDuration(500)
        self.card_5.setStartValue(QRect(110, 360, 581, 291))
        self.card_5.setEndValue(QRect(110, 410, 581, 291))

        self.card_5.start()

        self.card_6 = QPropertyAnimation(self.ui.frame_9, b'geometry')

        self.card_6.setDuration(500)
        self.card_6.setStartValue(QRect(710, 360, 581, 291))
        self.card_6.setEndValue(QRect(710, 410, 581, 291))

        self.card_6.start()

        self.ui.frame_17.show()

    def progress_fn(self, n):

        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        cnt = 0
        while True:
            cnt += 1
            time.sleep(1)
            bySubtractingSeconds = (bySubtractingDays - timedelta(seconds=cnt))

            days_ = str(bySubtractingSeconds.days)
            hours_ = str(bySubtractingSeconds.seconds // 3600)
            min_ = str((bySubtractingSeconds.seconds // 60) % 60)

            secs_ = str(int(((bySubtractingSeconds.total_seconds()) % 60)))

            print(bySubtractingSeconds)
            self.ui.label_10.setText(f'{days_}d {hours_}h {min_}m {secs_}s')
            progress_callback.emit(cnt)

        return "Done."

    def print_output(self, s):
        pass

    def thread_complete(self):
        pass

    def oh_no(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
