import unittest
import calc

class Testcalc(unittest.TestCase):
    def test_calc(self):        #imp to start the name of the test method by test
        result = calc.function1(5, 6)
        self.assertEqual(result, 5)

    def test_calc2(self):
        self.assertEqual(calc.function1(7, 8), 7)
        self.assertEqual(calc.function1(-3, 2), -1)
        self.assertEqual(calc.function1(0, 8), 7)   #this will fail

        self.assertRaises(ValueError, calc.divide, 10, 0)   #here we are passsing each argument seprately

        

if __name__ == "__main__":
    unittest.main() #unittest.main() is the special call by which the unittest can be execute 
# or
# to run this file you have to go to the terminal on this folder and run the following command
# python -m unittest test_calc.py









# the following are the things that you can do with assert method

# assertEqual(a, b)         # a == b
# assertNotEqual(a, b)      # a != b
# assertTrue(x)             # bool(x) is True
# assertFalse(x)            # bool(x) is False
# assertIs(a, b)            # a is b
# assertIsNot(a, b)         # a is not b
# assertIsNone(x)           # x is None
# assertIsNotNone(x)        # x is not None
# assertIn(a, b)            # a in b
# assertNotIn(a, b)         # a not in b
# assertIsInstance(a, b)    # isinstance(a, b)
# assertNotIsInstance(a, b) # not isinstance(a, b)