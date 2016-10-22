from database import Database as DB

db = DB()

db.insert({'light': 0, 'acc': 5.0, 'tmp': 10.0, 'baro': 999.0})
db.insert({'light': 1, 'acc': 5.0, 'tmp': 10.0, 'baro': 100.0})
