from Map import Map

class Cave(Map):
    def __init__(self,name, difficulty,currentLevel,maximumLevel,currentLevelString ):
        super().__init__(name, difficulty,currentLevel,maximumLevel,currentLevelString)

    def getMainStory(self):
        return "This is the main story"


    def getCurrentLevelInfo(self):
        if self.currentLevel == 1:
            self.currentLevelString = "1 part of the story"

        if self.currentLevel == 2:
            self.currentLevelString = "2 part of the story"

        if self.currentLevel == 3:
            self.currentLevelString = "3 part of the story"

        if self.currentLevel == 4:
            self.currentLevelString = "4 part of the story"

        if self.currentLevel == 5:
            self.currentLevelString = "5 part of the story"

        if self.currentLevel == 6:
            self.currentLevelString = "6 part of the story"

        if self.currentLevel == 7:
            self.currentLevelString = "7 part of the story"

        if self.currentLevel == 8:
            self.currentLevelString = "8 part of the story"

        if self.currentLevel == 9:
            self.currentLevelString = "9 part of the story"

        if self.currentLevel == 10:
            self.currentLevelString = "10 part of the story"

        return self.currentLevelString

