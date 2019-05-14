import pymongo

class MongoStatic:
    def __init__(self, inHost):
        self.dHost = inHost
        self.client = pymongo.MongoClient(self.dHost)

    def dBaseList(self):
        return self.client.list_database_names()

    def baseCheck(self, inBase):
        self.dBase = inBase
        if inBase in self.dBaseList():
            return False
        else:
            return True

    def baseCreate(self, inBase):
        self.inBase = inBase
        self.myDb = self.client[self.inBase]

    def collectionCreate(self, inColl):
        self.posts = self.myDb[inColl]

    def toCollection(self, postData):
        self.postData = postData
        result = self.posts.insert_one(postData)

    def collectionFindAll():
        return

testInstance = MongoStatic('mongodb://localhost:27017')
print(testInstance.dBaseList())
if testInstance.baseCheck('pymongo_gest'):
    testInstance.baseCreate('pymongo_gest')
    testInstance.collectionCreate('test')
    testInstance.toCollection({'title': 'mongo', 'content': 'mongo again', 'author': 'no mongo'})
else:
    print('Nope')
