from Login_pane import LoginPane
from Index_pane import IndexPane
from register_pane import RegisterPane
from my_pane import MyPane
from my2_pane import My2Pane
from Release_pane import ReleasePane
from PyQt5.Qt import *
from DataBase import *
from PyQt5.QtWidgets import QTableWidgetItem
import time

user_id = None


def show_register_pane():  # 显示注册界面
    register_pane.show()
    Login_pane.close()


def exit_pane():  # 从注册界面退出到登录界面
    Login_pane.show()
    register_pane.close()


def index_to_release():  # 从主页到发布页面
    Release_pane.show()
    Index_pane.close()


def index_to_my():
    show_myobject()
    My_pane.show()
    Index_pane.close()


def release_to_index():
    Index_pane.show()
    Release_pane.close()


def release_to_my():
    show_myobject()
    My_pane.show()
    Release_pane.close()


def my_to_index():
    Index_pane.show()
    My_pane.close()


def my_to_release():
    print("00")
    Release_pane.show()
    My_pane.close()


def my2_to_index():
    Index_pane.show()
    My2_pane.close()


def my2_to_release():
    Release_pane.show()
    My2_pane.close()


def my_to_my2():
    show_my_buy_object()
    My2_pane.show()
    My_pane.close()


def my2_to_my():
    show_myobject()
    My_pane.show()
    My2_pane.close()


def Login(a, b):
    global user_id
    if check_account(a, b):
        user_id = a
        Index_pane.show()
        Login_pane.close()
    else:
        QMessageBox.about(register_pane, "温馨提醒", "该账户不存在 ,请注册")


def check_account(a, b):  # 检测账户是否存在
    flag = False
    for m in user.getuser():
        if a == m[0] and b == m[1]:
            flag = True

    return flag


def register(a, b):  # 注册账户
    if not check_account(a, b):
        user.adduser(a, b)
        QMessageBox.about(register_pane, "温馨提醒", "注册成功,请登录")
    else:
        QMessageBox.about(register_pane, "温馨提醒", "该账户已存在")


def show_object():
    objectinfo = objections.getObjectInfo()

    header = ["名称", "价格", "详情", "发布时间", "卖家ID", "买家ID"]
    try:
        row = len(objectinfo)
        vol = len(objectinfo[0])
    except IndexError:
        Index_pane.tableWidget.setHorizontalHeaderLabels(header)
    else:
        Index_pane.tableWidget.setRowCount(row)
        Index_pane.tableWidget.setColumnCount(vol)
        Index_pane.tableWidget.setHorizontalHeaderLabels(header)
        for i in range(row):
            for z in range(vol):
                temp = objectinfo[i][z]
                data = QTableWidgetItem(str(temp))
                Index_pane.tableWidget.setItem(i, z, data)


def show_myobject():
    global user_id
    header = ["名称", "价格", "详情", "发布时间"]
    my_objectinfo = objections.getMyObject(user_id)
    try:
        row = len(my_objectinfo)
        vol = len(my_objectinfo[0])
    except IndexError:
        My_pane.tableWidget.setHorizontalHeaderLabels(header)
    else:
        if row != 0 and vol != 0:
            My_pane.tableWidget.setRowCount(row)
            My_pane.tableWidget.setColumnCount(vol)
            My_pane.tableWidget.setHorizontalHeaderLabels(header)
            for i in range(row):
                for z in range(vol):
                    temp = my_objectinfo[i][z]
                    data = QTableWidgetItem(str(temp))
                    My_pane.tableWidget.setItem(i, z, data)


def show_my_buy_object():
    global user_id
    header = ["名称", "价格", "详情", "发布时间", "卖家ID"]
    try:
        my_buy_objectinfo = objections.searchbuyObject(user_id)
        row = len(my_buy_objectinfo)
        vol = len(my_buy_objectinfo[0])
    except :
        My2_pane.tableWidget.setHorizontalHeaderLabels(header)
    else:
        if row != 0 and vol != 0:
            My2_pane.tableWidget.setRowCount(row)
            My2_pane.tableWidget.setColumnCount(vol)
            My2_pane.tableWidget.setHorizontalHeaderLabels(header)
            for i in range(row):
                for z in range(vol):
                    temp = my_buy_objectinfo[i][z]
                    data = QTableWidgetItem(str(temp))
                    My2_pane.tableWidget.setItem(i, z, data)


def buy_object(object_name):
    global user_id
    objections.buyObject(object_name, user_id)
    QMessageBox.about(Index_pane, "温馨提醒", "购买成功")


def add_object(name, price, describe):
    global user_id
    PublishTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if objections.check_object(name, user_id) != None:
        objections.addObject(name, price, describe, PublishTime, user_id)
        QMessageBox.about(register_pane, "温馨提醒", "发布成功")
    else:
        QMessageBox.about(register_pane, "温馨提醒", "您已发布过该商品")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    user = UserManager()  # 创建用户数据库对象
    objections = ObjectManager()

    Login_pane = LoginPane()  # 创建登录界面
    register_pane = RegisterPane()  # 创建注册界面
    Index_pane = IndexPane()  # 创建商品显示界面
    Release_pane = ReleasePane()  # 创建发布商品界面
    My_pane = MyPane()  # 创建我的商品界面
    My2_pane = My2Pane()  # 创建历史购买记录的商品界面
    Login_pane.show()  # 显示登录界面

    Login_pane.show_regiser_pane_singal.connect(show_register_pane)  # 点击注册键发射信号
    Login_pane.show_index_pane_singal.connect(lambda a, b: Login(a, b))

    register_pane.exit_signal.connect(exit_pane)
    register_pane.register_account_pwd_signal.connect(lambda a, b: register(a, b))

    Index_pane.show_my_pane_singal.connect(index_to_my)
    Index_pane.show_release_pane_singal.connect(index_to_release)
    Index_pane.search_btn_singal.connect(lambda object_name: buy_object(object_name))

    Release_pane.show_my_pane_singal.connect(release_to_my)
    Release_pane.show_index_pane_singal.connect(release_to_index)
    Release_pane.add_object_singal.connect(lambda a, b, c: add_object(a, b, c))

    My_pane.show_index_pane_singal.connect(my_to_index)
    My_pane.show_release_pane_singal.connect(my_to_release)
    My_pane.show_my2_pane_singal.connect(my_to_my2)

    My2_pane.show_index_pane_singal.connect(my2_to_index)
    My2_pane.show_release_pane_singal.connect(my2_to_release)
    My2_pane.show_upmy_pane_singal.connect(my2_to_my)

    show_object()
    sys.exit(app.exec_())
