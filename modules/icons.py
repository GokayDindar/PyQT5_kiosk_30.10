from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap

class Icons:

    openIcon = QIcon()
    openIcon1 = QIcon()

    closeIcon = QIcon()
    closeIcon1 = QIcon()

    stopIcon = QIcon()
    stopIcon1 = QIcon()

    settingsIcon = QIcon()
    settingsIcon1 = QIcon()

    doorIcon = QIcon()
    doorIcon1 = QIcon()

    def __init__(self):
        self.openIcon.addPixmap(QPixmap('../resources/open.png'), QIcon.Active)
        self.openIcon1.addPixmap(QPixmap('../resources/open1.png'), QIcon.Active)

        self.closeIcon.addPixmap(QPixmap('../resources/close.png'), QIcon.Active)
        self.closeIcon1.addPixmap(QPixmap('../resources/close1.png'), QIcon.Active)

        self.stopIcon.addPixmap(QPixmap('../resources/stop.png'), QIcon.Active)
        self.stopIcon1.addPixmap(QPixmap('../resources/stop1.png'), QIcon.Active)

        self.settingsIcon.addPixmap(QPixmap('../resources/settings.png'), QIcon.Active)
        self.settingsIcon1.addPixmap(QPixmap('../resources/settings1.png'), QIcon.Active)

        self.doorIcon.addPixmap(QPixmap('../resources/door.png'), QIcon.Active)
        self.doorIcon1.addPixmap(QPixmap('../resources/door1.png'), QIcon.Active)


