from Database import Database as DB

db = DB()

print(db.createQuery({'light': 1, 'acc': 5.0, 'tmp': 10.0, 'baro': 100.0}))
#db.insertSet('INSERT INTO data VALUES(\'2007-01-01 10:00:00\', 1, 1.0, 5.0, 10.0)')
#db.insertSet('INSERT INTO data VALUES(\'2007-01-01 10:00:01\', 0, 1.0, 5.0, 10.0)')
