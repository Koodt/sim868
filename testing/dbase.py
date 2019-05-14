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
        dBase = self.client.self.inBase

    def collectionCreate():
        self.posts = self.dBase.posts

    def toCollection():
        post_data = {
            'title': 'mongo',
            'content': 'mongo again',
            'author': 'no mongo'
        }
        result = posts.insert_one(post_data)

    def collectionFindAll():
        return

testInstance = MongoStatic('mongodb://localhost:27017')
print(testInstance.dBaseList())
if testInstance.baseCheck('pymongo_test'):
    testInstance.baseCreate('pymongo_est')
else:
    print('Nope')
