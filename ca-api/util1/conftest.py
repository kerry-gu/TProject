import json
import requests as req
import pytest
import pymysql

BASE_URL = 'http://192.168.6.86:9200'

#可以设置连接多个数据库
DB_SETTING = {
    'sys-center' : {
        'HOST': '192.168.6.86',
        'USER': 'root',
        'PASSWORD': 'vp123456',
        'DATABASE': 'sys-center',
    },
    'param-center': {
        'HOST': '192.168.6.86',
        'USER': 'root',
        'PASSWORD': 'vp123456',
        'DATABASE': 'param-center',
    }
}

@pytest.fixture(scope='session')
def requests_session():
    with req.session() as session:a
        session.headers.update({
            'Content-Type': 'application/json'
        })
        yield session


@pytest.fixture(scope='function')
def requests_no_session():
    with req.session() as session:
        session.headers.update({'Content-Type': 'application/json'})
        yield session


@pytest.fixture(scope='session')
def base_url():
    return BASE_URL

class _TokenList:
    _data = {}

    def set(self, username: str, password: str) -> str:
        data = {
            'username': username,
            'password':password,
        }
        headers = {
            'client_id': 'webApp',
            'client_secret': 'webApp'
        }
        url = BASE_URL + "/api-auth/oauth/user/token"
        with req.session() as session:
            session.headers.update({'Content-Type': 'application/json'})
            r = session.post(url, json=data, headers=headers)
            assert r.status_code == 200

            # 此处保存用户的 Token 信息
            response_data = r.json()
            assert response_data['code'] == 200
            self._data[username] = response_data['data']['access_token']
            # 

            return response_data['data']['access_token']


    def get(self, username: str) -> str:
        return self._data[username]

@pytest.fixture(scope='session')
def tokens():
    yield  _TokenList()


class _DBConnections:
    _data = {}

    def get(self, database: str) -> pymysql.connections.Connection:
        if not database in self._data.keys():
            self._data[database] = pymysql.connect(
                host=DB_SETTING[database]['HOST'],
                user=DB_SETTING[database]['USER'],
                password=DB_SETTING[database]['PASSWORD'],
                db=DB_SETTING[database]['DATABASE'],
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        return self._data[database]

    def __del__(self):
        for k in self._data:
            self._data[k].close()


@pytest.fixture(scope='session')
def connect():
    yield _DBConnections()

