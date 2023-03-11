"""

total = input('请输入一个数值:')
print('用户输入的数值是:', total+'10', 'hi:\nboy')

print('整数%d' % 2)
print('小数%.1f' % 2.5)
print('字符串%s' % 'zii')
print('小数%.1f%%' % 2.5)

print('{:.2}'.format(2.125))
print('{1},{0}'.format(1, 2))
print("我叫{}今年{}岁!".format('小明', 10))

import keyword
import math
import random
a = [1, 2, 8]
random.shuffle(a)
print(a)
print(math.ceil(4.5))
print(keyword.kwlist)

import math

s = '你好 我是 python'
# print(s[-6:1:-2])
s1 = ['你好', '我是', 'python']
print(s.split(" "))
print(','.join(s1))
print(s.find('t'))
s = '     你好 我是 python   '
s1 = s.strip()
print(s1)


lis = ['你好', '我是', 'python']
print(''.join(lis))
lis1 = ['你好1', 5, 'python1']
s = '你好我是python'
print(list(s))
print(s.split())
lis[0] = 'jj'
del lis1[0]
lis1.clear()
print(list(range(10)))


lis = ['你好', '我是', 'python']
join = "".join(lis)
print(join)

# 字典
s = (1, 2, 3)
d = dict.fromkeys(s, 10)
print(d)
get = d.get(1)
print(get)

seq = ('name', 'age', 'sex')

tinydic = dict.fromkeys(seq)
items = tinydic.items()
l = list(items)

print(l)
for k, v in items:
    print(k, ":", v)

print(items)
print("新的字典为 : %s" % tinydic)
print("新的字典为:{}".format(tinydic))
# 同时使用元组和字典传参 元组只能用数值或者空格代替，不能用关键字（skill）写
# 多种混合使用的时候。位置参数要在关键字参数前面，元组要在字典前面
name = ["卡卡罗特", "界王拳"]
names = {"nickname": "孙君", "skill": "元气弹"}
print(names.items())
print("我是{0},我的绝招是{skill}".format(*name, **names))
print("我是{nickname},我的绝招是{1}".format(*name, **names))

import os
import shutil
import sys

# -*- coding: utf-8 -*-
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gbk")

# f = open("D:\\test.txt", 'r', encoding='utf-8')
# readline = f.readlines()
# print(readline)
# # for at in readline:
# #     print(at)
# f.close()
# shutil.rmtree('D:\\test')
# os.mkdir("D:\\test")
if not os.path.exists("D:\\test"):
    os.makedirs("D:\\test")
t = open("D:\\test\\test.txt", mode='w')
t.close()

# os.mknod("D:\\test\\test1.txt")

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
items = params.items()
join = ','.join(items)
print(join)

x = True
y = False
z = False

if not x or y:          #false
    print(1)
elif not x or not y and z:   #fasle
    print(2)
elif not x or y or not y and x: # true
    print(3)
else:
    print(4)

for char in 'PYTHON STRING':
    if char == ' ':
        break

    print(char, end='')

    if char == '0':
        continue




import pymysql as pymysql

pymysql.connect(host="localhost", user="root", password="123456", database="mysql", port=3306,
                          charset="utf8mb4")
"""
import os
import re
import requests
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import get_browser_version_from_os

# id 定位元素
# chrome = webdriver.Chrome()
# chrome.get("https://www.taobao.com/")
# chrome.find_element("id", "q")
# chrome.find_element("id", "q").clear()
# chrome.find_element("id", "q").send_keys("男鞋")
# time.sleep(5)
# chrome.close()

# name 定位元素
# chrome = webdriver.Chrome()
# chrome.get("https://www.taobao.com/")
# chrome.find_element("name", "q")
# chrome.find_element("name", "q").clear()
# chrome.find_element("name", "q").send_keys("男袜")
# # 如有相同的name属性 find_element默认选中第一个
# # find_elements 方法返回的是一个list 可以用下标进行选取 eg：chrome.find_element("name", "q").[1].click()
# time.sleep(5)
# chrome.close()

# class 定位元素
# chrome = webdriver.Chrome()
# chrome.get("https://www.taobao.com/")
# chrome.find_element("class", "q")
# chrome.find_element("class", "q").clear()
# chrome.find_element("class", "q").send_keys("男袜")
# # 如果class 是符合样式 不能用这个属性 eg： （class", "ree hh"）
# time.sleep(5)
# chrome.close()

