from PyQt5.QtCore import Qt,QTimer,QTime,QLocale
from PyQt5.QtGui import QDoubleValidator,QIntValidator,QFont
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QListWidget,QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    #tambah
    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

#tambahkan
def results(self):
    if self.exp.age<7:
        self.index=0
        return "there is no data for this age"
    self.index = (4*(int(self.exp.t1) + int(self.exp.t2
