import unittest
from tools.read_json import *
from parameterized import parameterized
from module.login import *

# def get_data():
#     ret = ReadJson('login.json').read_json()
#     arr = []
#     for k, v in ret.items():
#         arr.append(v)
#     return [tuple(arr)]

class TestLogin(unittest.TestCase):

    @parameterized.expand(ReadJson('login.json').get_data())
    def testLogin(self,url,account,password,status):
        ret=Login(url).get_login(account,password)
        self.assertEqual(ret['status'],status)