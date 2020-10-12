class Character:
    def __init__(self,name,hp,mp,weapon):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.weapon = weapon
        
    def getInfo(self):
        print("Name: %s, hp: %s, mp: %s, weapon: %s." % (self.name, self.hp, self.mp, self.weapon.name))



    def addWeapon(self):
        equiped = True
        self.weapon = weapon
        self.weapon.name = self.weapon.name
        
        
