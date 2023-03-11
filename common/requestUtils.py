
import requests
import logging

class RequestUtil:

    def __init__(self):
        """

        session管理器
        requests.session(): 维持会话,跨请求的时候保存参数
        """
        # 实例化session
        self.session = requests.session()

    # # 规范YAML测试用例
    def send_request(self, caseinfo):
        try:
            cs_request = caseinfo['request']
            method_ = cs_request['method']
            method = str(method_).lower()
            url = cs_request['url']
            data = cs_request['params']
            res = self.session.request(method, url, json=data)
        except Exception as e:
         logging.error("请求失败原因:{}".format(e))
        return res




