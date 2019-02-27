import pymysql
from config.TestConfig import TestConfig


def MysqlDB():

    connect = pymysql.Connect(host=TestConfig().db_host,
                    port = TestConfig().db_port,
                    user = TestConfig().db_user,
                    password = TestConfig().db_password,
                    db = TestConfig().db_database
                    )
    return connect

def MysqlEnd(cur, db):
    cur.close()
    db.close()