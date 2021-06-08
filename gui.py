"""
Uygulamanın arayüz öğelerini tutan modül.
"""

import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from communation import *

veichle = None  

def connect_to_veichle_gui(connectipn_string : str):
    pass

def disconnect_from_veichle_gui():
    pass

def switchFailSafe_gui(): ## global drone belirt 
    pass


def changeFlightMode_gui(): ## global drone belirt 
    pass


def arm_disarm_gui(): ## global drone belirt 
    pass



class Popup():
    """
İstendiğinde popup ekranını istenilen ögelerle bezeyip gösteren sınıf.     
    """
    pass


class MplCanvas(FigureCanvas):
    """
Açıklama eklenecek.
    """

    def __init__(self, parent=None, width=8, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(121)
        self.axes2 = fig.add_subplot(122)
        super(MplCanvas, self).__init__(fig)

class Window(QWidget): ## varsayılan olarak sekmeler arası geçiş butonları, arm/disarm gibi şeyleri tutacak alttaki de değişcek şekilde ayarla
    """
Uygulamanın ana penceresi.
    """

    def __init__(self, *args, **kwargs):

        super(Window, self).__init__(*args, **kwargs)
        
        self.title = "Eagle Tech Yer İstasyonu"

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)


class Telemetry_Window(QWidget):
    """
Telemetri verilerinin görüntülendiği ekran.
    """


    def __init__(self, *args, **kwargs):

        super(Telemetry_Window, self).__init__(*args, **kwargs)

        self.title = "Eagle Tech Yer İstasyonu"

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        #self.setCentralWidget(self.canvas)

        self.set_layout()


    def set_layout(self):
        
        global veichle

        if veichle is not None:

            n_data = 50
            self.xdata = list(range(n_data))
            self.ydata = [[random.randint(0, 10) for i in range(n_data)] for j in range(0,5)]
            self.update_data()

            self.setWindowTitle(self.title)
            self.setGeometry(10, 10, 1600, 900)

            self.horizontalGroupBox = QGroupBox("")
            layout = QGridLayout()
            #layout.setColumnStretch(1, 2)
            layout.setColumnStretch(2, 8)

            layout.addWidget(PyQt5.QtWidgets.QLabel("Paket Numarası: "), 0, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Görev Zamanı: "), 1, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Yükseklik: "), 2, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Basınç: "), 3, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Sıcaklık: "), 4, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Pil Gerilimi: "), 5, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Yükseklik(GPS): "), 6, 0)
            layout.addWidget(self.canvas, 0, 2, 0, 7)


            ## BURADA self.veri_adı_label ve self.veri_adı değişkenleri olacak, self.veri_adı_label değişenine veri sürekli self.veri_adı değişkeninden gitcek
            self.packet_num = layout.addWidget(PyQt5.QtWidgets.QLabel("32430"),0,1)
            self.mission_time = layout.addWidget(PyQt5.QtWidgets.QLabel("450 s"),1,1)
            self.height_sensor = layout.addWidget(PyQt5.QtWidgets.QLabel("330 m"),2,1)
            self.pressure = layout.addWidget(PyQt5.QtWidgets.QLabel("202 Pa"),3,1)
            self.temperature =layout.addWidget(PyQt5.QtWidgets.QLabel("011 °C"),4,1)
            self.voltage = layout.addWidget(PyQt5.QtWidgets.QLabel("10 V"),5,1)
            self.height_gps = layout.addWidget(PyQt5.QtWidgets.QLabel("10 m"),6,1)

            self.horizontalGroupBox.setLayout(layout)


            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)
            self.setLayout(windowLayout)
            self.show()
            # Setup a timer to trigger the redraw by calling update_plot.
            self.timer = QtCore.QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.update_data)
            self.timer.start()

        else: ## BURAYA CİHAZ BAĞLANMADI YAZISI EKLENECEK
            
            pass 

    def update_data(self, layout_code : int = None):

        global veichle

        layout_code = layout_code or self.default_layout_code

        if layout_code == 0:

            data = get_telemetry_data(veichle)

            if type(data) == str: 
            ## Error mesajını popup olarak vermeyi ekle ayrıca bisürü error mesajının dolmasını engellemek için o an ekranda başka popup olup olmadığına da bak
            ## bisürü dosya ile dolmasını engellemek için logs dosyasının önlemler al, communciation lost, communucation şeylerinde bak bunlara
                pass

            
            
            ## BURDA da değişkenklerin değerlerini değiştir ve kontrol et değişken değiştiğinde labeldaki değer de değişir mi diye değişmiyorsa ekstra değişken olayını
            ## boşver, label.settext vs de bak
            for i in range(0,5): self.ydata[i] = self.ydata[i][1:] + [random.randint(0, 10)]
            self.canvas.axes1.cla()  # Clear the canvas.
            self.canvas.axes2.cla()
            self.canvas.axes1.plot(self.xdata, self.ydata[0], 'r', label="Sıcaklık")
            self.canvas.axes1.plot(self.xdata, self.ydata[1], 'b', label="Pil Gerilimi")

            self.canvas.axes2.plot(self.xdata, self.ydata[2], 'purple', label="Basınç")
            self.canvas.axes2.plot(self.xdata, self.ydata[3], 'orange', label="Yükseklik")
            
            ## HER BAŞARILI TELEMETRY DE MİSSİON TİME A 1 SANİYE, PAKET NUMARASINA packet_per_signal EKLE

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


