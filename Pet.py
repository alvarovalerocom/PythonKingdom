from Character import Character

class Pet(Character):
    def __init__(self,name,hp,mp,weapon):
        super().__init__(name,hp,mp,weapon)

    def carryItems(self):
        pass
