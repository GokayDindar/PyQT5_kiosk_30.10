from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton

class Buttonizer(QPushButton):

    def __init__(self, name, widht, height, checkablity, icon, icon_size1, icon_size2):
        super().__init__()

        self.setCheckable(checkablity)
        self.setText(name)
        self.setFixedSize(widht, height)
        self.setIcon(icon)
        self.setIconSize(QSize(icon_size1, icon_size2))

        self.setStyleSheet("background-color:transparent;border: none;color:white;font-size:24px")
