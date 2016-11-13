class Club:
    def __init__(self, darkLargeImageUrl, normalLargeImageUrl, abbrName, id, imgUrl, name):
        self.darkLargeImageUrl = darkLargeImageUrl
        self.normalLargeImageUrl = normalLargeImageUrl
        self.abbrName = abbrName
        self.id = id
        self.imgUrl = imgUrl
        self.name = name

    def getDarkLargeImageUrl(self):
        return self.darkLargeImageUrl

    def getNormalLargeImageUrl(self):
        return self.normalLargeImageUrl

    def getAbbrName(self):
        return self.abbrName

    def getId(self):
        return self.id

    def getImgUrl(self):
        return self.imgUrl

    def getName(self):
        return self.name
