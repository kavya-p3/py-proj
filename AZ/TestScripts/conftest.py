import pytest
from selenium import webdriver
import os
from datetime import datetime
from selenium.webdriver.chrome.options import Options

dr = None
reg = []
filelocation=None


# def pytest_addoption(parser):
#     parser.addoption(
#         "--Registry_Name", action="append", default=[]
#     )


# def pytest_generate_tests(metafunc):
#     if "Registry_Name" in metafunc.fixturenames:
#         metafunc.parametrize("Registry_Name", metafunc.config.getoption("Registry_Name"))
#
#
# @pytest.fixture()
# def setup(Registry_Name, request):
#
#     global dr
#     reg = Registry_Name
#     now = datetime.now()
#     file = now.strftime('%d-%m-%Y (%H-%M-%S)')
#
#     dirName = 'C:\\Users\\kp\\Desktop\\Automation\\' + str(file)+reg
#     print(dirName)
#     if not os.path.exists(dirName):
#         os.makedirs(dirName)
#     dr = webdriver.Chrome(executable_path="C:\\Users\\kp\\PycharmProjects\\pySele\\Exe\\chromedriver.exe")
#
#     # dr.set_page_load_timeout(30)
#     # reg = request.config.getoption("Registry_Name")
#
#     if reg in ['unifirmd-elixir', 'compulink-elixir', 'ecw-elixir']:
#         dr.get("https://qa-peg2-" + reg + ".figmd.com/signup/login")
#     else:
#         dr.get("https://qa-pegasus2-" + reg + ".figmd.com/signup/login")
#     # dr.maximize_window()
#     request.cls.dr = dr
#
#     request.cls.reg = reg
#     request.cls.filelocation = str(dirName)
#     # yield
#     # dr.close()
# -----------------------------------------------------------------------------------------------------------------
# def pytest_addoption(parser):
#     parser.addoption(
#         "--Registry_Name", action="store", default="hns"
#     )
#


@pytest.fixture(scope="class", params=[])
def setup(request):
    global dr
    global filelocation
    #reg = request.config.getoption("Registry_Name")
    reg=request.param
    now = datetime.now()
    file = now.strftime('%d-%m-%Y (%H-%M-%S)')

    dirName = 'C:\\Users\\kp\\Desktop\\Automation\\' + str(file) + reg
    print(dirName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    op = Options()
    op.add_argument('--start-maximized')
    op.add_argument("Zoom 65%")
    dr = webdriver.Chrome(options=op, executable_path="C:\\Users\\kp\\PycharmProjects\\pySele\\Exe\\chromedriver.exe" )



    dr.get("https://amazon.in/")



    request.cls.dr = dr
    request.cls.reg = reg
    request.cls.filelocation = dirName
    filelocation=dirName
    yield
    #dr.close()
    dr.quit()

@pytest.fixture()
def takescreenshot():
    yield

    now = datetime.now()
    file = now.strftime('%d-%m-%Y (%H-%M-%S)')
    # dr.get_screenshot_as_file(filelocation+'\\'+str(file)+'result.png')

def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)
