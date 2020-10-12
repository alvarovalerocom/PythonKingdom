#game logic
from Hero import Hero
from Healer import Healer
from Weapon import BasicSword, LightStick
basicsword = BasicSword("", 20, 20,5)
lightstick = LightStick("",3,0,100)
print(basicsword.name)
valkiria = Hero("Valkiria", 100, 20, basicsword,"rage")
print(valkiria.getInfo())
lux = Healer("lux",60,60,lightstick,"heal")

#################################################

#Window
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel 
from PyQt5 import QtGui 
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Alv Kingdom'
        self.left = 10
        self.top = 10
        self.width = 1024 
        self.height = 768
        self.initUI()
        self.label = QLabel('This is label', self)
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#################################################
