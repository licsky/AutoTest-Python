import requests
from requests import cookies
import json
from config.TestConfig import TestConfig


class GetResult():
    def __init__(self):
        self.url_login = TestConfig().url_login
        self.url_adduser = TestConfig().url_adduser
        self.store = cookies.RequestsCookieJar()

    def get_result(self, query):
        payload = dict(userName=query.userName,
                       password=query.password
                       )
        header = {'Content-Type': "application/json"}
        url = self.url_login
        req = requests.post(url, data=json.dumps(payload), headers=header)
        text_json = json.loads(req.text)
        self.store = req.cookies
        print(self.store)
        return text_json

    def add_result(self, query):
        payload = dict(userName=query.userName,
                       password=query.password,
                       sex=query.sex,
                       age=query.age,
                       permission=query.permission,
                       isDelete=query.isDelete,
                       expected=query.expected
                       )
        header = {'Content-Type': "application/json"}
        store = self.store
        url = self.url_adduser
        req = requests.post(url, data=json.dumps(payload), headers=header, cookies=store)
        text_json = json.loads(req.text)
        return text_json
