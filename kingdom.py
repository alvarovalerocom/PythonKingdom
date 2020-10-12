#game logic
from Hero import Hero
from Healer import Healer
from Weapon import BasicSword, LightStick
basicsword = BasicSword("", 20, 20,5)
lightstick = LightStick("",3,0,100)
print(basicsword.name)
valkiria = Hero("Valkiria", 100, 20, basicsword,"rage")
a = (valkiria.name)
lux = Healer("lux",60,60,lightstick,"heal")

#################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Alv Kingdom'
        self.left = 10
        self.top = 10
        self.width = 1024 
        self.height = 768
        self.initUI()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.black)
        painter.setBrush(QtCore.Qt.white)
        painter.drawLine(1100,600,00,600)

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height) 
        self.label = QLabel(a,self)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#################################################
