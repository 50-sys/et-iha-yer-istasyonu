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

        self.telemetry_layout = Telemetry_Layout()
        self.map_layout =  Map_Layout()

        
        self.heartbeat_timer = QtCore.QTimer()
        self.heartbeat_timer.setInterval(1000)
        self.heartbeat_timer.timeout.connect(self.check_heartbeat)
        self.heartbeat_timer.start()


BUTONLARI AYARLARKEN örn FLİGHTMODE DEĞİŞTİR {vehicle.flightmode} gibi isimler koy


    
    def check_heartbeat(self):

        global vehicle

        heartbeat = None

        tm = time()

        results = []

        while time() - tm <= 5:

            heartbeat = vehicle.rcv_msg()

            results.append(heartbeat)

        if len(tuple(filter(lambda a : a is not None, results))) <= len(results) * (1/10):  # control if connection lost

            vehicle = None
            self.telemetry_layout.reset() ## reseting all telemetry values
            


    @exception_handling
    def connect_to_vehicle_gui(self, button):
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
                self, 'input dialog', 'Hangi usb portu?')

            port = not flag or "/dev/ttyUSB" + str(port)

        elif o_s == "win32":

            port, flag = QInputDialog.getText(
                self, 'input dialog', 'Hangi com portu?')

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


    def disconnect_from_vehicle_gui(self, button):
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
        self.telemetry_layout.reset()


    def switchFailSafe_gui(self, vehicle):

        if vehicle is not None:

            if hata var:  # exception handling sıkıntı verirse
                pass

        else:
            pass


    def changeFlightMode_gui(self, vehicle, mode: str):

        if vehicle is not None:

            if hata var:  # exception handling sıkıntı verirse
                pass

        else:
            pass


    def arm_disarm_gui(self, vehicle): if mode alındı to arm modu :  telemetrty_layout.reset([8]) yap

        if vehicle is not None:  # exception handling sıkıntı verirse

            if hata var:
                pass

        else:
            pass

class Telemetry_Layout(QWidget):
    
    """
Telemetri verilerinin görüntülendiği ekran.
    """

    def __init__(self, *args, **kwargs): ## her verinin değişkeni ve de label, graphi içimn değişkenler

        super(Telemetry_Layout, self).__init__(*args, **kwargs)

        self.filters_database_name = os.getcwd() + "filters.csv" ## path of file that stores current filters for telemetry data
        self.data_count = 9 ## count of telemetry data 

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        # self.setCentralWidget(self.canvas)

        try:

            
            with open(self.filters_database_name) as file:

                self.filters = file.read().split(",")

        except:

            with open(self.filters_database_name, "w+") as file:

                file.write(",".join(list(range(self.data_count))))
                
            filters = list(range(self.data_count))


        ## demetin ilk elemanı değişkenin değeri, ikincisi ekranda gösterilecek ad, üçüncüsü de gui da konumu
        # KONUMDA : (x, y) = x row, y column. ("g", x, y) = "g" = grafik, x grafik numarası, y eksen numarası.
        self.datas = { 

            0 : (Limited_List(50, 1, none_item = 0), "Basınç", ("g", 0, 0)), 
            1 : (Limited_List(50, 1, none_item = 0), "Pil Gerilimi", ("g", 0, 1)),
            2 : (Limited_List(50, 1, none_item = 0), "Sıcaklık", ("g", 1, 0)),
            3 : (Limited_List(50, 1, none_item = 0), "Yükseklik", ("g", 1, 1)),
            4 : (0, "GPS Yüksekliği", (0, 1)),
            5 : (0, "Enlem", (0, 2)),
            6 : (0, "Boylam", (0, 3)),
            7 : (0, "Paket Numarası", (0, 4)),
            8 : (0, "Görev Zamanı", (0, 5))
        }

   


        self.layout = self.get_layout()

    def reset_data(self, data_to_reset = None):

        """
Aracın bağlantısı kopruğunda tüm verileri sıfırlayan fonksiyon.
        """

        data_to_reset = data_to_reset or range(self.data_count)
        
        for i in data_to_reset:

            data = self.datas[i]

            if data[2][0] == "g":

                data[0] = Limited_List(50, 1, none_item = 0) ## assigning new list
 
            else:

                data[0] = 0 ## assigning new value



    def filter_data(self): ## self.filters ı check box lı bir popup ile güncelle

        pass ## csv dosyasını güncellemeyi de ekle

    def get_layout(self):

        global vehicle

        if vehicle is not None:

            self.__INTERVAL_of_GRAPHS = 50 ## the time from past to which the oldest data belongs 

            
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


            return windowLayout

            # self.show()




        else:  # BURAYA CİHAZ BAĞLANMADI YAZISI EKLENECEK

            pass

            return not coonected yazısının bulunduğu layout



    def update_visual_data(self):
        
        """
Her belli zaman aralığında ekrandaki telemetri verilerini güncellemek için kullanılan fonksyion.
Şu anda her 1 saniyede bir kez çağrılıyor.
        """

        global vehicle


        # BURDA da değişkenklerin değerlerini değiştir ve kontrol et değişken değiştiğinde labeldaki değer de değişir mi diye değişmiyorsa ekstra değişken olayını
        # boşver, label.settext vs de bak
          

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

    def update_variable_data(self):

        data = get_telemetry_data(vehicle)

        if type(data) == str:  # hata olmuşsa

            error_popup("Telemetri Verisi Alınamadı", data)

            return 1

        if vehicle.is_armed:

            self.datas[8] += 1

        self.datas[9] += 1
        
        TAMAMLA

    def update_data(self):

        update_variable_data()

        update_visual_data()


class Map_Layout(QWidget):
    pass
