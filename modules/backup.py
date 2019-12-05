import threading
import sys
import time
'''import RPi.GPIO as GPIO
import time
'''


from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel)


flag = False
flag2 = False
# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)

dc = 95 # duty cycle (0-100) for PWM pin


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        global okButton, cancelButton
        global label
        label = QLabel("door is waiting")
        label.setStyleSheet("background-color:blue;font-size:100px;color:white")
        okButton = QPushButton("OPEN")

        cancelButton = QPushButton("CLOSE")
        okButton.setFixedSize(599,500)
        cancelButton.setFixedSize(599,500)

        okButton.setCheckable(False)
        cancelButton.setCheckable(False)


        okButton.setStyleSheet("background-color:green;font-size:100px;color:white")
        cancelButton.setStyleSheet("background-color:green;font-size:100px;color:white")

        okButton.clicked.connect(hast)
        cancelButton.clicked.connect(hust)
        hbox = QHBoxLayout()

        hbox.addWidget(okButton)

        hbox.addStretch(100)
        hbox.addWidget(label)
        hbox.addStretch(100)
        hbox.addWidget(cancelButton)



        self.setLayout(hbox)

        self.setGeometry(1000, 1000, 1900, 900)
        self.setWindowTitle('Buttons')
        self.show()


def hast():
    global flag
    if flag == 0:
        global flag2
        cancelButton.setStyleSheet("background-color:green;font-size:100px;color:white")
        cancelButton.setText("CLOSE")
        flag2 = 0
        print("fuck")
        okButton.setText("STOP")
        okButton.setStyleSheet("background-color:red;font-size:100px;color:white")
        label.setText("door is opening")
        print("hh")
        flag = 1
    else:
        flag = 0
        print("hhhe")
        okButton.setStyleSheet("background-color:green;font-size:100px;color:white")
        label.setText("door is waiting")
        okButton.setText("OPEN")
def hust():
    global flag2
    if flag2 == 0:
        global flag
        flag = 0
        print("fuck")
        okButton.setStyleSheet("background-color:green;font-size:100px;color:white")
        okButton.setText("OPEN")
        cancelButton.setText("STOP")
        cancelButton.setStyleSheet("background-color:red;font-size:100px;color:white")
        print("hh")
        flag2 = 1
        label.setText("door is closing")
    else:
        flag2 = 0
        print("hhhe")
        cancelButton.setStyleSheet("background-color:green;font-size:100px;color:white")
        cancelButton.setText("CLOSE")
        label.setText("door is waiting")


if __name__ == '__main__':

    '''GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
    GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
    pwm = GPIO.PWM(pwmPin, 50)
    '''
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
