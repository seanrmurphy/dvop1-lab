import datetime
import unittest
from simple_python_service import *

class TestSimpleService(unittest.TestCase):

    def test_root_endpoint(self):
        return_val = root_endpoint()
        self.assertEqual(return_val, 'CCP2 - Devops 1 Lab Demonstration Service!')


    def test_status(self):
        return_val = status()
        self.assertEqual(return_val, '{"status": "OK"}')


    def test_hello(self):
        return_val = hello('Test')
        now = datetime.datetime.now()
        #{"welcome_string": "Hello Test - today is 19 Mar"}
        comparison_str = '{\"welcome_string\": \"Hello Test - today is ' + datetime.datetime.strftime(now, "%d %b") + '\"}'  
        self.assertEqual(return_val, comparison_str)


if __name__ == '__main__':
    unittest.main()
