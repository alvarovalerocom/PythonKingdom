#game logic
from Pet import Pet
from Hero import Hero
from Healer import Healer
from Weapon import BasicSword, LightStick
from Map import Map
from Cave import Cave
basicsword = BasicSword("", 20, 20,5)
lightstick = LightStick("",3,0,100)
print(basicsword.name)
valkiria = Hero("Valkiria", 100, 20, basicsword,"rage")

lux = Healer("Lux",60,60,lightstick,"heal")

pomm = Pet("Pomm", 30,0,"Bag")


map = Cave("Cave",1,1,10,"first")
map.getCurrentLevelInfo()


#currentMapLevel = 0
#maximumMapLevel = 10
#################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen 
from PyQt5.QtGui import QIcon , QFont
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui 
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
        painter.drawLine(1100,400,00,400)

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height) 

        #Hero labels
        self.heroNameLabel = QLabel(valkiria.name,self)
        self.heroNameLabel.setFont(QtGui.QFont("Times",14,QtGui.QFont.Bold))
        self.heroNameLabel.setGeometry(100,500,500,500)
        
        self.heroHealthLabel= QLabel("HP: "+ str(valkiria.hp),self)
        self.heroHealthLabel.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        self.heroHealthLabel.setStyleSheet("color: green")
        self.heroHealthLabel.setGeometry(100,480,500,500)
  
        self.heroManaLabel = QLabel("MP: "+str(valkiria.mp),self)
        self.heroManaLabel.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        self.heroManaLabel.setStyleSheet("color: blue")
        self.heroManaLabel.setGeometry(100,460,500,500)


        
        #Healer labels
        self.healerNameLabel = QLabel(lux.name,self)
        self.healerNameLabel.setFont(QtGui.QFont("Times",14,QtGui.QFont.Bold))
        self.healerNameLabel.setGeometry(300,500,500,500)

        self.healerHealthLabel= QLabel("HP: "+ str(lux.hp),self)
        self.healerHealthLabel.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        self.healerHealthLabel.setStyleSheet("color: green")
        self.healerHealthLabel.setGeometry(300,480,500,500)
  
        self.healerManaLabel= QLabel("MP: "+str(lux.mp),self)
        self.healerManaLabel.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        self.healerManaLabel.setStyleSheet("color: blue")
        self.healerManaLabel.setGeometry(300,460,500,500)

        


        #Pet Labels
        self.petNameLabel = QLabel(pomm.name,self)
        self.petNameLabel.setFont(QtGui.QFont("Times",14,QtGui.QFont.Bold))
        self.petNameLabel.setGeometry(500,500,500,500)

        self.petHealthLabel = QLabel("HP: "+ str(pomm.hp),self)
        self.petHealthLabel.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        self.petHealthLabel.setStyleSheet("color: green")
        self.petHealthLabel.setGeometry(500,480,500,500)
  
        self.petManaLabel= QLabel("MP: "+str(pomm.mp),self)
        self.petManaLabel.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        self.petManaLabel.setStyleSheet("color: blue")
        self.petManaLabel.setGeometry(500,460,500,500)

        
         
        #Monster labels

        #Level labels
        self.mapNameLabel = QLabel(map.name + "("+str(map.currentLevel)+"/"+str(map.maximumLevel)+")",self)
        self.mapNameLabel.setFont(QtGui.QFont("Times",20,QtGui.QFont.Bold))
        self.mapNameLabel.setGeometry(770,10,500,100)
        
        self.mapStoryLabel = QLabel(map.currentLevelString,self)
        self.mapStoryLabel.setFont(QtGui.QFont("Times",14,QtGui.QFont.Bold))
        self.mapStoryLabel.setGeometry(200,3,500,100)

        self.mapDifficultyLabel = QLabel(str(map.difficulty),self)
        self.mapDifficultyLabel.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))
        self.mapDifficultyLabel.setStyleSheet("color:red")
        self.mapDifficultyLabel.setGeometry(760,3,500,100)
   
        #Action buttons
        nextMapLevelButton = QPushButton("Next Level",self)
        nextMapLevelButton.move(800,300)
        nextMapLevelButton.clicked.connect(self.nextMapLevel)

        previousMapLevelButton = QPushButton("Previous Level",self)
        previousMapLevelButton.move(800,260)
        previousMapLevelButton.clicked.connect(self.previousMapLevel)

        
        
        self.show()
   
    @pyqtSlot()
    def previousMapLevel(self):
        if map.currentLevel == 1:
            return
        map.currentLevel = (map.currentLevel -1) 
        
        self.mapNameLabel.setText(map.name + "("+str(map.currentLevel)+"/"+str(map.maximumLevel)+")")
        self.mapStoryLabel.setText(map.getCurrentLevelInfo())

    def nextMapLevel(self):
        if map.currentLevel == 10:
            return
        map.currentLevel = (map.currentLevel +1)

        self.mapNameLabel.setText(map.name + "("+str(map.currentLevel)+"/"+str(map.maximumLevel)+")")

        self.mapStoryLabel.setText(map.getCurrentLevelInfo())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#################################################
