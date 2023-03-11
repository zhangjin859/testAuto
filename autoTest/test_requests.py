# fixture使用案例scope="function"
import json

import allure
import pytest
import logging, re, jsonpath

import self as self

from common.SendUtil import SendUtil
from common.yaml_util import YamlUtil

@allure.epic("项目名称：若依管理系统")
@allure.feature("模块名称：登录模块 测试类Test01")
class Test01:
    @pytest.mark.run(order=-3)
    @pytest.mark.smoke
    @allure.story("获取方法test_get_token1")
    @allure.step("测试步骤")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("caseinfo", YamlUtil.read_yaml(self, '/autoTest/extract.yaml'))
    def test_get_token1(self, caseinfo):
        result = SendUtil().analysis_yaml(caseinfo)
        # result1 = jsonpath.jsonpath(result.json(), "$.data.sex")
        logging.info(result.json())
        # logging.info("jjjj:{}".format(result1))
       #
       # // assert result.json()[]
       #  print(result.content)
       #  result = jsonpath.jsonpath(result.json(), "$.sex")
       #  logging.info("模糊匹配到的值为:{}".format(result))
       #  读取数据后写入token
       #  YamlUtil.write_yaml(self, data={"Authorization": 1})
       #
       #  yaml = YamlUtil.read_yaml(self, '/extract.yaml')
       #
       #  result_text__group = re.search('title="(.*?)"', result.text).group(1)
       #  logging.info("匹配到的值为:{}".format(result_text__group))

    # @pytest.mark.token
    # @pytest.mark.run(order=-1)
    # def demo(self):
    #      print(1111)
    #
    # @pytest.mark.run(order=-2)
    # # @pytest.mark.skip("条件错误")
    # def test_get_token3(self):
    #     try:
    #         YamlUtil.write_yaml(self, {"id": 22})
    #     except Exception as e:
    #         print(e)

