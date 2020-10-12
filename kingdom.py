#game logic
from Hero import Hero
from Weapon import BasicSword

valkiria = Hero("Valkiria", 100, 20, "weapon","rage")
print (valkiria)
print (valkiria.weapon, valkiria.getInfo)

basicsword = BasicSword("basic sword", 20, 20)
print(basicsword)
#################################################

#Window
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Alv Kingdom'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#################################################