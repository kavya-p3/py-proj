import pytest
from selenium import webdriver
import os
from datetime import datetime
from selenium.webdriver.chrome.options import Options


dr = None


def pytest_addoption(parser):
    parser.addoption(
        "--Registry_Name", action="append", default=[]
    )


def pytest_generate_tests(metafunc):
    if "Registry_Name" in metafunc.fixturenames:
        metafunc.parametrize("Registry_Name", metafunc.config.getoption("Registry_Name"))


@pytest.fixture()
def setup(Registry_Name, request):

    global dr
    reg = Registry_Name
    now = datetime.now()
    file = now.strftime('%d-%m-%Y (%H-%M-%S)')

    dirName = 'C:\\Users\\kp\\Desktop\\Automation\\' + str(file)+reg
    print(dirName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    dr = webdriver.Chrome(executable_path="C:\\Users\\kp\\PycharmProjects\\pySele\\Exe\\chromedriver.exe")

    # dr.set_page_load_timeout(30)
    # reg = request.config.getoption("Registry_Name")

    if reg in ['unifirmd-elixir', 'compulink-elixir', 'ecw-elixir','epic-elixir']:
        dr.get("https://qa-peg2-" + reg + ".figmd.com/signup/login")
    else:
        dr.get("https://qa-pegasus2-" + reg + ".figmd.com/signup/login")
    # dr.maximize_window()
    request.cls.dr = dr

    request.cls.reg = reg
    request.cls.filelocation = str(dirName)
    # yield
    # dr.close()

