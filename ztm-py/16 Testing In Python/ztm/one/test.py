import unittest
import main

class TestMain(unittest.TestCase):
    def test_fun(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)    #it will check if the result is equal to the excepted value


    def test_fun2(self):
        test_var = "ten"
        result2 = main.do_stuff2(test_var)
        # self.assertTrue(isinstance(result2, ValueError))

        # also you can use the following
        self.assertIsInstance(result2, ValueError)

unittest.main()