"""
Ana modül.
"""
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

import sys
from PyQt5 import QtWidgets
from gui import * 



def main():

    app = QtWidgets.QApplication(sys.argv)
    t_window = Window()
    t_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    