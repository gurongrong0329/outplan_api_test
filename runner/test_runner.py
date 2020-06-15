# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2020/6/15 9:56
# 文件: test_runner.py
import sys

sys.path.append('..')
import HTMLTestRunner
import unittest
import datetime
from tools.emailserver import EmailServer


class Runner(unittest.TestCase):

    def report(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_path = '../report/' + '{}.html'.format(now_time)

        with open(report_path, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report', description='')
            suiteTest = unittest.TestSuite()
            all_cases = unittest.defaultTestLoader.discover('../case/', 'test_*.py')

            for case in all_cases:
                suiteTest.addTest(case)
            runner.run(suiteTest)

        email = EmailServer()
        email.sendEmail(report_path)

if __name__ == '__main__':
    testrunner = Runner()
    testrunner.report()
