#conftest.py
import pytest
from self import self

from common.yaml_util import YamlUtil


#request.config.rootdir属性，这个属性表示的是pytest.ini这个配置文件所在的目录
#注意：当根目录下没有pytest.ini配置文件时，会默认指向conftest.py所在目录；此时要指向项目根目录，则在项目目录下新建一个 pytest.ini 空文件即可


#conftest.py文件中的函数只在conftest.py所在目录及其子目录中的测试活动生效
# @pytest.fixture 相当于setup teardown 默认作用域是方法。在测试方法执行前执行
@pytest.fixture(scope="session", autouse="True")
def fixture_for_func():
    print('连接数据库')
    yield
    YamlUtil.clean_yaml(self)
    print('关闭数据库')
