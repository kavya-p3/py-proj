import inspect
import logging
import os
from datetime import datetime


import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("takescreenshot")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    # def getScreenshotLocation(self):
    #
    #     now = datetime.now()
    #     file = now.strftime('%d-%m-%Y (%H-%M-%S)')
    #
    #     dirName = 'C:\\Users\\kp\\Desktop\\Automation\\'+str(file)
    #     print(dirName)
    #     if not os.path.exists(dirName):
    #         os.makedirs(dirName)
    #     return str(dirName)



