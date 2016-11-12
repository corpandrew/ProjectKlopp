class Player:

    def __init__(self, name, jerseyNumber, teamName):
        self.name = name
        self.jerseyNumber = jerseyNumber
        self.teamName = teamName

    def getName(self):
        return self.name

    def getJerseyNumber(self):
        return self.jerseyNumber

    def getTeamName(self):
        return self.teamName