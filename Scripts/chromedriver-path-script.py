#!c:\users\onoga\onedrive\desktop\mydocker\venvs\selenium\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'chromedriver-binary-auto==0.1.1','console_scripts','chromedriver-path'
__requires__ = 'chromedriver-binary-auto==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('chromedriver-binary-auto==0.1.1', 'console_scripts', 'chromedriver-path')()
    )
