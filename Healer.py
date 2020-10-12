from Character import Character

class Healer(Character):
    def __init__(self, name, hp , mp , weapon, heal):
        super().__init__(name, hp, mp,weapon)
        self.heal = heal

    def castHeal(self):
        return "healed"
