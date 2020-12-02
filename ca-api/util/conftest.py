import requests as rq
import json
import pytest

class ReqSwag:
    _apijson={}
    
    def getSwag(self):
        self.header ={
            'client_id': 'webApp',
            'client_secret': 'webApp',
            'Content-Type': 'application/json'
            }
        self.url = "http://192.168.6.86:7001/v2/api-docs"
        with rq.session as s:
            s.header.update(self.header)
            _json = s.get(url = self.url,headers=self.header)
            _json = _json.json()
            self._apijson=_json
            return _json
            
    # 获取接口文档方法  /index/queryUserMenu
    def getJson(pathname):
        return self._apijson['paths'][pathname]
# 全局变量接口文档类
@pytest.fixture(scope='session')
def apijson():
    yield ReqSwag


# 获取token
BASE_URL = 'http://192.168.6.86:9200'
class GetToken:
    _data = {}

    def getToken(self, username, password):
        self.header = {
            "client_id": "webApp",
            "client_secret": "webApp",
            "Content-Type": "application/json"
            }
        self.url = "http://192.168.6.86:9200/api-auth/oauth/user/token"
        self.data = {
            'username': username,
            'password': password,
            }
        with rq.session() as s:
            s.headers.update(self.header)
            _token = s.post(url=self.url, headers=self.header, json=self.data)
            a = _token.json()
            self._data[username] = a['data']['access_token']
            return self._data[username]
# 获取token
    def get(self,username):
        return self._data[username]
# 全局变量
@pytest.fixture(scope = 'session')
def tokens():
    yield GetToken()
# 全局管理员token
@pytest.fixture(scope = 'session')
def adminHeader():
    with rq.session as session:
        session.headers.update({
            'Content-Type': 'application/json'
        })
    yield session
# 全局普通用户token
@pytest.fixture(scope = 'session')
def ordinaryHeader():
    with rq.session as session:
        session.headers.update({
            'Content-Type': 'application/json'
            })
    yield session
# url全局
@pytest.fixture(scope='session')
def base_url():
    return BASE_URL


# a=GetToken()
# print(a.getToken('sysadmin','admin'))

