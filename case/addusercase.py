import requests
import json
import unittest
from config.mysqlconfig import MysqlDB, MysqlEnd
from model.AddUserCase import *
from config.TestConfig import TestConfig


class Test_adduser(unittest.TestCase):
    def setUp(self):
        self.db = MysqlDB()
        self.cursor = self.db.cursor()
        self.url = TestConfig().url_adduser
        self.store = TestConfig().store
        # 初始化测试数据，测试url

    def tearDown(self):
        MysqlEnd(self.cursor, self.db)
        # 结束测试释放资源，关闭sql查询

    def test_adduser(self):

        sql = "select * from addUserCase where id=%s;"

        self.cursor.execute(sql, (1))
        self.query = AddUserCase(self.cursor.fetchone())

        result = self.getResult()
        self.assertTrue(result)
        self.assertEqual(str(result), self.query.expected)

    def getResult(self):
        payload = dict(userName=self.query.userName,
                       password=self.query.password,
                       sex=self.query.sex,
                       age=self.query.age,
                       permission=self.query.permission,
                       isDelete=self.query.isDelete,
                       expected=self.query.expected
                       )
        header = {'Content-Type': "application/json"}
        #self.store.set('login','true')
        url = self.url
        req = requests.post(url, data=json.dumps(payload), headers=header, cookies=self.store)
        text_json = json.loads(req.text)
        return text_json