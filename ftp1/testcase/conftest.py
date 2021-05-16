import requests as req
import yaml
import json
import pytest
import logging
from util.commonlib import get_yaml_data
# import http.cookiejar as cooieslib
cases,list_params = get_yaml_data("./data/login.yaml")

@pytest.fixture(scope="function")
@pytest.mark.parametrize('case,http',list(list_params), ids=cases)
def test_1(case,http,env):
    log = logging.getLogger('test_1')
    log.info('~~~~~~~~login~~~~~~~~~~')
    with req.session() as s:
        _json=s.post(
            url = env["host"]["host"]+http['path'],
            headers = http['headers'],
            json = http['body']
        )
        resdata=req.utils.dict_from_cookiejar(_json.cookies)
        # print(resdata)
        log.info(resdata)
        log.info(_json.status_code)
        # log.debug(resdata)
        assert _json.status_code == 200
        return resdata
        # print(resdata)

# cookies= {}
# class Testlogin():
#     @pytest.mark.parametrize('case,http',list(list_params), ids=cases)
#     def test_login(self,case,http,env):
#         print('-----------')
#         log = logging.getLogger('test_login')
#         log.info('~~~~~~~~~~~~~~~~~~')
#         with req.session() as s:
#             _json=s.post(
#                 url = env["host"]["host"]+http['path'],
#                 headers = http['headers'],
#                 json = http['body']
#             )
#             resdata=req.utils.dict_from_cookiejar(_json.cookies)
#             # print(resdata)
#             # log.info(resdata)
#             # log.debug(resdata)
#             assert _json.status_code == 200
#             return resdata
