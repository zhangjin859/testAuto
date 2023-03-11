import os
import time

import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# 测试之前的环境准备--连接浏览器并打开目标页面
def setup_module():
    global webdriver_chrome
    chromedriver_autoinstaller.install()
    # import os  解决自动更新chrom驱动问题，
    # # to use when 1st time on the machine and then leave comented
    # os.system("pip install  selenium ")
    # os.system("pip install  chromedriver_autoinstaller ")
    options = webdriver.ChromeOptions()
    options.headless = False
    # 防止浏览器关闭
    options.add_experimental_option("detach", True)
    webdriver_chrome = webdriver.Chrome(options=options)
    webdriver_chrome.get("https://www.huawei.com/cn/?ic_medium=direct&ic_source=surlent")
    webdriver_chrome.maximize_window()
    print("setup")
# 测试之后的环境清除--关闭浏览器
def teardown_module():
    print("clear")
    global webdriver_chrome
    webdriver_chrome.quit()


# 测试用例名必需是test_或则_test开头的
def test_huawei():

    items = webdriver_chrome.find_element(By.XPATH, '//*[@id="hw-navbar"]/ul').text
    split = items.split("\n")
    item = []
    for result in split:
        item.append(result)
    assert item == ['个人及家庭产品', '商用产品及方案', '服务支持', '合作伙伴与开发者', '关于华为']
    print("111111")
def test_xiaomi():
    print("test xiaomi")

if __name__ == '__main__':
     # -s 是输出打印的内容  D:\tool\python\pycharm\pythonProject\test1.py
     #  pytest.main(["test1.py", "-s", "--alluredir=report", "--clean-alluredir"])
     # 在pytest.ini文件中配置生成报告的命令 addopts = -vs --alluredir ./report --clean-alluredir
      pytest.main(["test1.py"])
     # 这一步是生产html文档，并可以通过点击index.html在浏览器访问报告
     # os.system('allure generate --clean ./report -o ./report/html/')
     # 自动打开生成的报告
      os.system('allure serve ./report')
