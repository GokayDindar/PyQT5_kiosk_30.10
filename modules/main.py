import threading
import sys
import PyQt5

from modules.windu import MainWindow
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie
from modules.eventCheck import EventCheck
from modules.icons import Icons

if __name__ == '__main__':

    app = QApplication(sys.argv)
    gif = QLabel()
    icons = Icons()
    btnChecker = EventCheck()
    window = MainWindow(btnChecker)
    
    sys.exit(app.exec_())
