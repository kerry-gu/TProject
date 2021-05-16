import requests as req
import yaml
import json
import pytest
import logging
from util.commonlib import get_yaml_data
from util.mycookie import mycookie
from util.utils import utils

cases,list_params = get_yaml_data("./data/login.yaml")
@pytest.mark.parametrize('case,http',list(list_params), ids=cases)
def test_2(case,http,env):
    print('-----------')
    log = logging.getLogger('test_1')
    log.info('~~~~~~~~~~~~login~~~~~~')
    log.info(str(mycookie.get_cookie("JSESSIONID")))
    with req.session() as s:
        data=s.post(
            url = env["host"]["host"]+http['path'],
            cookies = {"JSESSIONID": mycookie.get_cookie("JSESSIONID")},
            headers = http['headers'],
            data = http['body']
        )
        resdata=req.utils.dict_from_cookiejar(data.cookies)
        utils.dealCookie(resdata, mycookie)
        assert data.content == b'1'
        mycookie.set_cookie('loginUserName', http['body']["username"])
        mycookie.set_cookie('loginPassword', str(http['body']["password"]))
        log.info(data.status_code)
        log.info(data.content)
        log.info(str(mycookie.get_allcookie()))
        
        assert data.status_code == 200