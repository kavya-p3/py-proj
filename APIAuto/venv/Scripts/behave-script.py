#!"C:\Users\kp\PycharmProjects\API Auto\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'behave==1.2.7.dev2','console_scripts','behave'
__requires__ = 'behave==1.2.7.dev2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('behave==1.2.7.dev2', 'console_scripts', 'behave')()
    )
