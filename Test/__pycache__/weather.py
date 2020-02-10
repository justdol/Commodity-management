# -*- coding:utf-8 -*-
# 天气脚本
import json
import re
import urllib as urlparse
import http.client
import requests
from lxml import etree

target_url = 'https://www.ip.cn/'
municipality = ['北京市','上海市','重庆市','天津市']

def download_page(url):
    """
    获取网页源代码
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    html = requests.get(url, headers=headers)
    # print(html.text)
    return html.text

def get_city_name(html):
    """
    对网页内容进行解析并分析得到需要的数据
    """
    selector = etree.HTML(html)     # 将源码转换为能被XPath匹配的格式
    _info = selector.xpath('//script')[1].text                   # 由于网页采用动态加载，“所在的地理位置”跑到了<script>中
    location = re.findall(r"<code>(.*?)</code>", _info)[1]        #使用正则表达式获取地理位置信息，在<code></code>标签中
    location = location.split(" ")[0]
    if location in municipality:
        city = location[:-1]        # 直辖市的话不取'市'，不然天气结果会不准
    else:
        for i, char in enumerate(location):
            if char == "区" or char == "省":
                index = i + 1
                break
        city = location[index:-1]       # 取'省'后面一直到'市'中间的城市名称用作天气搜索
    return city

def get_city_code(city='合肥'):
    """
    输入一个城市，返回在中国天气网上城市所对应的code
    """
    try:
        parameter = urlparse.parse.urlencode({'cityname': city})
        conn = http.client.HTTPConnection('toy1.weather.com.cn', 80, timeout=5)
        conn.request('GET', '/search?' + parameter)
        r = conn.getresponse()
        data = r.read().decode()[1:-1]
        json_data = json.loads(data)
        code = json_data[0]['ref'].split('~')[0]        # 返回城市编码
        return code
    except Exception as e:
        raise e

def get_city_weather(city_code):
    """
    通过城市编码找到天气信息
    """
    try:
        url = 'http://www.weather.com.cn/weather1dn/' + city_code + '.shtml'
        headers = { "Referer": url }
        conn = http.client.HTTPConnection('d1.weather.com.cn', 80, timeout=5)
        conn.request('GET', '/sk_2d/' + city_code + '.html', headers=headers)
        r = conn.getresponse()
        data = r.read().decode()[13:]
        weather_info = json.loads(data)
        return weather_info
    except Exception as e:
        raise e

if __name__ == '__main__':
    city = get_city_name(download_page(target_url))
    city_code = get_city_code(city)
    city_wether = get_city_weather(city_code)
    print(city_wether)