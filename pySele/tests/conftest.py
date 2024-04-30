import pytest
from selenium import webdriver
import time
dr = None


@pytest.fixture(scope="class")
def setup(request):
    global dr
    dr = webdriver.Chrome(executable_path="C:\\Users\\kp\\PycharmProjects\\pySele\\Exe\\chromedriver.exe")
    dr.get("https://qa-pegasus2-hns.figmd.com/signup/login")
    time.sleep(5)
    dr.maximize_window()
    request.cls.dr = dr
    # yield
    # dr.close()


