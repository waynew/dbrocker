#!c:\Users\wwerner\programming\dbrocker\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest==2.6.4','console_scripts','py.test-3.5'
__requires__ = 'pytest==2.6.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pytest==2.6.4', 'console_scripts', 'py.test-3.5')()
    )
