import yaml
import pytest

def get_yaml_data(data_path):
    case=[]
    http=[]
    dat = yaml.safe_load(open(data_path,encoding="utf-8"))
    test=dat['tests']
    for i in test:
        case.append(i.get('case',''))
        http.append(i.get('http',{}))
    parameters =zip(case,http)
    return case,parameters
# a=get_yaml_data('login.yaml')
# print(a)
