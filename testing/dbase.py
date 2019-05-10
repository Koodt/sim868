from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
dbase  = client.pymongo_test
posts  = dbase.posts

post_data = {
    'title': 'mongo',
    'content': 'mongo again',
    'author': 'no mongo'
}

result = posts.insert_one(post_data)

print('Post: %s' % result.inserted_id)
