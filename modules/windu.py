'''SCREEN RESOLUTİON IS 1024X600PX'''

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage, QBrush, QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QAction, qApp
from functools import partial
from modules.icons import Icons
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QCheckBox, QApplication, QListWidget, QWidget, QRadioButton, QLineEdit, \
    QFormLayout, QStackedWidget


class MainWindow(QWidget):

    def __init__(self, btnChecker):
        super().__init__()

        self.settingsButton = QPushButton("Settings")
        self.doorButton = QPushButton("door")

        self.settingsButton.setCheckable(True)
        self.doorButton.setCheckable(True)

        self.settingsButton.setStyleSheet("background-color:transparent;border: none;color:white;font-size:24px")
        self.settingsButton.setIcon(Icons.settingsIcon1)
        self.settingsButton.setIconSize(QSize(50, 50))

        self.doorButton.setStyleSheet("background-color:transparent;border: none;color:white;font-size:24px")
        self.doorButton.setIcon(Icons.doorIcon)
        self.doorButton.setIconSize(QSize(50, 50))



        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack1UI(btnChecker)
        self.stack2UI()

        self.Stack = QStackedWidget(self)

        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)

        hbox = QHBoxLayout()
        hbox.addWidget(self.doorButton)
        hbox.addWidget(self.settingsButton)


        vbox = QVBoxLayout()
        vbox.addSpacing(30)
        vbox.addLayout(hbox)
        vbox.addWidget(self.Stack)

        self.settingsButton.clicked.connect(partial(self.display, 1))
        self.doorButton.clicked.connect(partial(self.display, 0))

        self.setLayout(vbox)
        self.setWindowTitle('Modedoor Kiosk 30.10')
        self.show()

    def stack1UI(self, btnChecker):
        openButton = None
        closeButton = None
        stopButton = None
        label = QLabel("HELLOWORLD")

        self.grid = QGridLayout()

        MainWindow.openButton = QPushButton("")
        halfOpen = QPushButton("")
        halfClose = QPushButton("")
        MainWindow.closeButton = QPushButton("")
        MainWindow.stopButton = QPushButton("")

        MainWindow.openButton.setFixedSize(100, 100)
        halfClose.setFixedSize(100, 100)
        halfOpen.setFixedSize(100, 100)
        MainWindow.closeButton.setFixedSize(100, 100)
        MainWindow.stopButton.setFixedSize(100, 100)

        MainWindow.openButton.setCheckable(False)
        MainWindow.closeButton.setCheckable(False)
        MainWindow.stopButton.setCheckable(False)

        MainWindow.openButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.openButton.setIcon(Icons.openIcon)
        MainWindow.openButton.setIconSize(QSize(100, 100))

        halfOpen.setStyleSheet("background-color: transparent;border: none;")
        halfOpen.setIcon(Icons.openIcon)
        halfOpen.setIconSize(QSize(100, 100))

        halfClose.setStyleSheet("background-color: transparent;border: none;")
        halfClose.setIcon(Icons.openIcon)
        halfClose.setIconSize(QSize(100, 100))

        MainWindow.closeButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.closeButton.setIcon(Icons.closeIcon)
        MainWindow.closeButton.setIconSize(QSize(100, 100))

        MainWindow.stopButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.stopButton.setIcon(Icons.stopIcon)
        MainWindow.stopButton.setIconSize(QSize(100, 100))

        MainWindow.openButton.clicked.connect(partial(btnChecker.check, MainWindow.openButton, "openButton"))
        MainWindow.closeButton.clicked.connect(partial(btnChecker.check, MainWindow.closeButton, "closeButton"))
        MainWindow.stopButton.clicked.connect(partial(btnChecker.check, MainWindow.stopButton, "stopButton"))

        self.grid.addWidget(MainWindow.openButton, 0, 0)
        self.grid.addWidget(MainWindow.closeButton, 0, 1)
        self.grid.addWidget(MainWindow.stopButton, 0, 2)

        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('Buttons')
        oImage = QImage("../resources/background.png")
        sImage = oImage.scaled(QSize(700, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.stack1.setLayout(self.grid)

    def stack2UI(self):
        pass

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        if i == 1:
            self.settingsButton.setIcon(Icons.settingsIcon)
            self.doorButton.setIcon(Icons.doorIcon1)
        else:
            self.settingsButton.setIcon(Icons.settingsIcon1)
            self.doorButton.setIcon(Icons.doorIcon)