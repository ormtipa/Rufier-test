from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def result(self):
        if self.exp.age < 7:
            self.index = 0
            self.text1 = txt_index + str(self.index)
            return(txt_workheart + "there is no data for this age")

        self.index = (4 * (self.exp.test1 + self.exp.test2 + self.exp.test3) - 20)/10
        self.text1 = txt_index + str(self.index)

        if self.exp.age >= 15:
            if self.index >= 15:
                return(txt_workheart + txt_res1)
            elif self.index >= 11:
                return(txt_workheart + txt_res2)
            elif self.index >= 6:
                return(txt_workheart + txt_res3)
            elif self.index >= 0.5:
                return(txt_workheart + txt_res4)
            elif self.index <= 0.4:
                return(txt_workheart + txt_res5)
        
        elif self.exp.age >= 13:
            if self.index >= 16.5:
                return(txt_workheart + txt_res1)
            elif self.index >= 12.5:
                return(txt_workheart + txt_res2)
            elif self.index >= 7.5:
                return(txt_workheart + txt_res3)
            elif self.index >= 2:
                return(txt_workheart + txt_res4)
            elif self.index <= 1.9:
                return(txt_workheart + txt_res5)

        elif self.exp.age >= 11:
            if self.index >= 18:
                return(txt_workheart + txt_res1)
            elif self.index >= 14:
                return(txt_workheart + txt_res2)
            elif self.index >= 9:
                return(txt_workheart + txt_res3)
            elif self.index >= 3.5:
                return(txt_workheart + txt_res4)
            elif self.index <= 3.4:
                return(txt_workheart + txt_res5)

        elif self.exp.age >= 9:
            if self.index >= 19.5:
                return(txt_workheart + txt_res1)
            elif self.index >= 15.5:
                return(txt_workheart + txt_res2)
            elif self.index >= 10.5:
                return(txt_workheart + txt_res3)
            elif self.index >= 5:
                return(txt_workheart + txt_res4)
            elif self.index <= 4.9:
                return(txt_workheart + txt_res5)

        elif self.exp.age >= 7:
            if self.index >= 21:
                return(txt_workheart + txt_res1)
            elif self.index >= 17:
                return(txt_workheart + txt_res2)
            elif self.index >= 12:
                return(txt_workheart + txt_res3)
            elif self.index >= 6.5:
                return(txt_workheart + txt_res4)
            elif self.index <= 6.4:
                return(txt_workheart + txt_res5)
                

    def initUI(self):
        self.v_line = QVBoxLayout()

        self.label2 = QLabel(self.result())
        self.label1 = QLabel(self.text1)

        self.v_line.addWidget(self.label1, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.label2, alignment = Qt.AlignCenter)

        self.setLayout(self.v_line)

