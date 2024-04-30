import pytest
# import openpyxl
# from datetime import datetime, timedelta
#
# Path = 'C:\\Users\\kp\\Desktop\\testdata.xlsx'
# wb = openpyxl.load_workbook(Path)
# sheet = wb.active
# i=2
# testdata = []
# while sheet.cell(row = i, column = 1).value is not None:
#     testdata.append((sheet.cell(i,1).value, sheet.cell(i,2).value, sheet.cell(i,3).value))
#     i+=1
#
#
#
#
# @pytest.mark.parametrize("a,b,expected", testdata)
# def test_timedistance_v0(a, b, expected):
#     diff = int(a) - int(b)
#     assert diff == int(expected)

reg = None
def pytest_addoption(parser):
    global reg
    reg=parser.addoption(
        "--Registry_Name", action="store", default=['hns']

    )


print(reg)