# tag name 定位元素 一般用于寻找同类的元素进行批量操作 eg： input textarea(批量输入参数) 用find_elements()方法
# chrome = webdriver.Chrome()
# chrome.get("https://www.taobao.com/")
# element = chrome.find_elements("tag name", "input")
# # 查看多少个input 标签
# print(len(element))
# chrome.find_element("tag name", "input").clear()
# chrome.find_element("tag name", "input").send_keys("男鞋")
# time.sleep(5)
# chrome.close()

# link text<a>需要完整写入名称  partial link text<a>模糊查询 不需要完整写入 定位元素 超链接元素
# chrome = webdriver.Chrome()
# chrome.get("https://www.baidu.com/")
# time.sleep(5)
# chrome.find_element('link text', "新闻").click()
# time.sleep(5)
# chrome.close()

# xpath
# chrome = webdriver.Chrome()
# chrome.get("https://www.baidu.com/")
# time.sleep(5)
# 1根据路径进行匹配
# chrome.find_element('xpath', '//*[@id="s-top-left"]/a[text()="新闻"]').click()
# 2根据属性进行定位
# chrome.find_element('xpath', '//span[@class="hot-refresh-text"]').click()
# 3模糊进行定位
# chrome.find_element('xpath', '//*[contains(@class,"hot-refresh-text")]').click()
# time.sleep(5)
# chrome.close()

# baidu 登录操作
# chrome = webdriver.Chrome()
# chrome.get("https://www.baidu.com/")
# chrome.maximize_window()
# # 全局等待时间10s 最大10s
# chrome.implicitly_wait(10)
# chrome.find_element("xpath", '//*[@id="s-top-loginbtn"]').click()
# chrome.find_element("xpath", '//*[contains(@placeholder, "手机号/用户名/邮箱")]').send_keys("18326133107")
# # # 获取输入框的值
# attribute = chrome.find_element("xpath", '//*[contains(@placeholder, "手机号/用户名/邮箱")]').get_attribute("value")
# print(attribute)
# chrome.find_element("xpath", '//*[contains(@placeholder, "密码")]').send_keys("zhangjin940211ll")
# # # chrome.find_element("xpath", '//*[@id="TANGRAM__PSP_11__submit"]').click()
# chrome.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
# # time.sleep(5)
# # 显示等待  EC()方法里是一个元组所以用（）
# WebDriverWait(chrome, 5).until(EC.presence_of_element_located(("id", "TANGRAM__PSP_11__error"), "用户名错误"))
# text = chrome.find_element(By.ID, 'TANGRAM__PSP_11__error').text
# print(text)
# time.sleep(5)
# chromedriver_autoinstaller.install()
# # import os  解决自动更新chrom驱动问题，
# # # to use when 1st time on the machine and then leave comented
# # os.system("pip install  selenium ")
# # os.system("pip install  chromedriver_autoinstaller ")

browserVersion=get_browser_version_from_os("google-chrome") # 获取当前系统chrome浏览器的版本号
mainBrowserVersion=browserVersion.split(".")[0] # 获取浏览器的主版本号
resp=requests.get(url="https://chromedriver.storage.googleapis.com/")
content=resp.text
availableVersionList=re.search(f"<Contents><Key>({mainBrowserVersion}\.\d+\.\d+\.\d+)/chromedriver_win32\.zip</Key>.*?",content,re.S)
if availableVersionList==None:
    print(f"镜像网站上没有找到主版本号为{mainBrowserVersion}的chromedriver文件，请核实！")
    time.sleep(10)
    os._exit(0)
