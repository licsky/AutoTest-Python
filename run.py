from case.logincase import *
from case.addusercase import *
import time
from util.HTMLTestRunner import HTMLTestRunner
import unittest


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_login("test_login_true"))
    #suite.addTest(Test_login("test_login_false"))
    suite.addTest(Test_adduser("test_adduser"))

    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = './report/' + now + 'result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(
    #     stream=fp,
    #     title='测试报告',
    #     description='测试用例执行情况：'
    # )
    # runner.run(suite)
    # fp.close()
    runner = unittest.TextTestRunner()
    runner.run(suite)