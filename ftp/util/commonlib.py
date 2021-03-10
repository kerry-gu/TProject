import yaml
import pytest
def get_test_data(data_path):
    case = [] #存储测试用例名称
    http = [] #存储请求对象
    dat = yaml.safe_load(open(data_path,encoding="utf-8"))
    test = dat['tests']
    for td in test:
        case.append(td.get('case',''))
        http.append(td.get('http',{}))
    parameters = zip(case,http)
    return case,parameters