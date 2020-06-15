import unittest
from tools.read_json import *
from parameterized import parameterized
from module.login import *


class TestLogin(unittest.TestCase):

    # @parameterized.expand(ReadJson('login.json').get_single_data('login01'))
    @parameterized.expand(ReadJson('login.json').get_data())
    def testLogin(self,url,account,password,status):
        u'''登录测试'''
        ret=Login(url).get_login(account,password)
        self.assertEqual(ret['status'],status)