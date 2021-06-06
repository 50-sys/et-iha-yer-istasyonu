import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=8, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(121)
        self.axes2 = fig.add_subplot(122)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.title = "Eagle Tech Yer İstasyonu"

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        #self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [[random.randint(0, 10) for i in range(n_data)] for j in range(0,5)]
        self.update_plot()

        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 1600, 900)

        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        #layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 8)
        a = 10

        layout.addWidget(PyQt5.QtWidgets.QLabel("Paket Numarası: "), 0, 0)
        layout.addWidget(PyQt5.QtWidgets.QLabel("Görev Zamanı: "), 1, 0)
        layout.addWidget(PyQt5.QtWidgets.QLabel("Yükseklik: "), 2, 0)
        layout.addWidget(PyQt5.QtWidgets.QLabel("Basınç: "), 3, 0)
        layout.addWidget(PyQt5.QtWidgets.QLabel("Sıcaklık: "), 4, 0)
        layout.addWidget(PyQt5.QtWidgets.QLabel("Pil Gerilimi: "), 5, 0)
        layout.addWidget(PyQt5.QtWidgets.QLabel("Yükseklik(GPS): "), 6, 0)
        layout.addWidget(self.canvas, 0, 2, 0, 7)
        self.packet_num = layout.addWidget(PyQt5.QtWidgets.QLabel("32430"),0,1)
        self.mission_time = layout.addWidget(PyQt5.QtWidgets.QLabel("450 s"),1,1)
        self.height_sensor = layout.addWidget(PyQt5.QtWidgets.QLabel("330 m"),2,1)
        self.pressure = layout.addWidget(PyQt5.QtWidgets.QLabel("202 Pa"),3,1)
        self.temperature =layout.addWidget(PyQt5.QtWidgets.QLabel("011 °C"),4,1)
        self.voltage = layout.addWidget(PyQt5.QtWidgets.QLabel(str(a) + " V"),5,1)
        self.height_gps = layout.addWidget(PyQt5.QtWidgets.QLabel("10 m"),6,1)

        self.horizontalGroupBox.setLayout(layout)


        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)        
        self.timer.start()


    def update_plot(self):
        # Drop off the first y element, append a new one.
        for i in range(0,5): self.ydata[i] = self.ydata[i][1:] + [random.randint(0, 10)]
        self.canvas.axes1.cla()  # Clear the canvas.
        self.canvas.axes2.cla()
        sıcaklık = sıcaklıkverisinial()
        self.canvas.axes1.plot(self.xdata, sıcaklık, 'r', label="Sıcaklık")
        self.canvas.axes1.plot(self.xdata, self.ydata[1], 'b', label="Pil Gerilimi")

        self.canvas.axes2.plot(self.xdata, self.ydata[2], 'purple', label="Basınç")
        self.canvas.axes2.plot(self.xdata, self.ydata[3], 'orange', label="Yükseklik")

        self.canvas.axes1.legend()
        self.canvas.axes2.legend()

        self.canvas.axes1.set_title("Telemetri Verileri")
        self.canvas.axes1.set_xlabel("Zaman (saniye)")
        self.canvas.axes1.set_ylabel("Değer")

        self.canvas.axes2.set_title("Telemetri Verileri")
        self.canvas.axes2.set_xlabel("Zaman (saniye)")
        self.canvas.axes2.set_ylabel("Değer")

        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
