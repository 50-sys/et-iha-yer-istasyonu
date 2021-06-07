"""
Ana modül.
"""

import sys
from PyQt5 import QtWidgets
from gui import Telemetry_Window

app = QtWidgets.QApplication(sys.argv)
t_window = Telemetry_Window()
app.exec_()
