import pytest
import yaml
import requests as re
from util.commonlib import get_test_data
cases, list_params = get_test_data("./data/api.yaml")
class TestInPost():
    @pytest.mark.parametrize('case,http',list(list_params), ids=cases)
    def test_in_post(self,case,http):
        with re.session() as s:
            _json = s.post(
                url = http['path'],
                headers = http['headers'],
                json = http['body'])
        return _json
        assert code=='200'
