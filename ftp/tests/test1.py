import pytest
import yaml
import requests as re
from util.commonlib import get_test_data
cases, list_params = get_test_data("./data/login.yaml")
class TestInPost():
        @pytest.mark.parametrize('case,http,expected',list(list_params), ids=cases)
        def test_in_post():
            with re.session() as s:
                _json = s.post(
                    url = env['host']['host']+http['path'],
                    headers = http['headers'],
                    json = http['body'])
            return _json
            assert code=='200'