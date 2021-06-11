"""
Uygulamanın arayüz öğelerini tutan modül.
"""

from communation import *
from time import time
from helper import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QVBoxLayout, QWidget, QInputDialog, QMessageBox, QPushButton
from PyQt5 import QtCore, QtWidgets
import PyQt5
import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')


vehicle = None

@exception_handling
def connect_to_vehicle_gui(window, button):
    """
Mavlink protokolü ile araca bağlanılmasını sağlayan fonksiyonun arayüze uygulanması.

Parametreler:

window : Bağlanma penceresinin gösterileceği pencere.
button : Bağlan butonu.
    """

    global vehicle

    o_s = sys.platform

    if "linux" in o_s:

        port, flag = QInputDialog.getText(
            window, 'input dialog', 'Hangi usb portu?')

        port = not flag or "/dev/ttyUSB" + str(port)

    elif o_s == "win32":

        port, flag = QInputDialog.getText(
            window, 'input dialog', 'Hangi com portu?')

        port = not flag or "com" + str(port)

    else:

        raise Exception("OS not supported!")

    if not flag:

        return 0

    vehicle = connect_to_vehicle(str(port))

    if type(vehicle) == str:  # exception handling sıkıntı verirse

        error_popup("Araca bağlanılamadı.", vehicle)

        return 1

    button.setText("Bağlantıyı Kes")


def disconnect_from_vehicle_gui(button):
    """
Mavlink protokolü ile araç bağlantısının kesilmesini sağlayan fonksiyonun arayüze uygulanması.

Parametreler:

button : Bağlan butonu.
    """

    veichle = disconnect_from_vehicle()

    if type(vehicle) == vehicle:  # exception handling sıkıntı verirse

        error_popup("Bağlantı kesilirken bir sorun oluştu.", vehicle)

        return 1

    button.setText("Bağlan")


def switchFailSafe_gui(vehicle):

    if vehicle is not None:

        if hata var:  # exception handling sıkıntı verirse
            pass

    else:
        pass


def changeFlightMode_gui(vehicle, mode: str):

    if vehicle is not None:

        if hata var:  # exception handling sıkıntı verirse
            pass

    else:
        pass


def arm_disarm_gui(vehicle):

    if vehicle is not None:  # exception handling sıkıntı verirse

        if hata var:
            pass

    else:
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


class Window(QWidget):  # varsayılan olarak sekmeler arası geçiş butonları, arm/disarm gibi şeyleri tutacak alttaki de değişcek şekilde ayarla
    """
Uygulamanın ana penceresi.
    """

    def __init__(self, *args, **kwargs):

        super(Window, self).__init__(*args, **kwargs)

        self.title = "Eagle Tech Yer İstasyonu"

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.show()


BUTONLARI AYARLARKEN örn FLİGHTMODE DEĞİŞTİR {vehicle.flightmode} gibi isimler koy

   def telemetry_button(self):

        pass

    def flight_mode_button(self):

        pass

    def arm_disarm_button(self):

        pass

    def map_button(self):

        pass

    def connect_button(self):

        pass


