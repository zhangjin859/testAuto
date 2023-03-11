import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate  ./report -o ./report/html  --clean")