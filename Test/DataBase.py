# -
# @pyVersion: 3.6

import os
import os.path
import sqlite3
import hashlib

home = os.path.expanduser('~')
dbpath = os.path.join(home, '.ObjectManagerSystem', 'LibraryManagement.db')

if '.ObjectManagerSystem' not in os.listdir(home):
    os.mkdir(os.path.join(home, '.ObjectManagerSystem'))

createUserTableString = """
CREATE TABLE IF NOT EXISTS user(
    userid VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(20),
    Password CHAR(32)
)"""

createObjectTableString = """
CREATE TABLE IF NOT EXISTS Objections(
    ObjectName VARCHAR(30),
    price INT,
    describe VARCHAR(60),
    PublishTime DATE,
    Publisher VARCHAR(20),
    Buyer VARCHAR(20)
)"""


class DbManager(object):

    def __init__(self, *args):
        self.db = sqlite3.connect(*args)
        self.cursor = self.db.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, types, value, traceback):
        self.db.commit()

        return False

    def __del__(self):
        self.db.commit()
        self.db.close()

    def switchDb(self, *args):
        self.db.close()

        self.db = sqlite3.connect(*args)
        self.cursor = self.db.cursor()

    def createTable(self, tableString):
        self.cursor.execute(tableString)
        self.db.commit()

    def commitAndClose(self):
        self.db.commit()
        self.db.close()


class UserManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createUserTableString)

    def adduser(self, userid, password):
        '''  添加用户    '''
        insertData = self.cursor.execute(
            """INSERT OR IGNORE INTO user (userid, password) 
            VALUES ('{0}', '{1}')""".format(userid, password))
        self.db.commit()

    def getuser(self):
        ''' 获取所有注册账户'''
        result = self.cursor.execute(
            "SELECT userid,password FROM user")
        return result.fetchall()

    def addObject(self, ObjectName, price, describe, PublishTime, Publisher, Buyer):
        '''  添加商品    '''
        time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        insertData = self.cursor.execute("""INSERT INTO Object 
                (ObjectName,ObjectID, Auth, Category,Publisher,PublishTime,NumStorage,NumCanBuy,NumBuyed) VALUES 
                ('{0}', '{1}', '{2}','{3}','{4}','{5}')
                """.format(ObjectName, price, describe, time, Publisher, Buyer))
        self.db.commit()


class ObjectManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createObjectTableString)

    def initDatabase(self):
        self.addObject('草料', 3, '苏格兰牧场名马专供', '1999-01-01', 'admin')

    def check_object(self, theObjectName, thePublisher):
        '''  添加是否已经存在商品    '''
        result = self.cursor.execute(
            "SELECT *  FROM objections WHERE ObjectName = '%s' and Publisher = '%s'" % (theObjectName, thePublisher))
        return result.fetchall()

    def addObject(self, ObjectName, price, describe, PublishTime, Publisher):
        '''  添加商品    '''
        self.cursor.execute("""INSERT OR IGNORE INTO Objections 
                (ObjectName, price, describe, PublishTime, Publisher) VALUES 
                ('{0}', '{1}', '{2}','{3}','{4}')
                """.format(ObjectName, price, describe, PublishTime, Publisher))
        self.db.commit()

    def getObjectInfo(self):
        ''' 获取所有商品信息'''
        result = self.cursor.execute(
            "SELECT ObjectName, price, describe, PublishTime, Publisher, Buyer FROM Objections ")
        return result.fetchall()

    def searchObject(self, user_id):
        result = self.cursor.execute(
            "SELECT ObjectName, price, describe, PublishTime, Publisher FROM Objections WHERE Publisher ='%s'" % user_id)
        return result.fetchall()

    def searchbuyObject(self, user_id):
        result = self.cursor.execute(
            "SELECT ObjectName, price, describe, PublishTime, Publisher FROM Objections WHERE Buyer = '%s'" % user_id)
        return result.fetchall()

    def getMyObject(self, name):
        ''' 获取所有我上架的商品信息'''
        result = self.cursor.execute(
            "SELECT ObjectName, price, describe, PublishTime FROM Objections WHERE Publisher='%s'" % name)
        return result.fetchall()

    def buyObject(self, object_name, user_id):
        self.cursor.execute("UPDATE Objections SET  Buyer = '%s' WHERE ObjectName = '%s'" % (user_id, object_name))
        self.db.commit()
