'''
# insert the tests directory into this path
import sys
sys.path.insert(0, './tests')

# import ./tests/main.py
import main

main.main()
'''

from tests.main import *

testAll()
