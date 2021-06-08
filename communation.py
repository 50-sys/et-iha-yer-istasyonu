"""
İHA ile iletişimi sağlayan araçları barındıran modül.
"""

from helper import exception_handling
import os  
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink import mavutil

@exception_handling
def connect_to_drone(connection_string : str): ## burda objeyi return et 
    ## linux ve windowsa göre ayrım yap
    drone = mavutil.mavlink_connection(connection_string)
    
    return drone

def disconnect_from_veichle():
    pass    


@exception_handling
def get_telemetry_data(veichle, *args):

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
7 : PUSULAYLA ALAKALI BİR ŞEYLER


Parametreler:

veichle : Telemetri verisi alınacak araç. 
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
        6 : boylamınkodu,
        7 : pusulaylaalakalıbirşeylerinkodu
    }

    results = []

    for i in args:

        data = veichle.messages[codes[i]].alt

        if not data:
            
            raise Exception("Veri alınamadı veya yanlış.")
    
        results.append(data)
        

    return tuple(results)

https://www.ardusub.com/developers/pymavlink.html 
https://www.researchgate.net/publication/323683430_Communicating_with_Raspberry_Pi_via_MAVLink
https://docs.px4.io/master/en/companion_computer/pixhawk_companion.html
https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html




@exception_handling
def switchFailSafe(): ## global drone belirt 
    pass

@exception_handling
def changeFlightMode(): ## global drone belirt 
    pass

@exception_handling
def arm_disarm(): ## global drone belirt 
    pass