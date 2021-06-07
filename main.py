"""
Ana modül.
"""

import sys
from PyQt5 import QtWidgets
from gui import * 



def main():

    app = QtWidgets.QApplication(sys.argv)
    t_window = Telemetry_Window()
    app.exec_()



if __name__ == '__main__':
    main()