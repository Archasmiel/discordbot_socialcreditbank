from tinydb import TinyDB, Query
from datetime import datetime as t

User = Query()


async def get_usrcreditpair(dbname, user):
    return TinyDB(dbname).search(User.name == user)[0].get('name', 0), int(db.search(User.name == user)[0].get('credits', 0))


async def get_credits(dbname, user):
    return int(TinyDB(dbname).search(User.name == user)[0].get('credits', 0))


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
    return TinyDB(dbname).search(credit1 < User.credits < credit2)
