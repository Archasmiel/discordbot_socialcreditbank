from tinydb import TinyDB, Query
from datetime import datetime as t

User = Query()


async def insert(dbname, user, credit):
    db = TinyDB(dbname)
    db.insert({'name': user, 'credits': credit})


async def update(dbname, user, credit):
    db = TinyDB(dbname)
    db.update({'credits': credit}, User.name == user)


async def updategreettime(dbname, user, time):
    db = TinyDB(dbname)
    db.update({'greet_time': time}, User.name == user)


async def updatetesttime(dbname, user, time):
    db = TinyDB(dbname)
    db.update({'test_last_time': time}, User.name == user)


async def updatetestmode(dbname, user, mode):
    db = TinyDB(dbname)
    db.update({'test_mode': mode}, User.name == user)


async def search(dbname, user):
    db = TinyDB(dbname)
    results = db.search(User.name == user)
    return results
