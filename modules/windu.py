'''SCREEN RESOLUTİON IS 1024X600PX'''

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage, QBrush, QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QAction, qApp, \
    QGroupBox, QSpinBox, QComboBox, QDateEdit, QTimeEdit, QLCDNumber, QSlider, QTabWidget
from functools import partial
from modules.icons import Icons
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QCheckBox, QApplication, QListWidget, QWidget, QRadioButton, QLineEdit, \
    QFormLayout, QStackedWidget
from PyQt5.QtWidgets import QMessageBox
import modules.buttonizer


class MainWindow(QWidget):
    toLock = 0

    def __init__(self, btnChecker):
        super().__init__()


        self.setWindowTitle('Modedoor Kiosk 30.10')

        self.showFullScreen()

        self.isLocked = 0;

        label = QLabel()
        labelPixmap = QPixmap('../resources/SAFEBANNER.png')
        label.setPixmap(labelPixmap)
        label.setAlignment(Qt.AlignCenter)

        # Optional, resize window to image size
        self.resize(labelPixmap.width(), labelPixmap.height())

        self.settingsButton = modules.buttonizer.Buttonizer("Settings", 150, 110, True, Icons.settingsIcon, 50, 50)
        self.doorButton = modules.buttonizer.Buttonizer("Control", 150, 110, True, Icons.doorIcon, 50, 50)
        self.lockButton = modules.buttonizer.Buttonizer("UnLocked", 170, 110, True, Icons.lockIcon, 100, 50)

        self.controlStack = QWidget()
        self.settingStack = QWidget()
        self.lockStack = QWidget()

        self.settingStackUI()
        self.controlStackUI(btnChecker)
        self.lockStackUI()

        self.Stack = QStackedWidget(self)

        self.Stack.addWidget(self.controlStack)
        self.Stack.addWidget(self.settingStack)
        self.Stack.addWidget(self.lockStack)

        hbox = QHBoxLayout()
        hbox.setSpacing(0.5)
        hbox.addWidget(self.doorButton)
        hbox.addWidget(self.lockButton)
        hbox.addWidget(self.settingsButton)

        vbox = QVBoxLayout()
        vbox.addSpacing(2)
        vbox.addLayout(hbox)
        vbox.addWidget(self.Stack)

        vbox.addWidget(label)

        self.settingsButton.clicked.connect(partial(self.display, 1))
        self.doorButton.clicked.connect(partial(self.display, 0))
        self.lockButton.clicked.connect(partial(self.display, 2))

        self.setLayout(vbox)
        self.setGeometry(0, 0, 1024, 600)
        self.show()

    def controlStackUI(self, btnChecker):

        grid = QGridLayout()

        MainWindow.openButton = modules.buttonizer.Buttonizer("", 140, 140, False, Icons.openIcon, 140, 140)
        MainWindow.halfOpen = modules.buttonizer.Buttonizer("", 140, 140, False, Icons.halfOpenIcon, 140, 140)
        MainWindow.halfClose = modules.buttonizer.Buttonizer("", 140, 140, False, Icons.halfCloseIcon, 140, 140)
        MainWindow.closeButton = modules.buttonizer.Buttonizer("", 140, 140, False, Icons.closeIcon, 140, 140)
        MainWindow.stopButton = modules.buttonizer.Buttonizer("", 140, 140, False, Icons.stopIcon, 140, 140)

        MainWindow.openButton.clicked.connect(partial(btnChecker.check, MainWindow.openButton, "openButton"))
        MainWindow.closeButton.clicked.connect(partial(btnChecker.check, MainWindow.closeButton, "closeButton"))
        MainWindow.stopButton.clicked.connect(partial(btnChecker.check, MainWindow.stopButton, "stopButton"))

        grid.addWidget(MainWindow.openButton, 1, 0)
        grid.addWidget(MainWindow.closeButton, 1, 1)
        grid.addWidget(MainWindow.stopButton, 1, 2)
        grid.addWidget(MainWindow.halfOpen, 1, 3)
        grid.addWidget(MainWindow.halfClose, 1, 4)

        oImage = QImage("../resources/background.png")
        sImage = oImage.scaled(QSize(700, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.controlStack.setLayout(grid)

    def settingStackUI(self):

        layout = QVBoxLayout(self)

        topVlayout = QVBoxLayout()
        topVlayout.setSpacing(0)

        self.labelMin = QLabel()
        self.labelHour = QLabel()

        self.labelMin.setText("57")
        self.labelHour.setText("19")

        self.labelMin.setStyleSheet("color:black;font-size:34px")
        self.labelHour.setStyleSheet("color:black;font-size:34px")

        self.labelMin.setFixedSize(100, 100)
        self.labelHour.setFixedSize(100, 100)

        labelTag = QLabel("SET HOUR")
        labelTag.setStyleSheet("color:black;font-size:34px")

        labelTag2 = QLabel(":")
        labelTag2.setStyleSheet("color:black;font-size:34px")
        labelTag2.setFixedSize(100, 100)
        labelTag1 = QLabel("SET MINUTE:")
        labelTag1.setStyleSheet("color:black;font-size:34px")

        sliderMin = QSlider(Qt.Horizontal)
        sliderMin.setValue(15)
        sliderMin.setTickInterval(1)
        sliderMin.setMaximum(59)
        sliderMin.setMinimum(00)
        sliderMin.setFixedSize(500, 90)
        sliderMin.valueChanged.connect(self.updateMin)
        sliderMin.setStyleSheet("color:white")

        sliderHour = QSlider(Qt.Horizontal)
        sliderHour.setValue(15)
        sliderHour.setMaximum(23)
        sliderHour.setMinimum(00)
        sliderHour.setFixedSize(500, 90)
        sliderHour.valueChanged.connect(self.updateHour)
        sliderHour.setStyleSheet("color:white")


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

        numpad = QGridLayout()
        save = QPushButton("Save")
        numpad_layout = QVBoxLayout()

        numpad.setSpacing(5)
        numpad.setAlignment(Qt.AlignLeft)
        number1 = QPushButton('1')
        number2 = QPushButton('2')
        number3 = QPushButton('3')
        number4 = QPushButton('4')
        number5 = QPushButton('5')
        number6 = QPushButton('6')
        number7 = QPushButton('7')
        number8 = QPushButton('8')
        number9 = QPushButton('9')

        number1.setFixedSize(100,100)
        number2.setFixedSize(100,100)
        number3.setFixedSize(100,100)
        number4.setFixedSize(100,100)
        number5.setFixedSize(100,100)
        number6.setFixedSize(100,100)
        number7.setFixedSize(100,100)
        number8.setFixedSize(100,100)
        number9.setFixedSize(100,100)

        numpad.addWidget(number1,0,0)
        numpad.addWidget(number2,0,1)
        numpad.addWidget(number3,0,2)
        numpad.addWidget(number4,1,0)
        numpad.addWidget(number5,1,1)
        numpad.addWidget(number6,1,2)
        numpad.addWidget(number7,2,0)
        numpad.addWidget(number8,2,1)
        numpad.addWidget(number9,2,2)

        numpad_layout.addLayout(numpad)
        numpad_layout.addWidget(save)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()


        # Add tabs
        self.tabs.addTab(self.tab1,"Time")
        self.tabs.addTab(self.tab2,"Password")

        # Create first tab

        self.tab1.setLayout(layoutV)
        self.tab2.setLayout(numpad_layout)


        # Add tabs to widget
        layout.addWidget(self.tabs)
        self.settingStack.setLayout(layout)


    def lockStackUI(self):
        pass

    def lockUnlock(self, toLock):

        try:
            f = open('password.txt', 'r')
        except:
            lay = QHBoxLayout()
            lay.setAlignment(Qt.AlignCenter)
            warn = QLabel("YOU HAVE TO SPECIFY PASSWORD TO LOCK!.\n \t      GO TO SETTINGS")
            warn.setStyleSheet("color:red;font-size:30px")
            lay.addWidget(warn)
            self.lockStack.setLayout(lay)
        else:
            if toLock == 0:
                self.settingsButton.setHidden(True)
                self.doorButton.setHidden(True)
                MainWindow.toLock = 1
                self.lockButton.setIcon(Icons.lockIcon1)
            else:
                self.settingsButton.setHidden(False)
                self.doorButton.setHidden(False)
                self.Stack.setCurrentIndex(0)
                self.lockButton.setText("Unlocked")
                self.lockButton.setIcon(Icons.lockIcon)
                MainWindow.toLock = 0

    def display(self, i):

        self.Stack.setCurrentIndex(i)
        if i == 1:
            self.settingsButton.setIcon(Icons.settingsIcon1)
            self.doorButton.setIcon(Icons.doorIcon)
            self.lockButton.setIcon(Icons.lockIcon)

        elif i == 0:
            self.settingsButton.setIcon(Icons.settingsIcon)
            self.doorButton.setIcon(Icons.doorIcon1)
            self.lockButton.setIcon(Icons.lockIcon)
        elif i == 2:
            self.settingsButton.setIcon(Icons.settingsIcon)
            self.doorButton.setIcon(Icons.doorIcon)
            self.lockUnlock(MainWindow.toLock)

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
