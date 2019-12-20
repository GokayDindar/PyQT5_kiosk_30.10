'''SCREEN RESOLUTİON IS 1024X600PX'''

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage, QBrush, QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QAction, qApp, \
    QGroupBox, QSpinBox, QComboBox, QDateEdit, QTimeEdit, QLCDNumber, QSlider
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
        self.doorButton = QPushButton("Control")

        self.settingsButton.setCheckable(True)
        self.doorButton.setCheckable(True)

        self.settingsButton.setStyleSheet("background-color:transparent;border: none;color:white;font-size:24px")
        self.settingsButton.setIcon(Icons.settingsIcon1)
        self.settingsButton.setIconSize(QSize(50, 50))

        self.doorButton.setStyleSheet("background-color:transparent;border: none;color:white;font-size:24px")
        self.doorButton.setIcon(Icons.doorIcon)
        self.doorButton.setIconSize(QSize(50, 50))

        self.doorButton.setFixedSize(150, 110)
        self.settingsButton.setFixedSize(150, 110)

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

        grid = QGridLayout()

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

        grid.addWidget(MainWindow.openButton, 0, 0)
        grid.addWidget(MainWindow.closeButton, 0, 1)
        grid.addWidget(MainWindow.stopButton, 0, 2)

        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('Buttons')
        oImage = QImage("../resources/background.png")
        sImage = oImage.scaled(QSize(700, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.stack1.setLayout(grid)

    def stack2UI(self):

        self.labelMin = QLabel()
        self.labelHour = QLabel()

        self.labelMin.setText("57")
        self.labelHour.setText("19")

        self.labelMin.setStyleSheet("color:white;font-size:34px")
        self.labelHour.setStyleSheet("color:white;font-size:34px")

        self.labelMin.setFixedSize(50,50)
        self.labelHour.setFixedSize(50,50)

        labelTag = QLabel("SET HOUR")
        labelTag2 = QLabel(":")
        labelTag2.setStyleSheet("color:white;font-size:34px")
        labelTag2.setFixedSize(50,50)
        labelTag1 = QLabel("SET MINUTE:")

        sliderMin = QSlider(Qt.Horizontal)
        sliderMin.setValue(15)
        sliderMin.setTickInterval(1)
        sliderMin.setMaximum(59)
        sliderMin.setMinimum(00)
        sliderMin.setFixedSize(800, 90)
        sliderMin.valueChanged.connect(self.updateMin)
        sliderMin.setStyleSheet("color:white")

        sliderHour = QSlider(Qt.Horizontal)
        sliderHour.setValue(15)
        sliderHour.setMaximum(23)
        sliderHour.setMinimum(00)
        sliderHour.setFixedSize(800, 90)
        sliderHour.valueChanged.connect(self.updateHour)
        sliderHour.setStyleSheet("color:white")

        labelTag.setStyleSheet("color:white")
        labelTag1.setStyleSheet("color:white")

        layoutH = QHBoxLayout()
        layoutH1 = QHBoxLayout()
        layoutH2 = QHBoxLayout()
        layoutV = QVBoxLayout()

        layoutH2.addWidget(self.labelHour)
        layoutH2.addWidget(labelTag2)
        layoutH2.addWidget(self.labelMin)

        layoutH.addWidget(labelTag)
        layoutH.addWidget(sliderHour)

        layoutH1.addWidget(labelTag1)
        layoutH1.addWidget(sliderMin)

        layoutV.addLayout(layoutH2)
        layoutV.addLayout(layoutH1)
        layoutV.addLayout(layoutH)

        self.stack2.setLayout(layoutV)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        if i == 1:
            self.settingsButton.setIcon(Icons.settingsIcon)
            self.doorButton.setIcon(Icons.doorIcon1)
        else:
            self.settingsButton.setIcon(Icons.settingsIcon1)
            self.doorButton.setIcon(Icons.doorIcon)

    def updateMin(self, min):
        min = str(min)
        min = min.zfill(2)
        self.labelMin.setText(min)

    def updateHour(self, hour):
        print(hour)
        event = str(hour)
        event = event.zfill(2)
        self.labelHour.setText(event)


    @staticmethod
    def numLen(num):
        return len(str(abs(num)))