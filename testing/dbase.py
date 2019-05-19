class MongoStatic:
    def __init__(self, inBase, inHost):
        import pymongo
        self.dBase = inBase
        self.dHost = inHost
        self.client = pymongo.MongoClient(self.dHost)

    def baseList(self):
        return self.client.list_database_names()

    def collList(self):
        return self.client.self.dBase.list_collection_names()

    def baseCheck(self):
        if self.dBase in self.baseList():
            return False
        else:
            return True

    def collCheck(self):
        if self.inColl in self.baseCheck():
            return False
        else:
            return True

    def baseCreate(self):
        self.myDb = self.client[self.dBase]

    def collectionCreate(self, inColl):
        self.posts = self.dBase[inColl]

    def toCollection(self, postData):
        self.postData = postData
        result = self.posts.insert_one(postData)

    def collectionFindAll():
        return

testInstance = MongoStatic('pymongo_guest', 'mongodb://localhost:27017')
print(testInstance.baseList())
if testInstance.baseCheck():
    testInstance.baseCreate()
else:
    print('Dbase exist')

if testInstance.colCheck():
    testInstance.collectionCreate('test')
    testInstance.toCollection({'title': 'mongo', 'content': 'mongo again', 'author': 'no mongo'})
