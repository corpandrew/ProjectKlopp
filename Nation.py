class Nation:
    def __init__(self,largeImageUrl,abbrName,id,imgUrl,name):
        self.largeImageUrl = largeImageUrl
        self.abbrName = abbrName
        self.id = id
        self.imgUrl = imgUrl
        self.name = name

    def getLargeImageUrl(self):
        return self.largeImageUrl

    def getAbbrName(self):
        return self.abbrName

    def getId(self):
        return self.id

    def getImgUrl(self):
        return self.imgUrl

    def getName(self):
        return self.name
