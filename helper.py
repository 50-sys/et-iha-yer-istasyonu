"""
Hata ayıklama gibi önemli yardımcı fonksiyonları tutan modül.
"""

from datetime import datetime
from PyQt5.QtCore import qErrnoWarning
from PyQt5.QtWidgets import QMessageBox, QWidget
import os, sys


def replace_widget(layout, old_widget : QWidget, new_widget : QWidget):

    
    layout.removeWidget(old_widget)
    layout.addWidget(new_widget, )

def exception_handling():
    pass   

def is_int(string : str):

    """
Verilen stringin sayı olup olmadığını kontrol eden fonksiyon.
    """

    try:
    
        int(string)

        return True

    except:

        return False

@exception_handling
def saveLog(exception : str, folder_name : str = "logs"): ## log nasıl bir şey araştır, ona göre yaz
    
    o_s = sys.platform


    if "linux" in o_s:

        path = os.getcwd() + "/" + folder_name


    elif o_s == "win32":

        path = os.getcwd() + "\\" + folder_name

    else:

        raise Exception("OS not supported!")

    max_log = int(max(filter(lambda a : a[-4 : ] == ".log" and is_int(a[-4 : ]), path.listdir()), key = lambda a : a[: -4])) ## yoldaki maksimum numaralı log dosyasının adı 

    file_name = str(max_log + 1) + ".log"

    path += file_name

    with open(path) as file:

        file.write(exception)



    return path

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
Hata bilgilerinin kaydedildiği dosyanın yolu: 
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


            path = saveLog(error_msg) 

            return error_msg + f"\nLog Dosyası Yolu : {path}"

    return inner
def replace_widget(layout, old_widget : QWidget, new_widget : QWidget):

    
    layout.removeWidget(old_widget)
    layout.addWidget(new_widget, )

def exception_handling():
    pass   

def is_int(string : str):

    """
Verilen stringin sayı olup olmadığını kontrol eden fonksiyon.
    """

    try:
    
        int(string)

        return True

    except:

        return False

@exception_handling
def saveLog(exception : str, folder_name : str = "logs"): ## log nasıl bir şey araştır, ona göre yaz
    
    o_s = sys.platform


    if "linux" in o_s:

        path = os.getcwd() + "/" + folder_name


    elif o_s == "win32":

        path = os.getcwd() + "\\" + folder_name

    else:

        raise Exception("OS not supported!")

    max_log = int(max(filter(lambda a : a[-4 : ] == ".log" and is_int(a[-4 : ]), path.listdir()), key = lambda a : a[: -4])) ## yoldaki maksimum numaralı log dosyasının adı 

    file_name = str(max_log + 1) + ".log"

    path += file_name

    with open(path) as file:

        file.write(exception)



    return path

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
Hata bilgilerinin kaydedildiği dosyanın yolu: 
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


            path = saveLog(error_msg) 

            return error_msg + f"\nLog Dosyası Yolu : {path}"

    return inner

def error_popup(error : str, detailed_description : str = ""):

    popup = QMessageBox()
    popup.setText(error)
    popup.setInformativeText(detailed_description)
    popup.setTitle("HATA")
    popup.setIcon("Warning")

    ret = popup.exec_()

class Limited_List:

    """ 
Eleman sayısı belli bir limiti geçmeyen özel bir liste.

Parametreler:

container : verileri depolayan konteyner
limit : container değişkeninin tutabileceği maksimum eleman sayısı
start_blank : true verilirse containerdeki boş yerler none_item ile doldurulur
none_item : boşlukların doldurulacağı nesne
lean_to_right : true verilirse none_item olmayan değerleri sağa yaslar ve nesne eklemelerinde başa ekler

    """
    
    def __init__(self, limit : int, start_blank : bool, container = list(), none_item = None, lean_to_right = False):
            
        if start_blank:
                
            self.__container = list(container)

        else:
                if lean_to_right:

                    self.__container = [none_item for x in range(limit - len(container))] + list(container)

                else:

                    self.__container = list(container) + [none_item for x in range(limit - len(container))]


        self.__limit = limit
        self.__none_item = none_item
        self.__lean_to_right = lean_to_right

    def __iter__(self):

        self.__current = 0

        return self

    def __len__(self):

        return len(self.__container)

    def __next__(self):

        if self.__current <= len(self):

            raise StopIteration()

        self.__current += 1
        
        

        return self.__container[self.__current - 1]

    
    def __getitem__(self, index : int):
        
        return self.__container[index]

    
    def add(self, item):

        if len(self.__container) == self.__limit:

            if self.__lean_to_right:

    """ 
Eleman sayısı belli bir limiti geçmeyen özel bir liste.

Parametreler:

container : verileri depolayan konteyner
limit : container değişkeninin tutabileceği maksimum eleman sayısı
start_blank : true verilirse containerdeki boş yerler none_item ile doldurulur
none_item : boşlukların doldurulacağı nesne
lean_to_right : true verilirse none_item olmayan değerleri sağa yaslar ve nesne eklemelerinde başa ekler

    """
    
    def __init__(self, limit : int, start_blank : bool, container = list(), none_item = None, lean_to_right = False):
            
        if start_blank:
                
            self.__container = list(container)

        else:
                if lean_to_right:

                    self.__container = [none_item for x in range(limit - len(container))] + list(container)

                else:

                    self.__container = list(container) + [none_item for x in range(limit - len(container))]


        self.__limit = limit
        self.__none_item = none_item
        self.__lean_to_right = lean_to_right

    def __iter__(self):

        self.__current = 0

        return self

    def __len__(self):

        return len(self.__container)

    def __next__(self):

        if self.__current <= len(self):

            raise StopIteration()

        self.__current += 1
        
        

        return self.__container[self.__current - 1]

    
    def __getitem__(self, index : int):
        
        return self.__container[index]

    
    def add(self, item):

        if len(self.__container) == self.__limit:

            if self.__lean_to_right:


                self.__container = [item] + self.__container[: -1]

            else:

                self.__container = self.__container[1 : ] + [item]

        else:

            if self.__lean_to_right:

                self.__container = [item] + self.__container

            else:

                self.__container.append(item)


    def remove(self, item):

        self.__container.remove(item)
        

    def __copy__(self):

        return Limited_List(self.__limit, self.__start_blank, self.__container, self.__none_item, self.__lean_to_right)


