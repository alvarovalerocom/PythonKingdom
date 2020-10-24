#durability = each attack -1 
class Weapon:
    def __init__(self,name,attack,defense,durability):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.durability = durability
    def getInfo(self):
        if self.name == False:
            return "no weapon equiped"
        else:
            print(self.name, self.attack, self.defense)
    

    #def setWeapon(self):

class BasicSword(Weapon):
    def __init__(self,name,attack,defense,durability):
        super().__init__("Basic Sword",attack,defense,durability)

class LightStick(Weapon):
    def __init__(self,name,attack,defense,durability):
        super().__init__("Light Stick",attack, defense, durability)
