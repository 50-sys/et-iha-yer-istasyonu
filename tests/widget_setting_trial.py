from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QPushButton, QWidget
from PyQt5 import QtWidgets
import sys

"""
Test edilenler:


widget değiştirme mevzusu

layoutdaki widgetin başka layoutla değişmesi

o anki layoutun x olmaması durumunda bile x in timer inin çalışıp verileri güncellemesi
"""



class app():

    def __init__(self):


        
        layout = QGridLayout()

        c = QLabel("dskfd")

        layout.addWidget(c, 0, 1)

        layout1 = QGridLayout()
        
        b = QLabel("kfdgkng")
        layout.addWidget(b, 0, 2)

        o = QLabel("lkfdlkfsdfd")
        o.setFont(QFont("Arial", 100))
        layout.addWidget(o, 1, 0)

        button = QPushButton("dfjn")

        button.clicked.connect(lambda  : self.d(layout1))
        
        layout.addWidget(button, 0, 3)
        
        
        self.layout = layout

        
        print(self.layout.itemAt(1).widget())

        print(o, b, c, button, button)

    def d(self, layout):
        self.layout = layout

class ap(QWidget):

   def __init__(self):

       super(ap, self).__init__()
       self.setWindowTitle("jd")
       print(help(self.setGeometry))

       layout = app().layout
       self.setLayout(layout)
       self.resize(1000, 1000)

        
class a(QWidget):

    def __init__(self):

        super(a, self).__init__()

        self.setWindowTitle("skjdnj")

        label = QLabel("jksdvkl")

        layout = QGridLayout()
        
        layout.addWidget(label, 0, 10)
        self.setLayout(layout)

ab = QApplication(sys.argv)
w = ap()
w.show()
sys.exit(ab.exec_())