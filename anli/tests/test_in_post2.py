import pytest
import yaml
import requests as re
from util.commonlib import get_test_data
cases, list_params = get_test_data("./data/test_in_post.yaml")
class TestInPost():
        @pytest.mark.parametrize('case,http,expected',list(list_params), ids=cases)
        def test_in_post(sel,env,case,http,expected):
            with re.session() as s:
                _json = s.post(
                    url = env['host']['jsonplaceholder']+http['path'],
                    headers = http['headers'],
                    json = http['body'])
            return _json
            assert response["title"] == expected['response']["title"]
            assert response["body"] == expected['response']["body"]
            assert response["userId"] == expected['response']["userId"], "实际的标题是：{}".format(response["title"])