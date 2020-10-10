class Weapon:
    def __init__(self,name,attack,defense):
        self.name = name
        self.attack = attack
        self.defense = defense
    def getInfo(self):
        print(self.name, self.attack, self.defense)

class BasicSword(Weapon):
    def __init__(self,name,attack,defense):
        super().__init__(name,attack,defense)