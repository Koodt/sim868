import sqlite3

dbConnect = sqlite3.connect('/srv/testing.db')
dbCursor = dbConnect.cursor()
dbCursor.execute('CREATE TABLE testTable (Count INTEGER, Item TEXT, Quantity INTEGER)')
dbConnect.commit()
dbConnect.close()
