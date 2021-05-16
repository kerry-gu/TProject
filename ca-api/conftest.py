import os
import requests as re
import pytest
import yaml
import logging
from util.commonlib import get_test_data
cases, list_params = get_test_data("./data/login.yaml") 

class Testgetcookies():
    _cookie = {}
    @pytest.mark.parametrize('case,http',list(list_params), ids=cases)
    def savacookie(self,case,http,env):
        print('-----------')
        log = logging.getLogger('test1')
        log.info('~~~~~~~~~~~~~~~~~~')
        with re.session() as s:
            _json = s.post(
                url = env["host"]["host"]+http['path'],
                headers = http['headers'],
                json = http['body']
                )
            print(_json)
            log.info(_json)
            log.debug(_json)
            res=re.utils.dict_from_cookiejar(_json.cookies)
            _cookie=response_data
            return self._cookie

@pytest.fixture(scope='session')
def cook():
    return self._cookie

