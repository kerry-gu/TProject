import pytest
import requests

# def test_01(apijson):
#     apijson.getSwag()

def test_00(tokens):
    p = tokens.setToken('sysadmin', 'admin')
    print('1------------------')
    print(p)
    print('2------------------')

def test_02()





if __name__ == "__main__":
    pytest.main(["-s", "test_case.py"])