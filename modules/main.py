import threading
import sys
import PyQt5

from windu import MainWindow
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie
from eventCheck import EventCheck
from icons import Icons

if __name__ == '__main__':

    app = QApplication(sys.argv)
    gif = QLabel()
    icons = Icons()
    btnChecker = EventCheck()
    window = MainWindow(btnChecker)
    
    sys.exit(app.exec_())
