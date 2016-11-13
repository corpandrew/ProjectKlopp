class League:
    def __init__(self, abbrName, id, imgUrl, name):
        self.abbrName = abbrName
        self.id = id
        self.imgUrl = imgUrl
        self.name = name

    def getAbbrName(self):
        return self.abbrName

    def getId(self):
        return self.id

    def getImgUrl(self):
        return self.imgUrl

    def getName(self):
        return self.name