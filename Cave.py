from Map import Map

class Cave(Map):
    def __init__(self,name, difficulty ):
        super().__init__(name, difficulty)

    def getMainStory(self):
        return "This is the main story"