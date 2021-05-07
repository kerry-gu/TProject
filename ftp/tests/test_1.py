import json
import pytest
import yaml
import requests as re
import logging
from util.commonlib import get_test_data
cases, list_params = get_test_data("./data/api.yaml")
class TestInPost():
    @pytest.mark.parametrize('case,http',list(list_params), ids=cases)
    def test_1(self,case,http,env):
        log = logging.getLogger('test1')
        with re.session() as s:
            _json = s.post(
                url = env["host"]["host"]+http['path'],
                headers = http['headers'],
                json = http['body']
                )
            print(_json)
            log.info(_json)
            log.debug(_json)
            # return _json 
            assert _json.status_code == 200