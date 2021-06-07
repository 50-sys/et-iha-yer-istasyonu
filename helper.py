from datetime import datetime


def saveLog(exception_name : str, folder_name : str = "logs"): ## log nasıl bir şey araştır, ona göre yaz
    pass

def exception_handling(func):
    
    """
Decorator olarak kullanıldığı fonksiyonlarda bir hata oluşması durumunda log dosyasını project/logs yoluna kaydedip hatayı döndüren fonksiyon.
    """

    def inner(*args, **kwargs):

        try:
            func(*args, **kwargs)

        except Exception as e:
            saveLog() ##netten log dosyası örneklerine bak
            
            return f"{func.__name__} Fonksiyonunda HATA : {e}"

    return inner

