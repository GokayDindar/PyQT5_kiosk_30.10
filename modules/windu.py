'''SCREEN RESOLUTİON IS 1024X600PX'''

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage, QBrush,QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QLabel,QGridLayout
from functools import partial
from icons import Icons

class MainWindow(QWidget):
    openButton = None
    closeButton = None
    stopButton = None

    def __init__(self,btnChecker):
        super().__init__()
        self.initUI(btnChecker)

    def initUI(self,btnChecker):

        label = QLabel("HELLOWORLD")

        MainWindow.openButton = QPushButton("")
        halfOpen = QPushButton("")
        halfClose = QPushButton("")
        MainWindow.closeButton = QPushButton("")
        MainWindow.stopButton = QPushButton("")

        MainWindow.openButton.setFixedSize(300,300)
        halfClose.setFixedSize(300,300)
        halfOpen.setFixedSize(300,300)
        MainWindow.closeButton.setFixedSize(300,300)
        MainWindow.stopButton.setFixedSize(300,300)

        MainWindow.openButton.setCheckable(False)
        MainWindow.closeButton.setCheckable(False)
        MainWindow.stopButton.setCheckable(False)


        MainWindow.openButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.openButton.setIcon(Icons.openIcon)
        MainWindow.openButton.setIconSize(QSize(300, 300))

        halfOpen.setStyleSheet("background-color: transparent;border: none;")
        halfOpen.setIcon(Icons.openIcon)
        halfOpen.setIconSize(QSize(300,300))

        halfClose.setStyleSheet("background-color: transparent;border: none;")
        halfClose.setIcon(Icons.openIcon)
        halfClose.setIconSize(QSize(300,300))

        MainWindow.closeButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.closeButton.setIcon(Icons.closeIcon)
        MainWindow.closeButton.setIconSize(QSize (300, 300))

        MainWindow.stopButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.stopButton.setIcon(Icons.stopIcon)
        MainWindow.stopButton.setIconSize(QSize (300, 300))


        MainWindow.openButton.move(12,50)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(MainWindow.openButton, 1, 0)
        grid.addWidget(MainWindow.closeButton, 1, 2)
        grid.addWidget(MainWindow.stopButton, 1, 1)
        self.setLayout(grid)
   
        '''
        hbox = QHBoxLayout()
        hbox.addWidget(openButton)
        hbox.addWidget(closeButton)
        hbox.addWidget(stopButton)
        '''
        MainWindow.openButton.clicked.connect(partial(btnChecker.check,MainWindow.openButton,"openButton"))
        MainWindow.closeButton.clicked.connect(partial(btnChecker.check,MainWindow.closeButton,"closeButton"))
        MainWindow.stopButton.clicked.connect(partial(btnChecker.check,MainWindow.stopButton,"stopButton"))


        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('Buttons')
        oImage = QImage("/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/background.png")
        sImage = oImage.scaled(QSize(700,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)


        self.show()
