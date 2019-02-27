import requests
import json
import unittest
from config.mysqlconfig import MysqlDB, MysqlEnd
from model.LoginCase import *
from config.TestConfig import TestConfig
from util.getResult import GetResult


class Test_login(unittest.TestCase):
    def setUp(self):
        self.db = MysqlDB()
        self.cursor = self.db.cursor()
        self.store = TestConfig().store
        # 初始化测试数据，测试url

    def test_login_true(self):
        sql = "select * from loginCase where id=%s;"

        self.cursor.execute(sql,(1))
        self.query = LoginCase(self.cursor.fetchone())

        result = GetResult().get_result(self.query)

        self.assertEqual(str(result), self.query.expected)

        # 测试用例

    def test_login_false(self):
        sql = "select * from loginCase where id=%s;"

        self.cursor.execute(sql, (2))
        self.query = LoginCase(self.cursor.fetchone())

        result = self.getResult()
        self.assertEqual(str(result), self.query.expected)

    def getResult(self):
        payload = dict(userName=self.query.userName,
                       password=self.query.password
                       )
        header = {'Content-Type': "application/json"}
        url = TestConfig().url_login
        req = requests.post(url, data=json.dumps(payload), headers=header)
        text_json = json.loads(req.text)
        self.store = req.cookies
        print(self.store)
        return text_json
        # 测试执行请求

    def tearDown(self):
        MysqlEnd(self.cursor, self.db)
        # 结束测试释放资源，关闭sql查询
