# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    
    def test_fact(self):
        self.assertEqual(fact(3),6)
        self.assertEqual(fact(0),1)
        self.assertEqual(fact(1),1)
        self.assertEqual(fact(4),24)
        
        
    
    def test_roots(self):

        self.assertEqual(roots(3, 2, 1), None)
        self.assertEqual(roots(4, 3, 5), None)
        self.assertEqual(roots(1, 2, 3), None)
        self.assertEqual(roots(1, 0, -1), (1, -1))
       
     
    def test_integrate(self):

        self.assertEqual(integrate(ff(),0,5), 110/3)
        


        


        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
