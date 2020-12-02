import pytest
import requests
import allure


# def test_01(apijson):
#     apijson.getSwag()
@allure.feature("测试")
def test_00(tokens):
    tokens.setToken('sysadmin', 'admin')
  

def test_02(adminHeader,toknes):
    adminHeader.headers.update({'access_token': tokens.get('sysadmin')})

def test_03(ordinaryHeader,tokens):
    ordinaryHeader.headers.update({'access_token': tokens.get('zhangsan')})

def test_04(adminHeader,apijson):
    json = apijson.getSwag()#.items()
    for key, value in json:
        url = key
        if not 'post' in self._data.keys():
            data = value['get']['parameters']
            requests_session.get(url, json=data)
        else:
            data = value['post']['parameters']
            requests_session.post(url, json=data)
    
def test_A003(requests_session, base_url):
    # 从缓存中获取字典键值对，延用sysadmin令牌
    url = base_url + '[paths]'
    data = {
        "typeId": "dm_mpping_type"
    }
    r = requests_session.post(url, json=data)
    assert r.status_code == 200


def test_tt(tokens):
    _case = [
        {
            'name': '修改当前登录用户的密码',
            'data': {
                'jsonObject': 1
            }
        },
        {
            'name': 'token获取当前登录用户',
            'data': {}
        },
        {
            'name': '分页查询',
            'data': {
                'orderby': 1,
                'order': 2
            }
        }
    ]
    path = [
        {
            name: '修改当前登录用户的密码',
            url: '',
            paraments: {},
            respons:{}
        },
        {
            name: '修改当前登录用户的密码',
            url: '',
            paraments: {},
            respons:{}
        }
    ]
    json = apijson.getSwag()
    for key, value in json:
        url = key
        if not 'post' in self._data.keys():
            data = value['get']['parameters']
            requests_session.get(url, json=data)
        else:
            data = value['post']['parameters']
            requests_session.post(url, json=data)






if __name__ == "__main__":
    pytest.main(["-s", "test_case.py"])