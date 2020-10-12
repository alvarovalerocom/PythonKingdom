from Character import Character

class Hero(Character):
    def __init__(self,name,hp,mp,weapon, ultimate):
        super().__init__(name,hp,mp,weapon)
        self.ultimate = ultimate

    def getInfo(self):
        print(self.name, self.hp)