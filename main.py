# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pytest
import os
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 生成JSON数据,加上--clean-alluredir解决JSON文件生成冗余问题
pytest.main(["-s", "--alluredir=report", "--clean-alluredir"])
# 命令：pytest -v -s --alluredir=report --clean-alluredir

# 将JSON文件转换成HTML格式的测试报告（生成JSON文件路径：report; 生成HTML报告路径：report/html）
os.system("allure generate --clean ./report -o ./report/html")
# 命令：allure generate outputs/reports/allure -o outputs/reports/html --clean
# 打开测试报告
os.system("allure serve ./report")
# 命令：allure serve ./report


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
