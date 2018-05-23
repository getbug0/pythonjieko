# coding:utf-8
import requests
import unittest

class Testceas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        print("前置条件")
    @classmethod
    def tearDownClass(cls):
        print("后置条件")

    def test_01(self):
        # self.s.get(url='sfe')
        print('第一条用例')

    def test_02(self):
        print("第二条用例")

if __name__ == '__main__':
    unittest.main()