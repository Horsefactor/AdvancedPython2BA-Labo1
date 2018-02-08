# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(n):
        # À compléter...
    try:
        while n > 0:
        fact = 1
        fact = fact*n
        n -= 1
   
    except :
        pass

    finally :  
         return fact
        
    
    def test_roots(a, b, c):
        # À compléter...
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
