# it works for which button is in the action and interrupts the last action
from PyQt5.QtCore import QSize, QThread, pyqtSignal
from icons import Icons
from windu import MainWindow
"""
import RPi.GPIO as GPIO
"""
import time
from datetime import datetime
import logging
from Qthreads import drive_thread


class WorkerThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    flag = 0

    def __init__(self, name,GPIO):
        super(WorkerThread, self).__init__()
        self.name = name
        self.GPIO = GPIO

    def run(self):
        print (self.flag)
        while 1:
            if self.name == "stoper":
                
                """
                GPIO.output(26, GPIO.HIGH)
                GPIO.output(25, GPIO.HIGH)
                GPIO.output(24, GPIO.LOW)
                break
                """
                pass
            if self.name == "opener":
                
                """
                GPIO.output(26, GPIO.HIGH)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                break
                """
                pass
            if self.name == "closer":
                
                """
                GPIO.output(26, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                GPIO.output(24, GPIO.HIGH)
                break
                """
                pass
            else:
                break


class EventCheck:

    def __init__(self):
        
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        self.worker = WorkerThread("stay", GPIO)
        """
        pass

    def check(self, button, name):

        if name == "stopButton":
            MainWindow.openButton.setIcon(Icons.openIcon)
            MainWindow.closeButton.setIcon(Icons.closeIcon)
            
            button.setIcon(Icons.stopIcon1)
            button.setIconSize(QSize(300, 300))
            
            """
            
            if self.worker.isRunning():
                self.worker.terminate()

            self.worker = WorkerThread("stoper",GPIO)
            self.worker.start()
            """

        elif name == "openButton":
            
            MainWindow.closeButton.setIcon(Icons.closeIcon)
            MainWindow.stopButton.setIcon(Icons.stopIcon)
            
            button.setIcon(Icons.openIcon1)
            button.setIconSize(QSize(300, 300))
            
            """ 
            if self.worker.isRunning():
                self.worker.terminate()

            self.worker = WorkerThread("opener",GPIO)
            self.worker.start()
            """

        elif name == "closeButton":
            MainWindow.openButton.setIcon(Icons.openIcon)
            MainWindow.stopButton.setIcon(Icons.stopIcon)

            button.setIcon(Icons.closeIcon1)
            button.setIconSize(QSize(300, 300))
            
            """
            if self.worker.isRunning():
                self.worker.terminate()

            self.worker = WorkerThread("closer",GPIO)
            self.worker.start()
            """

            
