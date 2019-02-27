import requests
import json
import re
import time
from Mydb.Sqlbase import MysqlBaocaidata
from base_fun import md5, sha1

class BcUsers():
    def __init__(self, phone, password):
        self.phone = phone
        self.password = md5(password)
        self.data = {}
        

    def login(self):
        self.data['login'] = {}
        data = self.data['login']
        print(self.password)
        payload = dict(keywords = self.phone, 
                        password = self.password
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/login'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['token'] = text_json['data']['token']
            
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data 

    def login_out(self, token):
        self.data['login_out'] = {}
        data = self.data['login_out']

        payload = dict(token = token
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/logout'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['message'] == 'OK':
            data['flag'] = True
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data 

    def forget_password(self):
        self.data['forget_password'] = {}
        data = self.data['forget_password']

        payload = dict(phone = self.phone
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/reset/phone/sign'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['sign'] = text_json['data']['sign']
            data['forget_sign'] = sha1(data['sign'] + self.phone)
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def forget_sign_password(self, forget_sign):
        time.sleep(3)
        self.data['forget_sign_password'] = {}
        data = self.data['forget_sign_password']

        payload = dict(phone = self.phone,
                        forget_sign = forget_sign
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/reset/phone/code'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data
    
    def code_password(self):
        time.sleep(3)
        db = MysqlBaocaidata()
        cur = db.cursor()
        sql = "SELECT contents FROM diyou_phone_smslog WHERE phone = " + self.phone + " ORDER BY id DESC LIMIT 1"
        cur.execute(sql)
        r = cur.fetchone()
        code = re.search(r'\d{6}', r[0]).group()

        self.data['code_password'] = {}
        data = self.data['code_password']

        payload = dict(phone = self.phone,
                        code = code
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/reset/phone'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['vcode'] = text_json['data']['vcode']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def reset_password(self, new_password):
        self.data['reset_password'] = {}
        data = self.data['reset_password']

        payload = dict(phone = self.phone,
                        password = md5(new_password),
                        vcode = self.data['code_password']['vcode']
                                        )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/reset/password'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def name_verified(self, token, realname, idcard):
        self.data['name_verified'] = {}
        data = self.data['name_verified']

        payload = dict(realName = realname,
                        IDCard = idcard
                        )
        header = {"X-Authorization":token}
        url = 'https://mapi.baocai.com/v2/auth/register/id'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def change_password(self, token, new_pwd, repeatpwd):
        self.data['change_password'] = {}
        data = self.data['change_password']

        payload = dict(password = self.password,
                        newPwd = md5(new_pwd),
                        repeatPwd = md5(repeatpwd),
                        )
        header = {"X-Authorization":token}
        url = 'https://mapi.baocai.com/v2/users/password/modify'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def user_status(self, token):
        self.data['user_status'] = {}
        data = self.data['user_status']
        # m = self.login()
        # print(m)
        # if m['login']['flag']:
        #     token = m['login']['token']
        # else:
        #     data['flag'] = False
        #     data['message'] = m['login']['message']
        #     return data
        payload = dict()
        header = {"X-Authorization":token}
        url = 'https://mapi.baocai.com/v2/users/password/modify'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def set_paypwd(self,token, paypwd):
        self.data['set_paypwd'] = {}
        data = self.data['set_paypwd']

        payload = dict(password = self.password,
                        payPassword = md5(paypwd)
                        )
        header = {"X-Authorization":token}
        url = 'https://mapi.baocai.com/v2/invests/paypassword'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def modify_paypwd(self, token, new_paypwd, repeatpwd):
        self.data['modify_paypwd'] = {}
        data = self.data['modify_paypwd']

        payload = dict(payPassword = self.password,
                        newPaypwd = md5(paypwd),
                        repeatPaypwd = md5(repeatpwd)
                        )
        header = {"X-Authorization":token}
        url = 'https://mapi.baocai.com/v2/invests/paypassword'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

class BcUserRegister():
    def __init__(self, phone, pwd):
        self.phone = phone
        self.pwd = md5(pwd)
        self.data = {}

    def register_protocol(self):
        self.data['register_protocol'] = {}
        data = self.data['register_protocol']

        payload = ""
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/register/protocol'
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def register_sign(self):
        self.data['register_sign'] = {}
        data = self.data['register_sign']

        payload = dict(phone = self.phone 
                        )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/register/phone/sign'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['sign'] = text_json['data']['sign']
            data['reg_sign'] = sha1(data['sign'] + self.phone)
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def register_sign_code(self, reg_sign):
        time.sleep(3)
        self.data['register_sign_code'] = {}
        data = self.data['register_sign_code']

        payload = dict(phone = self.phone,
                        reg_sign = reg_sign
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/register/phone/code'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data
    
    def code_register(self):
        time.sleep(3)
        db = MysqlBaocaidata()
        cur = db.cursor()
        sql = "SELECT contents FROM diyou_phone_smslog WHERE phone = " + self.phone + " ORDER BY id DESC LIMIT 1"
        cur.execute(sql)
        r = cur.fetchone()
        code = re.search(r'\d{6}', r[0]).group()

        self.data['code_register'] = {}
        data = self.data['code_register']

        payload = dict(phone = self.phone,
                        code = code
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/register/phone'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['vcode'] = text_json['data']['vcode']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def set_password(self):
        self.data['set_password'] = {}
        data = self.data['set_password']

        payload = dict(phone = self.phone,
                        password = self.pwd,
                        vcode = self.data['code_register']['vcode']
                                        )
        header = {}
        url = 'https://mapi.baocai.com/v2/auth/register/user'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        print(text_json)
        if text_json['data']['error']['code'] == '0000':
            data['flag'] = True
            data['message'] = text_json['message']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    