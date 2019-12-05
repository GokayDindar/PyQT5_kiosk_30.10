from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap

class Icons:

    openIcon = QIcon()
    openIcon1 = QIcon()

    closeIcon = QIcon()
    closeIcon1 = QIcon()

    stopIcon = QIcon()
    stopIcon1 = QIcon()

    def __init__(self):
        self.openIcon.addPixmap(QPixmap('/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/open.png'), QIcon.Active)
        self.openIcon1.addPixmap(QPixmap('/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/open1.png'), QIcon.Active)

        self.closeIcon.addPixmap(QPixmap('/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/close.png'), QIcon.Active)
        self.closeIcon1.addPixmap(QPixmap('/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/close1.png'), QIcon.Active)

        self.stopIcon.addPixmap(QPixmap('/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/stop.png'), QIcon.Active)
        self.stopIcon1.addPixmap(QPixmap('/Users/gokay/Desktop/kiosk/Modedoor_last_stable_kiosk---2019-12-4_WİTH_GPİO_DİSABLED/resources/stop1.png'), QIcon.Active)

