import yaml


def get_test_data(data_path):
    case = [] #存储测试用例名称
    http = [] #存储请求对象
    dat = yaml.safe_load(open(data_path,encoding="utf-8"))#加载yaml文件数据
    test = dat['tests']
    for i in test:
        case.append(i.get('case',))
        http.append(i.get('http',{}))
    parameters =zip(case,http)
    return case,parameters
    # return parameters

a=get_test_data("api.yaml")
print(a)