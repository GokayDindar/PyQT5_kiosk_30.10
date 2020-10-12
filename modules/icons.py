from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap

class Icons:

    openIcon = QIcon()
    openIcon1 = QIcon()

    closeIcon = QIcon()
    closeIcon1 = QIcon()

    stopIcon = QIcon()
    stopIcon1 = QIcon()


    halfOpenIcon = QIcon()
    halfOpenIcon1 = QIcon()

    halfCloseIcon = QIcon()
    halfCloseIcon1 = QIcon()

    settingsIcon = QIcon()
    settingsIcon1 = QIcon()

    doorIcon = QIcon()
    doorIcon1 = QIcon()

    lockIcon = QIcon()
    lockIcon1 = QIcon()

    def __init__(self):
        self.openIcon.addPixmap(QPixmap('../resources/open.png'), QIcon.Active)
        self.openIcon1.addPixmap(QPixmap('../resources/open1.png'), QIcon.Active)

        self.closeIcon.addPixmap(QPixmap('../resources/close.png'), QIcon.Active)
        self.closeIcon1.addPixmap(QPixmap('../resources/close1.png'), QIcon.Active)

        self.stopIcon.addPixmap(QPixmap('../resources/stop.png'), QIcon.Active)
        self.stopIcon1.addPixmap(QPixmap('../resources/stop1.png'), QIcon.Active)

        self.halfCloseIcon.addPixmap(QPixmap('../resources/half-close.png'), QIcon.Active)
        self.halfCloseIcon1.addPixmap(QPixmap('../resources/half-close1.png'), QIcon.Active)

        self.halfOpenIcon.addPixmap(QPixmap('../resources/half-open.png'), QIcon.Active)
        self.halfOpenIcon1.addPixmap(QPixmap('../resources/half-open1.png'), QIcon.Active)

        self.settingsIcon.addPixmap(QPixmap('../resources/settings.png'), QIcon.Active)
        self.settingsIcon1.addPixmap(QPixmap('../resources/settings1.png'), QIcon.Active)

        self.doorIcon.addPixmap(QPixmap('../resources/door.png'), QIcon.Active)
        self.doorIcon1.addPixmap(QPixmap('../resources/door1.png'), QIcon.Active)

        self.lockIcon.addPixmap(QPixmap('../resources/user-unlocked.png'), QIcon.Active)
        self.lockIcon1.addPixmap(QPixmap('../resources/user-locked.png'), QIcon.Active)


