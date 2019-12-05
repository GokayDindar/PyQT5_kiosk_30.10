from PyQt5.QtCore import QThread
from multiprocessing import *
from PyQt5.QtCore import QThread
class Driver_thread(QThread):

    def __init__(self):
        pass

    def open(self):
        print ("opening")

