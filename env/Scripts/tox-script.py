#!c:\Users\wwerner\programming\dbrocker\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tox==1.8.1','console_scripts','tox'
__requires__ = 'tox==1.8.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('tox==1.8.1', 'console_scripts', 'tox')()
    )
