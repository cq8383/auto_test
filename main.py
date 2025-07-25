import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s','-q','./testcase/test_bookingform.py','--clean-alluredir','--alluredir=./report'])
    os.system('allure generate ./report -o ./allure --clean')

