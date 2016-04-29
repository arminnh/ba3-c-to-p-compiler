# 3 attempts that didnt really work:

'''

from tests.main import *

testAll()
'''


'''
import unittest

if __name__=="__main__":
    testsuite = unittest.TestLoader().discover('tests/')
    unittest.TextTestRunner(verbosity=1).run(testsuite)
'''


'''
# insert the tests directory into this path
import sys
sys.path.insert(0, './tests')

# import ./tests/main.py
import main

main.testAll()
'''


import os
os.chdir("./tests/")
os.system("python3 main.py")
