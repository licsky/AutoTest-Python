import unittest
import time
from util.HTMLTestRunner import HTMLTestRunner
from AboutUsers import BcUsers

class Test_login(unittest.TestCase):
    def setUp(self):
        self.username = 'anruo'
        self.password = '123456a'
        self.paypwd = '123456b'
        self.test_user = BcUsers(self.username, self.password)

    def test_ok_login(self):
        self.assertEqual(self.test_user.login()['login']['flag'], True)

    def test_forget_password(self):
        data = self.test_user.forget_password()
        self.assertEqual(data['forget_password']['flag'], True, msg=data['forget_password']['message'])
        forget_sign = data['forget_password']['forget_sign']
        data = self.test_user.forget_sign_password(forget_sign)
        self.assertEqual(data['forget_sign_password']['flag'], True, msg=data['forget_sign_password']['message']
        )
        data = self.test_user.code_password()
        self.assertEqual(data['code_password']['flag'], True, msg=data['code_password']['message'])
        data = self.test_user.reset_password(self.paypwd)
        self.assertEqual(data['reset_password']['flag'], True, msg=data['reset_password']['message'])
    



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_login("test_ok_login"))
    suite.addTest(Test_login("test_forget_password"))

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title = '测试报告',
        description='测试用例执行情况：'
    )
    runner.run(suite)
    fp.close()
    