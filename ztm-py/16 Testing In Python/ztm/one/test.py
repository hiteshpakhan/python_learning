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


if __name__ == "__main__":
    unittest.main()

# or you can also run this file in terminal by folling
# python -m unittest

# and if you want to test but get more info about your test cases you can use the following command in terminal
# python -m unittest -v         #here v stands for verbose