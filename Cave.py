from Map import Map

class Cave(Map):
    def __init__(self,name, difficulty,currentLevel,maximumLevel ):
        super().__init__(name, difficulty,currentLevel,maximumLevel)

    def getMainStory(self):
        return "This is the main story"