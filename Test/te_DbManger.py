# -*- coding: utf-8 -*-
# @Date     : 2018-12-12 15:31:22
# @Author   : Jimy_Fengqi (jmps515@163.com)
# @Link     : https://blog.csdn.net/qiqiyingse
# @Version  : V1.0
# @pyVersion: 3.6

import os
import os.path
import sqlite3
import hashlib

home = os.path.expanduser('~')

if '.ObjectManagerSystem' not in os.listdir(home):
    os.mkdir(os.path.join(home, '.ObjectManagerSystem'))

dbpath = os.path.join(home, '.ObjectManagerSystem', 'LibraryManagement.db')

createUserTableString = """
CREATE TABLE IF NOT EXISTS user(
    userid CHAR(10) PRIMARY KEY ,
    Name VARCHAR(20),
    Password CHAR(32),
    IsAdmin BIT,
    TimesBuyed INT,
    NumBuyed INT    
)"""

createUser_ObjectTableString = """
CREATE TABLE IF NOT EXISTS User_Object(
    userid CHAR(10),
    ObjectID CHAR(6) PRIMARY KEY,
    BuyTime DATE,
    ReturnTime DATE,
    BuyState BIT
)"""

createObjectTableString = """
CREATE TABLE IF NOT EXISTS Object(
    ObjectName VARCHAR(30),
    ObjectID CHAR(6),
    Auth VARCHAR(20),
    Category VARCHAR(10),
    Publisher VARCHAR(20),
    PublishTime DATE,
    NumStorage INT,
    NumCanBuy INT,
    NumBuyed INT 
)"""

