import pytest


class TestData:

    @pytest.mark.parametrize('args', ["测试", "12", "java", "34"])
    def test_data(self, args):
        print(args)




if __name__ == '__main__':
     pytest.main(["-vs", "dataDriver.py"])