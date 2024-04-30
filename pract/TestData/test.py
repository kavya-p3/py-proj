import pytest
from selenium import webdriver
import os
from datetime import datetime

dr = None


def pytest_addoption(parser):
    parser.addoption(
        "--Registry_Name", action="append", default=[]
    )

def pytest_generate_tests(metafunc):
    if "Registry_Name" in metafunc.fixturenames:
        metafunc.parametrize("Registry_Name", metafunc.config.getoption("Registry_Name"))

@pytest.fixture(scope="class")
def setup(request):
    global dr
    now = datetime.now()
    file = now.strftime('%d-%m-%Y (%H-%M-%S)')

    dirName = 'C:\\Users\\kp\\Desktop\\Automation\\' + str(file)
    print(dirName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    # return str(dirName)

    dr = webdriver.Chrome(executable_path="C:\\Users\\kp\\PycharmProjects\\pySele\\Exe\\chromedriver.exe")
    reg = request.config.getoption("Registry_Name")
    if reg in ['unifirmd-elixir', 'compulink-elixir', 'ecw-elixir']:
        dr.get("https://qa-peg2-" + reg + ".figmd.com/signup/login")
    else:
        dr.get("https://qa-pegasus2-" + reg + ".figmd.com/signup/login")
    # dr.maximize_window()
    request.cls.dr = dr
    request.cls.reg = reg
    request.cls.filelocation = str(dirName)
    yield
    dr.close()


def test_login(param1):
    print(param1)
