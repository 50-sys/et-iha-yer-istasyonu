"""
İHA ile iletişimi sağlayan araçları barındıran modül.
"""

from helper import exception_handling
import os  
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink import mavutil

class Vehicle:

    def __init__(self, vehicle, fligt_mode : str, is_armed : bool):

        self.vehicle = vehicle   
        self.fligt_mode = fligt_mode
        self.is_armed = is_armed

@exception_handling
def connect_to_vehicle(connection_string : str):

    vehicle = mavutil.mavlink_connection(connection_string)
    
    vehicle.wait_heartbeat()
    
    return Vehicle(vehicle, "", 0)

def disconnect_from_vehicle():

    return None


@exception_handling
def get_telemetry_data(vehicle, *args):

    global drone 

    """
    getTelemetryData(*args)

Sırasıyla args parametresinde belirtilen telemetri verilerini bir demet olarak döndüren fonksiyon.


Telemetri Verilerinin Kodları:

0 : BASINÇ
1 : PİL GERİLİMİ
2 : SICAKLIK
3 : YÜKSEKLİK
4 : YÜKSEKLİK (GPS)
5 : ENLEM
6 : BOYLAM


Parametreler:

vehicle : Telemetri verisi alınacak araç. 
args : Döndürülmesi talep edilen telemetri verilerin sırasıyla kodlarını tutan ve tüm elemanları integer veri tipinden olan bir demet.


Döndürür: Args parametresinde sırasına göre kodları verilmiş telemetri verilerini tutan bir demet.
    """

    args = args or tuple(range(8)) ## Eğer argüman girilmemişse tüm değerleri sırasıyla döndürecek şekilde demet atıyoruz.
    
    if len(set(args).intersection(set(range(8)))) != len(args):
        raise Exception("Geçersiz veri girişi.")


    codes = {
        0 : basıncınkodu,
        1 : pilgerilimininkodu,
        2 : sıcaklığınkodu,
        3 : yüksekliğinkodu,
        4 : gpsyüksekliğininkodu,
        5 : enleminkodu,
        6 : boylamınkodu
    }

    results = []

    for i in args:

        data = vehicle.messages[codes[i]].alt

        if not data:
            
            raise Exception("Veri alınamadı veya yanlış.")
    
        results.append(data)
        

    return tuple(results)

"""
https://www.ardusub.com/developers/pymavlink.html 
https://www.researchgate.net/publication/323683430_Communicating_with_Raspberry_Pi_via_MAVLink
https://docs.px4.io/master/en/companion_computer/pixhawk_companion.html
https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html
"""



@exception_handling
def switch_fail_safe(vehicle): ## global drone belirt 
    pass

@exception_handling
def change_flight_mode(vehicle, mode : str): ## global drone belirt 
    pass

@exception_handling
def arm_disarm(vehicle): ## global drone belirt 
    pass

