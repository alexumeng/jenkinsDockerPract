import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Main import run

class TestInterests(unittest.TestCase):

    def test_InterestReturn1(self):
        
        result = run("Userfile.txt")
        self.assertEqual(result, [('games', 10), ('arena', 6), ('apex', 4), ('various', 4), ('syndicate', 4)])
        print("Test 1 Succesful")

    def test_InterestReturn2(self):
        
        result = run("Userfile.txt")
        self.assertEqual(result, [('jesse', 12), ('ivor', 6), ('group', 6), ('wither', 5), ('portal', 4)])
        print("Test 2 Succesful")


