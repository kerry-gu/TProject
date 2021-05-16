import os
import yaml
import requests as re
import pytest
import logging
from util.commonlib import get_yaml_data
@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")

# mycookies = ''
# @pytest.fixture(scope="session")
# def get_cookie():
#     global mycookies
#     return mycookies

# cases, list_params = get_test_data("./data/login.yaml") 
# class Testgetcookies():
#     _cookie = {}
#     @pytest.mark.parametrize('case,http',list(list_params), ids=cases)
#     def savacookie(self,case,http,env):
#         print('-----------')
#         log = logging.getLogger('test1')
#         log.info('~~~~~~~~~~~~~~~~~~')
#         with re.session() as s:
#             _json = s.post(
#                 url = env["host"]["host"]+http['path'],
#                 headers = http['headers'],
#                 json = http['body']
#                 )
#             print(_json)
#             log.info(_json)
#             log.debug(_json)
#             res=re.utils.dict_from_cookiejar(_json.cookies)
#             _cookie=response_data
#             return self._cookie

# @pytest.fixture(scope='session')
# def cook():
#     return self._cookie