class Telemetry_Window(QWidget):
    """
Telemetri verilerinin görüntülendiği ekran.
    """

    def __init__(self, *args, **kwargs):

        super(Telemetry_Window, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        # self.setCentralWidget(self.canvas)

        self.filters = list(range(7))  # Gösterilmesi istenen öğeler

        self.data_correspondings = {

            0: "Basınç",
            1: "Pil Gerilimi",
            2: "Sıcaklık",
            3: "Yükseklik",
            4: "GPS Yüksekliği",
            5: "Enlem",
            6: "Boylam",
            7: "Paket Numarası",
            8: "Görev Zamanı"
        }

        self.layout = self.set_layout()

    def filter_data(self): ## self.filters ı check box lı bir popup ile güncelle

        pass


    def set_layout(self):

        global vehicle

        if vehicle is not None:


GRAFİK VERİLERİ İÇİN LİMİTED_LİST KULLAN

            n_data = 50
            self.xdata = list(range(n_data))
            self.ydata = [[0 for i in range(n_data)] for j in range(0, 5)]
            self.update_data()

            self.setGeometry(10, 10, 1600, 900)

            self.horizontalGroupBox = QGroupBox("")
            layout = QGridLayout()
            #layout.setColumnStretch(1, 2)
            layout.setColumnStretch(2, 8)

            filter_button = PyQt5.QtWidgets.QPushButton("Filtrele")
            filter_button.clicked.connect(self.filter_data)

            layout.addWidget(PyQt5.QtWidgets.QLabel("Paket Numarası: "), 0, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Görev Zamanı: "), 1, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Yükseklik: "), 2, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Basınç: "), 3, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Sıcaklık: "), 4, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Pil Gerilimi: "), 5, 0)
            layout.addWidget(PyQt5.QtWidgets.QLabel("Yükseklik(GPS): "), 6, 0)
            layout.addWidget(filter_button, 7, 0)
            layout.addWidget(self.canvas, 0, 2, 0, 7)

            GRAFİK VERİLERİ İÇİN LİMİTED_LİST KULLAN

            # BURADA self.veri_adı_label ve self.veri_adı değişkenleri olacak, self.veri_adı_label değişenine veri sürekli self.veri_adı değişkeninden gitcek
            self.packet_num = layout.addWidget(PyQt5.QtWidgets.QLabel("32430"), 0,1)
            self.mission_time = layout.addWidget(PyQt5.QtWidgets.QLabel("450 s"), 1,1)
            self.height_sensor = layout.addWidget(PyQt5.QtWidgets.QLabel("330 m"), 2,1)
            self.pressure = layout.addWidget(PyQt5.QtWidgets.QLabel("202 Pa"), 3,1)
            self.temperature = layout.addWidget(PyQt5.QtWidgets.QLabel("011 °C"),4,1)
            self.voltage = layout.addWidget(PyQt5.QtWidgets.QLabel("10 V"), 5,1)
            self.height_gps = layout.addWidget(PyQt5.QtWidgets.QLabel("10 m"), 6,1)

            self.horizontalGroupBox.setLayout(layout)

            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)

            self.data_timer = QtCore.QTimer()
            self.data_timer.setInterval(1000)
            self.data_timer.timeout.connect(self.update_data)
            self.data_timer.start()

            self.heartbeat_timer = QtCore.QTimer()
            self.heartbeat_timer.setInterval(1000)
            self.heartbeat_timer.timeout.connect(Telemetry_Window.check_heartbeat)
            self.heartbeat_timer.start()

            return windowLayout

            # self.show()




        else:  # BURAYA CİHAZ BAĞLANMADI YAZISI EKLENECEK

            pass

            return not coonected yazısının bulunduğu layout

    @classmethod
    def check_heartbeat(cls):

        global vehicle

        heartbeat = None

        tm = time()

        results = []

        while time() - tm <= 5:

            heartbeat = vehicle.rcv_msg()

            results.append(heartbeat)

        if len(tuple(filter(lambda a : a is not None, results))) <= len(results) * (1/10):  # to control if connection is lost

            vehicle = None

    def update_data(self):
        """
Her belli zaman aralığında ekrandaki telemetri verilerini güncellemek için kullanılan fonksyion.
Şu anda her 1 saniyede bir kez çağrılıyor.
        """

        global vehicle


        if 1:

            data = get_telemetry_data(vehicle)

            if type(data) == str:  # hata olmuşsa

                error_popup("Telemetri Verisi Alınamadı", data)

                return 1

GRAFİK VERİLERİ İÇİN LİMİTED_LİST KULLAN

            # BURDA da değişkenklerin değerlerini değiştir ve kontrol et değişken değiştiğinde labeldaki değer de değişir mi diye değişmiyorsa ekstra değişken olayını
            # boşver, label.settext vs de bak
            for i in range(0,5):
                
                self.ydata[i] = self.ydata[i][1:] + [random.randint(0, 10)]

            self.canvas.axes1.cla()  # Clear the canvas.
            self.canvas.axes2.cla()
            self.canvas.axes1.plot(self.xdata, self.ydata[0], 'r', label="Sıcaklık")
            self.canvas.axes1.plot(self.xdata, self.ydata[1], 'b', label="Pil Gerilimi")

            self.canvas.axes2.plot(self.xdata, self.ydata[2], 'purple', label="Basınç")
            self.canvas.axes2.plot(self.xdata, self.ydata[3], 'orange', label="Yükseklik")

            # HER BAŞARILI TELEMETRY DE MİSSİON TİME A 1 SANİYE, PAKET NUMARASINA packet_per_signal EKLE

            self.canvas.axes1.legend()
            self.canvas.axes2.legend()

            self.canvas.axes1.set_title("Telemetri Verileri - 1")
            self.canvas.axes1.set_xlabel("Zaman (saniye)")
            self.canvas.axes1.set_ylabel("Değer")

            self.canvas.axes2.set_title("Telemetri Verileri - 2")
            self.canvas.axes2.set_xlabel("Zaman (saniye)")
            self.canvas.axes2.set_ylabel("Değer")

            # diğer veriler için de yap

            # Trigger the canvas to update and redraw.
            self.canvas.draw()


class Map_Window(QWidget):
    pass
