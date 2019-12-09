'''SCREEN RESOLUTİON IS 1024X600PX'''

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QIcon,  QPalette, QImage, QBrush, QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QToolBar, \
    QToolButton, QAction, qApp
from functools import partial
from modules.icons import Icons


class MainWindow(QWidget):
    openButton = None
    closeButton = None
    stopButton = None

    def __init__(self, btnChecker):
        super().__init__()
        self.initUI(btnChecker)

    def initUI(self, btnChecker):


        label = QLabel("HELLOWORLD")
        grid = QGridLayout()
        grid.setSpacing(5)
        self.setLayout(grid)

        """ ________________________TOOL BAR____________________               """
        toolBar = QToolBar()
        toolButton = QToolButton()
        toolButton.setText("Apple")
        toolButton.setCheckable(False)
        toolButton.setAutoExclusive(True)

        toolBar.setIconSize(QSize(50, 50))
        toolBar.move(0, 0)
        toolBar.addAction(exitAct)

        MainWindow.openButton = QPushButton("")
        MainWindow.closeButton = QPushButton("")
        MainWindow.stopButton = QPushButton("")

        MainWindow.openButton.setFixedSize(150, 150)
        MainWindow.closeButton.setFixedSize(150, 150)
        MainWindow.stopButton.setFixedSize(150, 150)

        MainWindow.openButton.setCheckable(False)
        MainWindow.closeButton.setCheckable(False)
        MainWindow.stopButton.setCheckable(False)

        MainWindow.openButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.openButton.setIcon(Icons.openIcon)
        MainWindow.openButton.setIconSize(QSize(150, 150))

        MainWindow.closeButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.closeButton.setIcon(Icons.closeIcon)
        MainWindow.closeButton.setIconSize(QSize(150, 150))

        MainWindow.stopButton.setStyleSheet("background-color: transparent;border: none;")
        MainWindow.stopButton.setIcon(Icons.stopIcon)
        MainWindow.stopButton.setIconSize(QSize(150, 150))

        grid.addWidget(MainWindow.openButton, 1, 0)
        grid.addWidget(MainWindow.closeButton, 1, 2)
        grid.addWidget(MainWindow.stopButton, 1, 1)

        '''
        hbox = QHBoxLayout()
        hbox.addWidget(openButton)
        hbox.addWidget(closeButton)
        hbox.addWidget(stopButton)
        '''
        MainWindow.openButton.clicked.connect(partial(btnChecker.check, MainWindow.openButton, "openButton"))
        MainWindow.closeButton.clicked.connect(partial(btnChecker.check, MainWindow.closeButton, "closeButton"))
        MainWindow.stopButton.clicked.connect(partial(btnChecker.check, MainWindow.stopButton, "stopButton"))

        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('Buttons')

        oImage = QImage('../resources/background.png')
        sImage = oImage.scaled(QSize(700, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.show()
