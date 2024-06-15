from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.test1 = int(test1)
        self.test2 = int(test2)
        self.test3 = int(test3)


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.label1 = QLabel(txt_name)
        self.label2 = QLabel(txt_age)
        self.label3 = QLabel(txt_test1)
        self.label4 = QLabel(txt_test2)
        self.label5 = QLabel(txt_test3)
        self.label6 = QLabel(txt_timer)

        self.edit1 = QLineEdit(txt_hintname)
        self.edit2 = QLineEdit(txt_hintage)
        self.edit3 = QLineEdit(txt_hinttest1)
        self.edit4 = QLineEdit(txt_hinttest2)
        self.edit5 = QLineEdit(txt_hinttest2)

        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button_next = QPushButton(txt_sendresults)

        self.r_line.addWidget(self.label1)
        self.r_line.addWidget(self.edit1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.label2)
        self.r_line.addWidget(self.edit2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.label3)
        self.r_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.edit3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.label4)
        self.r_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.label5)
        self.r_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.edit4, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.edit5, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.button_next, alignment = Qt.AlignCenter)

        self.l_line.addWidget(self.label6)

        self.h_line.addLayout(self.r_line)
        self.h_line.addLayout(self.l_line)
        self.setLayout(self.h_line)

    def timer1_test(self):
        global time 
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer1Event)
        

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.label6.setText(time.toString("hh:mm:ss"))
        self.label6.setFont(QFont("Times", 36, QFont.Bold))
        self.label6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2_test(self):
        global time 
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.label6.setText(time.toString("hh:mm:ss")[6:8])
        self.label6.setFont(QFont("Times", 36, QFont.Bold))
        self.label6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3_test(self):
        global time 
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.label6.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss"[-2:])) >= 45 or int(time.toString("hh:mm:ss"[-2:])) <= 15:
            self.label6.setFont(QFont("Times", 36, QFont.Bold))
            self.label6.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.label6.setFont(QFont("Times", 36, QFont.Bold))
            self.label6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.button_next.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer1_test)
        self.button2.clicked.connect(self.timer2_test)
        self.button3.clicked.connect(self.timer3_test)

    def next_click(self):
        self.hide()
        self.exp = Experiment(self.edit2.text(), self.edit3.text(), self.edit4.text(), self.edit5.text())
        self.fw = FinalWin(self.exp)