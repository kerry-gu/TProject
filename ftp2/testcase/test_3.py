import requests as req
import yaml
import json
import pytest
import logging
from util.commonlib import get_yaml_data
from util.mycookie import mycookie
from util.utils import utils

cases,list_params = get_yaml_data("./data/user.yaml")
@pytest.mark.parametrize('case,http',list(list_params), ids=cases)
def test_3(case,http,env):
    print('-----------')
    log = logging.getLogger('test_3')
    log.info('~~~~~~~~~~~~user~~~~~~')
    log.info(str(mycookie.get_allcookie()))
    with req.session() as s:
        data=s.post(
            url = env["host"]["host"]+http['path'],
            cookies = mycookie.get_allcookie(),
            headers = http['headers'],
            data = http['body']
        )
        
        log.info(data.status_code)
        # log.info(str(data.content))
        
        assert data.status_code == 200