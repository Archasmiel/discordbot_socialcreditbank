from tinydb import TinyDB, Query
import datetime
from datetime import datetime as t

User = Query()


async def get_usrcreditpair(dbname, user):
    db = TinyDB(dbname)
    return db.search(User.name == user)[0].get('name', 0), int(db.search(User.name == user)[0].get('credits', 0))


async def get_credits(dbname, user):
    db = TinyDB(dbname)
    return int(db.search(User.name == user)[0].get('credits', 0))


async def get_greettime(dbname, user):
    db = TinyDB(dbname)
    if db.search(User.name == user)[0].get('greet_time', 0) == 0:
        db.update({'greet_time': t.now().strftime("%d.%m.%Y %H:%M:%S")}, User.name == user)
    return db.search(User.name == user)[0].get('greet_time', 0)


async def get_testtime(dbname, user):
    db = TinyDB(dbname)
    if db.search(User.name == user)[0].get('test_last_time', 0) == 0:
        db.update({'test_last_time': t.now().strftime("%d.%m.%Y %H:%M:%S")}, User.name == user)
    return db.search(User.name == user)[0].get('test_last_time', 0)


async def get_userscredits(dbname, credit1, credit2):
    db = TinyDB(dbname)
    results = db.search(credit1 < User.credits < credit2)
    return results


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