else:
    availableVersion=availableVersionList.group(1)
    driver_path=ChromeDriverManager(version=availableVersion).install()
    print(driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.headless = False
# webdriver_chrome = webdriver.Chrome(options=options)
webdriver_chrome = webdriver.Chrome(service=Service(driver_path), options=options)



def fun1():
    webdriver_chrome.get("https://sso.ahzwfw.gov.cn/uccp-server/login")
    webdriver_chrome.maximize_window()
    webdriver_chrome.find_element(By.ID, "perName").send_keys("Adffghhh")
    webdriver_chrome.find_element(By.ID, "psdBtn").click()
    # 显示等待可以控制时间，不需要等待5s，而强制等待需要等完5s
    WebDriverWait(webdriver_chrome, 5).until(
        EC.text_to_be_present_in_element(('xpath', '//*[@id="userLogin"]/li[3]/div'), '请输入密码'))
    text = webdriver_chrome.find_element(By.XPATH, '//*[@id="userLogin"]/li[3]/div').text
    print(text)

def fun3():
    # frame 上下文切换操作，
    webdriver_chrome.get("https://sso.ahzwfw.gov.cn/uccp-user/resources/register/register?appCode=&source=&callback=&serviceUrl=")
    webdriver_chrome.maximize_window()
    time.sleep(3)
    # 显示等待可以控制时间，不需要等待5s，而强制等待需要等完5s
    # WebDriverWait(webdriver_chrome, 5).until(
    #     EC.element_to_be_clickable(('id', 'psdBtn')))
    # webdriver_chrome.find_element(By.ID, "psdBtn").click()
    # 下拉框操作  Select only works on <select> elements, not on other things eg：下面的就是在span elements上
    #Select(webdriver_chrome.find_element(By.CLASS_NAME, 'select')).select_by_visible_text("护照")
    # 另一种下拉框 非select
    selectBox = WebDriverWait(webdriver_chrome, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form2"]/div/div[1]/div/div/span')))
    action = ActionChains(webdriver_chrome)  # 鼠标移动到指定位置进行点击
    action.move_to_element(selectBox).perform()
    selectBox.click()
    until = WebDriverWait(webdriver_chrome, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="credentType_listbox"]/li[2]')))
    action = ActionChains(webdriver_chrome)
    action.move_to_element(until).perform()
    until.click()
    webdriver_chrome.execute_script("window.scrollTo(0,300)")

def fun4():
    webdriver_chrome.get("https://mail.qq.com/")
    webdriver_chrome.maximize_window()
    # 登录输入框页面是一个子页面被包含在主页中
    webdriver_chrome.switch_to.frame(webdriver_chrome.find_element("id", "login_frame"))
    webdriver_chrome.find_element(By.ID, "u").send_keys("1150531814")
    webdriver_chrome.find_element(By.ID, "p").send_keys("zhangalong940211")
    time.sleep(10)
    # 回到主页面
    webdriver_chrome.switch_to.default_content()
    webdriver_chrome.find_element(By.PARTIAL_LINK_TEXT, "基本版").click()

    # 多个页面窗口进行操作   打开百度
    # webdriver_chrome.get('http://www.baidu.com')
    # # 新建一个选项卡
    # webdriver_chrome.execute_script('window.open()')
    # print(webdriver_chrome.window_handles)
    # # 跳转到第二个选项卡并打开知乎
    # webdriver_chrome.switch_to.window(webdriver_chrome.window_handles[1])
    # webdriver_chrome.get('http://www.zhihu.com')
    # # 回到第一个选项卡并打开淘宝（原来的百度页面改为了淘宝）
    # time.sleep(2)
    # webdriver_chrome.switch_to.window(webdriver_chrome.window_handles[0])
    # webdriver_chrome.get('http://www.taobao.com')

    # 显示等待可以控制时间，不需要等待5s，而强制等待需要等完5s
    # WebDriverWait(webdriver_chrome, 5).until(
    #     EC.text_to_be_present_in_element(('xpath', '//*[@id="userLogin"]/li[3]/div'), '请输入密码'))
    # text = webdriver_chrome.find_element(By.XPATH, '//*[@id="userLogin"]/li[3]/div').text
    # print(text)

def fun5():
        webdriver_chrome.get("https://www.huawei.com/cn/?ic_medium=direct&ic_source=surlent")
        webdriver_chrome.maximize_window()
        items = webdriver_chrome.find_element(By.XPATH, '//*[@id="hw-navbar"]/ul').text
        print(items)
        split = items.split("\n")
        print(split[1])
        item = []
        for result in split:
                item.append(result)
        print(item)
        assert item == ['个人及家庭产品', '商用产品及方案', '服务支持', '合作伙伴与开发者', '关于华为']
def fun6():
    webdriver_chrome.get(r"D:\tool\python\pycharm\pythonProject\file.html")
    webdriver_chrome.maximize_window()
    # time.sleep(20)

if __name__ == '__main__':
    fun5()
# webdriver的常用8种定位方式
# id， name， class name ，tag name , link text<a> , partial link xt<ate>,xpath ,css select