createAddOrDropObjectTableString = """
CREATE TABLE IF NOT EXISTS AddOrDrop(
    ObjectID CHAR(6),
    ModifyTime  DATE,
    AddOrDrop INT,
    Numbers INT    
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
        self.createTable(createUser_ObjectTableString)

    def queryBuyObject(self, userid, ObjectID):
        result = self.cursor.execute(
            "SELECT * FROM User_Object WHERE userid='%s' AND ObjectID='%s' AND BuyState=1" % (userid, ObjectID))
        return result.fetchall()

    def countBuyNum(self, userid):
        result = self.cursor.execute(
            " SELECT COUNT(userid) FROM User_Object WHERE userid='%s' AND BuyState=1" % (userid))
        return result.fetchall()

    def BuyStatus(self, userid, ObjectID):
        result = self.cursor.execute(
            "SELECT COUNT(userid) FROM User_Object WHERE  userid='%s' AND ObjectID='%s' AND BuyState=1" % (
                userid, ObjectID))
        return result.fetchall()

    def BuyOrReturnObject(self, userid, ObjectID, timenow, Buyflag=1):
        if Buyflag == 1:
            result = self.cursor.execute(
                "INSERT INTO User_Object VALUES ('%s','%s','%s',NULL,1)" % (userid, ObjectID, timenow))
        else:
            result = self.cursor.execute(
                "UPDATE User_Object SET ReturnTime='%s',BuyState=0 WHERE userID='%s' AND ObjectID='%s' AND BuyState=1" % (
                timenow, userid, ObjectID))
        self.db.commit()


class AddOrDropManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createAddOrDropObjectTableString)

    def initDatabase(self):
        self.insertValue('IS1000', '2018-04-22', 1, 100)
        self.insertValue('IS1001', '2018-04-22', 1, 14)
        self.insertValue('IS1002', '2018-04-22', 1, 24)
        self.insertValue('IS1003', '2018-04-22', 1, 45)
        self.insertValue('IS1004', '2018-04-22', 1, 100)
        self.insertValue('IS1004', '2018-04-27', 1, 45)
        self.insertValue('IS1005', '2018-04-27', 1, 45)
        self.insertValue('IS1006', '2018-04-28', 1, 10)
        self.insertValue('IS1007', '2018-04-28', 1, 23)
        self.insertValue('IS1008', '2018-04-28', 1, 50)
        self.insertValue('IS1009', '2018-04-28', 1, 50)
        self.insertValue('IS1010', '2018-04-28', 1, 50)
        self.insertValue('IS1011', '2018-04-28', 1, 50)
        self.insertValue('IS1012', '2018-04-28', 1, 50)
        self.insertValue('IS1013', '2018-04-28', 1, 50)
        self.insertValue('IS1014', '2018-04-28', 1, 50)
        self.insertValue('IS1015', '2018-04-28', 1, 50)
        self.insertValue('IS1016', '2018-04-28', 1, 50)
        self.insertValue('IS1017', '2018-04-28', 1, 50)
        self.insertValue('IS1018', '2018-04-28', 1, 50)
        self.insertValue('IS1019', '2018-04-28', 1, 50)
        self.insertValue('IS1020', '2018-04-28', 1, 50)
        self.insertValue('IS1021', '2018-04-28', 1, 50)
        self.insertValue('IS1022', '2018-04-28', 1, 50)
        self.insertValue('IS1023', '2018-04-28', 1, 50)
        self.insertValue('IS1024', '2018-04-28', 1, 50)
        self.insertValue('IS1025', '2018-04-28', 1, 50)
        self.insertValue('IS1026', '2018-04-28', 1, 100)
        self.insertValue('IS1027', '2018-04-28', 1, 50)
        self.insertValue('IS1029', '2018-04-28', 1, 50)
        self.insertValue('IS1030', '2018-04-28', 1, 50)
        self.insertValue('IS1031', '2018-04-28', 1, 50)
        self.insertValue('IS1032', '2018-04-28', 1, 50)
        self.insertValue('IS1033', '2018-04-28', 1, 50)
        self.insertValue('IS1034', '2018-04-28', 1, 50)

    def insertValue(self, ObjectID, time, AddorDrop, addObjectNum):
        insertData = self.cursor.execute(
            "INSERT INTO AddOrDrop VALUES ('%s','%s',%d,%d)" % (ObjectID, time, AddorDrop, addObjectNum))
        self.db.commit()

    def addinfo(self, ObjectID, time, addObjectNum):
        self.insertValue(ObjectID, time, 1, addObjectNum)

    def dropinfo(self, ObjectID, time, addObjectNum):
        self.insertValue(ObjectID, time, 0, addObjectNum)

    def getAllinfo(self):
        '''获得所有书籍'''
        fetchedData = self.cursor.execute("SELECT * from AddOrDrop ")
        return fetchedData.fetchall()


class ObjectDbManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createObjectTableString)

    def initDatabase(self):
        self.addObject('力学', 'IS1000', '刘斌', '教育', '中国科学技术大学 ', '1999-01-01', 100, 100, 0)
        self.addObject('微积分', 'IS1001', '牛顿莱布尼兹', '教育', '中国科学技术大学', '1998-01-01', 14, 14, 0)
        self.addObject('电磁场论', 'IS1002', '叶邦角', '教育', '中国科学技术大学', '1997-01-01', 24, 24, 0)
        self.addObject('热学', 'IS1003', '张鹏飞', '教育', '中国科学技术大学', '2002-01-01', 45, 45, 0)
        self.addObject('电动力学', 'IS1004', '叶邦角', '教育', '中国科学技术大学', '2003-01-01', 100, 100, 0)
        self.addObject('数据库', 'IS1006', '袁平波', '教育', '中国科学技术大学', '2010-01-01', 10, 10, 0)
        self.addObject('电磁学', 'IS1005', '叶邦角', '教育', '中国科学技术大学 ', '2012-01-01', 43, 43, 0)
        self.addObject('数学分析', 'IS1007', '陈卿', '教育', '中国科学技术大学', '2013-01-01', 23, 23, 0)
        self.addObject('吉米多维奇题解1', 'IS1008', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addObject('吉米多维奇题解2', 'IS1009', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addObject('吉米多维奇题解3', 'IS1010', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addObject('吉米多维奇题解4', 'IS1011', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addObject('吉米多维奇题解5', 'IS1012', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addObject('吉米多维奇题解6', 'IS1013', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0)
        self.addObject('朗道力学', 'IS1014', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道电动力学', 'IS1015', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道量子力学', 'IS1016', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道量子电动力学', 'IS1017', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道统计物理学', 'IS1018', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道流体力学', 'IS1019', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道弹性理论力学', 'IS1020', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('朗道物理动力学', 'IS1021', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0)
        self.addObject('植物学', 'IS1022', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addObject('动物学', 'IS1023', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addObject('细胞生物学', 'IS1024', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addObject('动物生理学', 'IS1025', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addObject('古生物学', 'IS1026', '佚名', '生物学', '高等教育出版社', '2011-05-01', 100, 100, 0)
        self.addObject('高等数学', 'IS1027', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addObject('线性代数', 'IS1029', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0)
        self.addObject('C++程序设计', 'IS1030', '孙广中', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addObject('C程序设计', 'IS1031', '郑重', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addObject('数据结构', 'IS1032', '顾为兵', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addObject('信号与系统', 'IS1033', '李卫平', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)
        self.addObject('线性电子线路', 'IS1034', '陆伟', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0)

    def addObject(self, ObjectName, ObjectID, Auth, Category, Publisher, PublishTime, NumStorage, NumCanBuy, NumBuyed):
        '''  添加书籍    '''
        insertData = self.cursor.execute("""INSERT INTO Object 
                (ObjectName,ObjectID, Auth, Category,Publisher,PublishTime,NumStorage,NumCanBuy,NumBuyed) VALUES 
                ('{0}', '{1}', '{2}','{3}','{4}','{5}','{6}','{7}','{8}')
                """.format(ObjectName, ObjectID, Auth, Category, Publisher, PublishTime, NumStorage, NumCanBuy,
                           NumBuyed))
        self.db.commit()

    def dropObject(self, ObjectId):
        insertData = self.cursor.execute("DELETE  FROM Object WHERE ObjectID='%s'" % (ObjectId))
        self.db.commit()

    def updateObjectinfo(self, addObjectNum, ObjectId, addFlag=1):
        if addFlag == 1:
            self.cursor.execute(
                "UPDATE Object SET NumStorage=NumStorage+%d,NumCanBuy=NumCanBuy+%d WHERE ObjectID='%s'" % (
                    addObjectNum, addObjectNum, ObjectId))
        else:
            self.cursor.execute(
                "UPDATE Object SET NumStorage=NumStorage-%d,NumCanBuy=NumCanBuy-%d WHERE ObjectID='%s'" % (
                    addObjectNum, addObjectNum, ObjectId))
        self.db.commit()

    def getObjectinfo(self):
        '''获得所有书籍'''
        fetchedData = self.cursor.execute("SELECT * from Object ")
        return fetchedData.fetchall()

    def querybyObjectID(self, ObjectID):
        fetchedData = self.cursor.execute("SELECT * FROM Object WHERE ObjectID='%s'" % (ObjectID))
        return fetchedData.fetchall()
        # return self.queryObjectByKeywords(userid)

    def queryObjectByKeywords(self, keywords):
        fetchedData = self.cursor.execute("SELECT * from Object ORDER BY %s limit %s,%s" % (keywords, 0, 5))
        return fetchedData.fetchall()

    def BuyOrReturnObject(self, ObjectID, Buyflag=1):
        if Buyflag == 1:
            fetchedData = self.cursor.execute(
                "UPDATE Object SET NumCanBuy=NumCanBuy-1,NumBuyed=NumBuyed+1 WHERE ObjectID='%s'" % ObjectID)
        else:
            fetchedData = self.cursor.execute(
                "UPDATE Object SET NumCanBuy=NumCanBuy+1,NumBuyed=NumBuyed-1 WHERE ObjectID='%s'" % ObjectID)
        self.db.commit()


class UserDbManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createUserTableString)

    def initDatabase(self):

        password = 'admin123'
        hl = hashlib.md5()  # 将密码进行md5加密
        hl.update(password.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        self.addAdminUser('admin', 'Fengqi', md5password)  # 添加管理员账号

        password = 'user123'
        hl = hashlib.md5()  # 将密码进行md5加密
        hl.update(password.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        self.addUser('user000000', 'user000000', md5password)  # 添加普通用户

    def addUser(self, userid, Name, Password, IsAdmin=0):
        '''  添加普通用户    '''
        insertData = self.cursor.execute("""INSERT OR IGNORE INTO user 
                (userid, Name, Password,IsAdmin,TimesBuyed,NumBuyed) VALUES 
                ('{0}', '{1}', '{2}','{3}','{4}','{5}')
                """.format(userid, Name, Password, IsAdmin, 0, 0))
        self.db.commit()

    def addAdminUser(self, userid, Name, Password):
        ''' 添加管理员用户'''
        self.addUser(userid, Name, Password, IsAdmin=1)

    def querybyUserid(self, userid):
        fetchedData = self.cursor.execute("SELECT * FROM user WHERE userid='%s'" % (userid))
        # a=fetchedData.fetchall()#通过fetchall接受全部数据，是一个list,list的每个元素是tuple类型数据

        return fetchedData.fetchall()

    def getAdmineUserinfo(self):
        '''获取管理员用户 '''
        fetchedData = self.cursor.execute("SELECT userid,Name FROM user WHERE IsAdmin=1")
        return fetchedData

    def getUserinfo(self):
        '''获取一般用户'''
        fetchedData = self.cursor.execute("SELECT userid,Name FROM user WHERE IsAdmin=0")
        return fetchedData

    def updatePassword(self, password, userid):
        fetchedData = self.cursor.execute("UPDATE User SET Password='%s' WHERE userid=%s" % (password, userid))
        self.db.commit()

    def BuyOrReturnObject(self, userid, Buy=1):
        if Buy == 1:
            fetchedData = self.cursor.execute(
                "UPDATE User SET TimesBuyed=TimesBuyed+1,NumBuyed=NumBuyed+1 WHERE userid='%s'" % userid)
        else:
            fetchedData = self.cursor.execute(
                "UPDATE User SET TimesBuyed=TimesBuyed-1,NumBuyed=NumBuyed-1 WHERE userid='%s'" % userid)
        self.db.commit()


def testuserdb():
    userDb = UserDbManager()
    userDb.addAdminUser('admin', 'admin', '123456')
    userDb.addAdminUser('administrator', 'admin1', '123456')
    userDb.addUser('Test', 'AAA', '123456')
    userDb.addUser('Test1', 'BBB', '123456')
    userDb.addUser('Test2', 'CCC', '123456')
    userDb.getAdmineUserinfo()
    userDb.getUserinfo()
    #queryUser('admins')
    #userDb.queryUser('admin')


def testAddDropObjectData():
    userDb = AddOrDropManager()

    allObject = userDb.getAllinfo()
    for Object in allObject:
        print(Object)
        # print(" ".join('%s' %ids for ids in a))
        # a=list(Object)
        # print(a)


def testObjectDB():
    userDb = ObjectDbManager()
    if len(userDb.querybyObjectID('IS1006')):
        print('书籍已经存在，更新数量')
        userDb.updateObjectinfo(10, 'IS1005')
    else:
        print('书籍不存在，直接插入')
        userDb.addObject('力学3', 'IS1006', '刘斌3', '教育', '中国科学技术大学', '1999-01-01', '34', '34', '1')

    allObject = userDb.getObjectinfo()

    print('all Object length =%d' % len(allObject))
    for Object in allObject:
        print(Object)

    print('按照Objectid查询')
    Objectid = userDb.querybyObjectID('IS1006')
    if len(Objectid):
        print(Objectid)

    print('按照auth排序查询前几页')
    keyObject = userDb.queryObjectByKeywords('Auth')
    print(keyObject)


if __name__ == '__main__':
    testuserdb()
    testAddDropObjectData()
    testObjectDB()


class ObjectDbManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createObjectTableString)

    def dropObject(self, ObjectName, userid):
        insertData = self.cursor.execute(
            "DELETE  FROM Object WHERE ObjectName='%s' AND userid ='%s '" % (ObjectName, userid)))
        self.db.commit()

    def updateObjectinfo(self, addObjectNum, ObjectId, addFlag=1):
        if addFlag == 1:
            self.cursor.execute(
                "UPDATE Object SET NumStorage=NumStorage+%d,NumCanBuy=NumCanBuy+%d WHERE ObjectID='%s'" % (
                    addObjectNum, addObjectNum, ObjectId))
        else:
            self.cursor.execute(
                "UPDATE Object SET NumStorage=NumStorage-%d,NumCanBuy=NumCanBuy-%d WHERE ObjectID='%s'" % (
                    addObjectNum, addObjectNum, ObjectId))
        self.db.commit()

    def getObjectinfo(self):
        #获得所有书籍
        fetchedData = self.cursor.execute("SELECT * from Object ")
        return fetchedData.fetchall()

    def querybyObjectID(self, ObjectID):
        fetchedData = self.cursor.execute("SELECT * FROM Object WHERE ObjectID='%s'" % (ObjectID))
        return fetchedData.fetchall()
        # return self.queryObjectByKeywords(userid)

    def queryObjectByKeywords(self, keywords):
        fetchedData = self.cursor.execute("SELECT * from Object ORDER BY %s limit %s,%s" % (keywords, 0, 5))
        return fetchedData.fetchall()

    def BuyOrReturnObject(self, ObjectID, Buyflag=1):
        if Buyflag == 1:
            fetchedData = self.cursor.execute(
                "UPDATE Object SET NumCanBuy=NumCanBuy-1,NumBuyed=NumBuyed+1 WHERE ObjectID='%s'" % ObjectID)
        else:
            fetchedData = self.cursor.execute(
                "UPDATE Object SET NumCanBuy=NumCanBuy+1,NumBuyed=NumBuyed-1 WHERE ObjectID='%s'" % ObjectID)
        self.db.commit()


class UserDbManager(DbManager):
    def __init__(self, database=dbpath, *args):
        super().__init__(database, *args)
        self.initDb()

    def initDb(self):
        self.createTable(createUserTableString)

    def initDatabase(self):

        password = 'admin123'
        hl = hashlib.md5()  # 将密码进行md5加密
        hl.update(password.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        self.addAdminUser('admin', 'Fengqi', md5password)  # 添加管理员账号

        password = 'user123'
        hl = hashlib.md5()  # 将密码进行md5加密
        hl.update(password.encode(encoding='utf-8'))
        md5password = hl.hexdigest()
        self.addUser('user000000', 'user000000', md5password)  # 添加普通用户

    def addUser(self, userid, Name, Password, IsAdmin=0):
        #  添加普通用户
        insertData = self.cursor.execute("""INSERT OR IGNORE INTO user 
                (userid, Name, Password,IsAdmin,TimesBuyed,NumBuyed) VALUES 
                ('{0}', '{1}', '{2}','{3}','{4}','{5}')
                """.format(userid, Name, Password, IsAdmin, 0, 0))
        self.db.commit()

    def addAdminUser(self, userid, Name, Password):
        ''' 添加管理员用户'''
        self.addUser(userid, Name, Password, IsAdmin=1)

    def querybyUserid(self, userid):
        fetchedData = self.cursor.execute("SELECT * FROM user WHERE userid='%s'" % (userid))
        # a=fetchedData.fetchall()#通过fetchall接受全部数据，是一个list,list的每个元素是tuple类型数据

        return fetchedData.fetchall()

    def getAdmineUserinfo(self):
     #   '''获取管理员用户 '''
        fetchedData = self.cursor.execute("SELECT userid,Name FROM user WHERE IsAdmin=1")
        return fetchedData

    def getUserinfo(self):
      #  '''获取一般用户'''
        fetchedData = self.cursor.execute("SELECT userid,Name FROM user WHERE IsAdmin=0")
        return fetchedData

    def updatePassword(self, password, userid):
        fetchedData = self.cursor.execute("UPDATE User SET Password='%s' WHERE userid=%s" % (password, userid))
        self.db.commit()

    def BuyOrReturnObject(self, userid, Buy=1):
        if Buy == 1:
            fetchedData = self.cursor.execute(
                "UPDATE User SET TimesBuyed=TimesBuyed+1,NumBuyed=NumBuyed+1 WHERE userid='%s'" % userid)
        else:
            fetchedData = self.cursor.execute(
                "UPDATE User SET TimesBuyed=TimesBuyed-1,NumBuyed=NumBuyed-1 WHERE userid='%s'" % userid)
        self.db.commit()


def testuserdb():
    userDb = UserDbManager()
    userDb.addAdminUser('admin', 'admin', '123456')
    userDb.addAdminUser('administrator', 'admin1', '123456')
    userDb.addUser('Test', 'AAA', '123456')
    userDb.addUser('Test1', 'BBB', '123456')
    userDb.addUser('Test2', 'CCC', '123456')
    userDb.getAdmineUserinfo()
    userDb.getUserinfo()
    # queryUser('admins')
    # userDb.queryUser('admin')


def testAddDropObjectData():
    userDb = AddOrDropManager()

    allObject = userDb.getAllinfo()
    for Object in allObject:
        print(Object)
        # print(" ".join('%s' %ids for ids in a))
        # a=list(Object)
        # print(a)


def testObjectDB():
    userDb = ObjectDbManager()
    if len(userDb.querybyObjectID('IS1006')):
        print('书籍已经存在，更新数量')
        userDb.updateObjectinfo(10, 'IS1005')
    else:
        print('书籍不存在，直接插入')
        userDb.addObject('力学3', 'IS1006', '刘斌3', '教育', '中国科学技术大学', '1999-01-01', '34', '34', '1')

    allObject = userDb.getObjectinfo()

    print('all Object length =%d' % len(allObject))
    for Object in allObject:
        print(Object)

    print('按照Objectid查询')
    Objectid = userDb.querybyObjectID('IS1006')
    if len(Objectid):
        print(Objectid)

    print('按照auth排序查询前几页')
    keyObject = userDb.queryObjectByKeywords('Auth')
    print(keyObject)


if __name__ == '__main__':
    testuserdb()
    testAddDropObjectData()
    testObjectDB()