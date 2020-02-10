import requests
from bs4 import BeautifulSoup
import bs4
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def getHTMLText(url):  # 返回html页面内容
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):  # 将html页面内容返回到list列表中
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 过滤掉非标签类型数据
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[4].string])


def printUnivList(ulist, num):  # 将列表中内容打印出来
    fileobject = open('grade.txt', 'w', encoding='utf-8')
    fileobject.write("{:^10}\t{:8}\t{:^15}".format("排名", "学校名称", "总分"))
    fileobject.write('\n')
    list_name = []
    list_score = []
    for i in range(num):
        list_name.append(ulist[i][1])
        list_score.append(ulist[i][2])
        u = ulist[i]
        fileobject.write("{:^10}\t{:8}\t{:^15}".format(u[0], u[1], u[2]))
        fileobject.write('\n')

    fileobject.close()
    list_name.reverse()
    list_score.reverse()
    x_major_locator = MultipleLocator(1.5)
    y_major_locator = MultipleLocator(2)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.plot(list_name, list_score)
    plt.show()


def show(ulist, num):
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:8}\t{:^15}".format(u[0], u[1], u[2]))
        fileobject.write("{:^10}\t{:8}\t{:^15}".format(u[0], u[1], u[2]))
        fileobject.write('\n')
    fileobject.close()

    x = ulist[0][1]
    x = np.linspace(ulist[0][1], ulist[9][1], 10)
    y = 10
    # 第一个是横坐标的值，第二个是纵坐标的值


if __name__ == "__main__":
    uinfo = []
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10)  # 5 univ