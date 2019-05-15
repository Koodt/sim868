class MongoStatic:
    def __init__(self, inBase, inHost):
        import pymongo
        self.dBase = inBase
        self.dHost = inHost
        self.client = pymongo.MongoClient(self.dHost)

    def dBaseList(self):
        return self.client.list_database_names()

    def baseCheck(self):
        if self.dBase in self.dBaseList():
            return False
        else:
            return True

    def baseCreate(self):
        self.myDb = self.client[self.dBase]

    def collectionCreate(self, inColl):
        self.posts = self.myDb[inColl]

    def toCollection(self, postData):
        self.postData = postData
        result = self.posts.insert_one(postData)

    def collectionFindAll():
        return
