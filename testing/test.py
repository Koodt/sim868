#!/usr/bin/python3

import sqlite3

dbConnect = sqlite3.connect('/srv/testing.db')
dbCursor = dbConnect.cursor()
dbCursor.execute('CREATE TABLE IF NOT EXISTS storeTable (ID int NOT NULL AUTO_INCREMENT, Item varchar(255) NOT NULL, Quantity int NOT NULL, PRIMARY KEY (ID))')
#dbCursor.execute('INSERT INTO testTable VALUES ()')
dbConnect.commit()
dbConnect.close()
