import requests
import pytest

def test_00(tokens):
    # 获取token
    tokens.set('sysadmin', 'admin')
    # tokens.set('zhangsan', 'zhangsan')
    # tokens.set(username='lishi', password='lisi')

def test_01(requests_session, tokens):
    # 设置全局请求对象头的令牌
    requests_session.headers.update({'access_token': tokens.get('sysadmin')})


def test_A001(requests_session, base_url):
    # sysadmin分页查询用户，令牌一直有效
    url = base_url + '/api-sys/sys/user/queryUserForPage'
    data = {
        "page": 1,
        "size": 15
    }
    r = requests_session.post(url, json=data)
    assert r.status_code == 200
    response_data = r.json()
    assert response_data['code'] == 200


def test_A002(requests_no_session, tokens, base_url):
    # 非sysadmin分页查询用户，查询后该用户令牌失效
    url = base_url + '/api-sys/sys/user/queryUserForPage'
    data = {
        "page": 1,
        "size": 15
    }
    requests_no_session.headers.update({'access_token': tokens.get('zhangsan')})
    r = requests_no_session.post(url, json=data)
    assert r.status_code == 200
    response_data = r.json()
    assert response_data['code'] == 200


def test_A003(requests_session, base_url):
    # 从缓存中获取字典键值对，延用sysadmin令牌
    url = base_url + '/api-sys/sys/dict/cache'
    data = {
        "typeId": "dm_mpping_type"
    }
    r = requests_session.post(url, json=data)
    assert r.status_code == 200


def test_A004(requests_no_session, base_url):
    # 从缓存中获取字典键值对，用户未登录报错
    url = base_url + '/api-sys/sys/dict/cache'
    data = {
        "typeId": "dm_mpping_type"
    }
    r = requests_no_session.post(url, json=data)
    assert r.status_code == 401


def test_A005(connect):
    #数据库比较
    with connect.get('sys-center').cursor() as cursor:
        cursor.execute('select * from t_vmf_sys_user where user_name="sysadmin"')
        result = cursor.fetchone()

        assert result['USER_NAME'] == 'sysadmin'
        assert result['USER_TYPE'] == '1'


if __name__ == "__main__":
    pytest.main(["-s", "test_a.py"])
