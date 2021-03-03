
import os
import pytest
import yaml
@pytest.fixture(scope = 'session')
def env(request):
    config_path = os.path.join(request.config.rootdir,
                                'config',
                                'test',
                                'config.yaml')
    with open (config_path) as f:
        env_config = yaml.load(f.read(),loader = yaml.Safeloader)
    return env_config   

# import os
# import pytest
# import yaml

# @pytest.fixture(scope="session")
# def env(request):
#     config_path = os.path.join(request.config.rootdir,
#                                "config",
#                                request.config.getoption("environment"),
#                                "config.yaml")
#     with open(config_path) as f:
#         env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
#     return env_config

# def pytest_addoption(parser):
#     parser.addoption("--env",
#                      action="store",
#                      dest="environment",
#                      default="test",
#                      help="environment: test or prod")                             