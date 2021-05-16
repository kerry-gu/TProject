import requests as req
import yaml
import json
import pytest
import logging
from util.commonlib import get_yaml_data

cases,list_params = get_yaml_data("./data/api.yaml")
@pytest.mark.parametrize('case,http',list(list_params), ids=cases)
def test_2(case,http,env,test_1):
    print('-----------')
    log = logging.getLogger('test_1')
    log.info('~~~~~~~~~~~~~~~~~~')
    with req.session() as s:
        data=s.post(
            url = env["host"]["host"]+http['path'],
            cookies = test_1,
            headers = http['headers'],
            json = http['body']
        )
        log.info(data.status_code)
        log.info(str(data))
        # log.info(type(str))
        # log.info(str)
        assert data.status_code == 200