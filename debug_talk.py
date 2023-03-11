import random

from self import self

from common.yaml_util import YamlUtil


class DebugTalk:

    # 热加载获取随机数方法
    @classmethod
    def get_random_number(cls, min_num, max_num):
        number = random.randint(int(min_num), int(max_num))
        return number

    # 热加载获取随机名称
    @classmethod
    def get_random_name(cls, min_num, max_num):
        num = random.randint(int(min_num), int(max_num))
        name = str(num) + "测试岗位"
        return name

    # 热加载获取token或者其他关联参数
    #读取extract.yaml文件中的值
    @classmethod
    def get_extract_data(cls, params):
        return YamlUtil.read_extractYaml(self)



