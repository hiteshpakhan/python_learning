from re import L
import unittest
from unittest.main import main
import one

class TestOne(unittest.TestCase):
    def setUp(self):                #before each method in the class the setUP() method will be executed automatically
        print("now we are going to execute a new test")

    def test_fun(self):
        result = one.funone(5)
        self.assertEqual(result, 5+5**5)

    def test_fun2(self):
        result = one.funtwo(5)
        self.assertEqual(result, 40)

    def tearDown(self):             #after every method in our class the tearDown() method will be executed automatically
        print("we have executed the test function")

if __name__ == "__main__":
    unittest.main()