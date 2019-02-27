import os
import configparser
# import requests
from requests import cookies


class TestConfig():
    def __init__(self):
        self.cf = self.db_config()
        self.db_host = self.cf.get("db","db_host")
        self.db_port = self.cf.getint("db","db_port")
        self.db_user = self.cf.get("db","db_user")
        self.db_password = self.cf.get("db","db_password")
        self.db_database = self.cf.get("db","db_database")

        self.__url = self.cf.get("url","base")
        self.url_login = self.__url + self.cf.get("url","login")
        self.url_adduser = self.__url + self.cf.get("url","adduser")

        self.store = cookies.RequestsCookieJar()

    def db_config(self):
        os.chdir('/Users/lichao/workspace/autopython/AutoTest-Python/config')
        self.cf = configparser.ConfigParser()
        self.cf.read('config.ini')
        return self.cf
