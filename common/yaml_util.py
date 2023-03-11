import os
import yaml

class YamlUtil:
    # 获取当前文件的目录
    cur_path = os.path.abspath(os.path.dirname(__file__))
    print(cur_path)

    # 获取根目录
    root_path = cur_path[:cur_path.find("Project\\") + len("Project\\")]
    print(root_path)

    # 读取   yaml.load 把json转为字典格式
    def read_yaml(self, yaml_path):
        with open(YamlUtil.root_path + yaml_path, encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            # data = {'Authorization': value['Authorization']}
            # return data
            print(value)
            return value

    # 读取  写入token的extract.ymal文件中的token值
    def read_extractYaml(self):
        with open(YamlUtil.root_path + "/extract.yaml", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            # data = {'Authorization': value['Authorization']}
            # return data
            print(type(value))
            return value['token']
    # 写入 yaml.dump 把字典格式转为json
    def write_yaml(self, data):
        with open(YamlUtil.root_path + "/extract.yaml", encoding="utf-8", mode="a") as f:
            dump = yaml.dump(data, stream=f, allow_unicode=True)
            return dump

    # 清空
    def clean_yaml(self):
        with open(YamlUtil.root_path + "/extract.yaml", encoding="utf-8", mode="w") as f:
            f.truncate()

