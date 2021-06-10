"""
Hata ayıklama gibi önemli yardımcı fonksiyonları tutan modül.
"""

from datetime import datetime
import os, sys

def saveLog(exception_name : str, folder_name : str = "logs"): ## log nasıl bir şey araştır, ona göre yaz
    pass

def exception_handling(func):
    
    """
Decorator olarak kullanıldığı fonksiyonlarda bir hata oluşması durumunda log dosyasını logs klasörüne kaydedip hatayı f formatında döndüren fonksiyon.

f formatı:

'''
Hatanın olduğu dosya: 
Hatanın olduğu fonksiyon: 
Hata türü: 
Hata metni: 
Hatalı satır:
Hatanın zamanı:   
'''
    """

    def inner(*args, **kwargs):

        try:
            func(*args, **kwargs)

        except Exception as e:
            
            
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            time = datetime.ctime(datetime.now())

            error_msg = f"""
Hatanın olduğu dosya     : {file_name}
Hatanın olduğu fonksiyon : {func.__name__} 
Hata türü                : {str(exc_type)[8 : -2]}
Hata metni               : {e}
Hatanın olduğu satır     : {exc_tb.tb_lineno}
Hatanın zamanı           : {time} \n\n
            """


            saveLog() ## netten log dosyası örneklerine bak

            return error_msg 

    return inner

