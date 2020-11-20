import requests as rq
import json
import pytest

class ReqSwag:

    def test_header(self):
        self.header ={
            'client_id': 'webApp',
            'client_secret': 'webApp',
            'Content-Type': 'application/json'
            }
        self.url = "http://192.168.6.86:7001/v2/api-docs"

    def getSwag(self):
        _json = rq.get(self.url,self.header)
        a = _json.json()
        return a
@pytest.fixture(scope='session')
def apijson():
    yield ReqSwag


class GetToken:
    _data = {}

    def setToken(self, username, password):
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
            self._data = a['data']['access_token']
            return self._data

@pytest.fixture(scope = 'session')
def tokens():
    yield GetToken()


# a=GetToken()
# print(a.getToken('sysadmin','admin'))

