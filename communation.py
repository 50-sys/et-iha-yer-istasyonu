"""
İHA ile iletişimi sağlayan araçları barındıran modül.
"""

from helper import exception_handling


@exception_handling
def getTelemetryData(*args):
    
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

args : Döndürülmesi talep edilen telemetri verilerin sırasıyla kodlarını tutan ve tüm elemanları integer veri tipinden olan bir demet.


Döndürür: Args parametresinde sırasına göre kodları verilmiş telemetri verilerini tutan bir demet.
    """

    args = args or tuple(range(8)) ## Eğer argüman girilmemişse tüm değerleri sırasıyla döndürecek şekilde demet atıyoruz.
    
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


https://www.ardusub.com/developers/pymavlink.html 


def switchFailSafe():
    pass

def changeFlightMode():
    pass

def arm_disarm():
    pass