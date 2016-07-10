import sqlite3

def getDatabase(name):
    return sqlite3.connect(name)

def getMaxIndex(database):
    cursor = database.cursor()
    cmd = "SELECT MAX(id) AS id FROM DICT"
    resObj = cursor.execute(cmd)
    res = resObj.fetchone()
    return res[0]

def getWordPair(database, index):
    cursor = database.cursor()
    cmd = "SELECT pashto,english FROM DICT where id=?"
    resObj = cursor.execute(cmd, (str(index),))
    res = resObj.fetchone()
    return res

