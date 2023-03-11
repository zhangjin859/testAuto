import json
import logging
import re

import jsonpath
import requests

from common.yaml_util import YamlUtil
from debug_talk import DebugTalk


class SendUtil:
    session = requests.Session()

    # # 初始化时，就获得项目名称，和环境名称
    # def __init__(self, team, workspace):
    #     self.base_url = YamlUtil.read_configyaml(team, workspace)
    #     self.headers_dict = {}
    # 先生成字符串格式，替换URL中的{{}}，然后返回原有格式的URL
    # @classmethod
    # def replace_value(cls, data):
    #     if data and isinstance(data, dict):
    #         value = json.dumps(data)
    #     else:
    #         value = data
    #     for item in range(0, value.count("{{")):
    #         if "{{" in value and "}}" in value:
    #             start_index = value.index("{{")
    #             end_index = value.index("}}")
    #             old_value = value[start_index:end_index + 2]
    #             new_value = YamlUtil.read_extract(old_value[2:-2])
    #             # replace方法只能传字符串，如果是数值，需要转换
    #             if type(new_value) == int:
    #                 new_value = str(new_value)
    #             value = value.replace(old_value, new_value)
    #     # 如果不先生成字符串格式，无法进行替换，替换了之后，需要把数据还原成字典格式
    #     if value and isinstance(data, dict):
    #         new_data = json.loads(value)
    #     else:
    #         new_data = value
    #     return new_data

    # 根据数据文件的绝对路径，在调用时，拼接上具体的模块名，即可完成接口拼接
    def send(self, method, url, headers, **kwargs):
        # 获取{{param}}参数，替换为关联参数
        # url = self.base_url + SendUtil.replace_load(url)
        # 替换请求头
        headers_dict = {}
        # if headers:
        #     # if "${" in value and "}" in value:
        #     # 取token的value
        #     headers_value = SendUtil.replace_load(headers)
        #     # 取key，拼接成字典格式
        #     headers_key = headers[2: -2]
        #     headers_dict = {headers_key: headers_value}
        # 替换请求数据
        for key, value in kwargs.items():
            if key in ['params', 'data', 'json']:
                kwargs[key] = self.replace_load(value)
            elif key == "files":
                for file_key, file_path in value.items():
                    value[file_key] = open(file_path, 'rb')
        method = str(method).lower()
        # 多参数可以传入data，json，cookie等
        res = self.session.request(method=method, url=url, headers=headers, **kwargs)
        # print(f"当前环境是：{YamlUtil.now_workspace}:{url}")
        return res

        # yaml测试用例规则约束

    def analysis_yaml(self, case):
        # 获取yaml用例的所有键
        resp = None
        case_key = case.keys()
        # 判断必填的键是否存在
        if 'name' in case_key and 'request' in case_key and 'validate' in case_key:
            request_key = dict(case['request']).keys()
            # 判断request中的method和url是否存在
            if 'method' in request_key and 'url' in request_key:
                # # 获取method和url
                # method = case['request']['method']
                # url = case['request']['url']
                # 从列表中移除method和url和headers，因为要把可变长度的参数传给send方法的**kwargs
                # del case['request']['method']
                method = case['request'].pop("method")  # pop() 函数用于移除列表中的一个元素，并且返回该元素的值
                url = case['request'].pop("url")
                # del case['request']['url']
                headers = None
                # 通过jsonpath判断是否存在请求头
                if jsonpath.jsonpath(case, '$.request.headers'):
                    headers_value = case['request']['headers']
                    # 从列表中移除method和url和headers，因为要把可变长度的参数传给send方法的**kwargs
                    # del case['request']['headers']
                    headers = self.replace_load(headers_value)
                    headers = case['request'].pop("headers")
                resp = self.send(method=method, url=url, headers=headers, **case['request'])
                try:
                    res_data = resp.json()
                except Exception as e:
                    logging.error("接口返回的结果出错：{}".format(e))
                if case['validate'] is not None:
                    self.validate_result(resp.json(), case['validate'])
                elif case['validate'] is None:
                    logging.info("断言为空")
                # //jsonpath.jsonpath(res_data,"$.data.token")
                # res_text = resp.text
                if jsonpath.jsonpath(case, '$.extract'):
                    for key, value in dict(case['extract']).items():
                        # 通过正则表达式提取token
                        if '(.+?)' in value or '(*.?)' in value:
                            re_value = re.search(value, str(res_data))
                            if re_value:
                                extract_data = {key: re_value.group(1)}
                                YamlUtil.write_yaml(self, extract_data)
                        # 通过jsonpath表达式提取token
                        else:
                            js_value = jsonpath.jsonpath(res_data, value)
                            if js_value:
                                extract_data = {key: js_value}
                                print(extract_data)
                                YamlUtil.write_yaml(self, extract_data)


            else:
                print("request必填项不能为空")
        else:
            print("yaml用例必填项不能为空")
        return resp

    # 热加载替换方式
    @classmethod
    def replace_load(cls, data):
        if data and isinstance(data, dict):
            value = json.dumps(data, ensure_ascii=False)
        else:
            value = data
        for item in range(0, value.count("${")):
            if "${" in value and "}" in value:
                start_index = value.index("${")
                end_index = value.index("}")
                old_value = value[start_index:end_index + 1]
                # 获取yaml文件中的方法名
                function_name = old_value[2: old_value.index('(')]
                # 获取yaml文件中的参数
                args_value = old_value[old_value.index('(') + 1: old_value.index(')')]
                # 将参数分割，变成单个个体
                args_value_list = args_value.split(',')
                # 通过反射方法，去获取新的值
                new_value = getattr(DebugTalk(), function_name)(*args_value_list)
                print("new_value", new_value)
                # 得到新的值，replace只能传字符串，需要强转
                value = value.replace(old_value, str(new_value))
        # 如果不先生成字符串格式，无法进行替换，替换了之后，需要把数据还原成字典格式
        if data and isinstance(data, dict):
            data = json.loads(value)
        else:
            data = value
        return data

    # 断言封装
    def validate_result(self, result, expect):
        for i in expect:
            if "eq" in i.keys():
                yaml_result = i.get("eq")[0]
                actual_result = jsonpath.jsonpath(result, yaml_result)
                expect_result = i.get("eq")[1]
                assert actual_result[0] == expect_result
                logging.info("期望值:{} 实际值：{}".format(expect_result, actual_result[0]))



if __name__ == '__main__':
    expect = [{'eq': ['$.code', 200]}, {'eq': ['$.data.sex', 'man']}]
    for i in expect:
        print(i.keys())
        print(i.get("eq")[0])
