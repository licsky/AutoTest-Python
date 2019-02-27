import requests
import json
from AboutUsers import BcUsers
from base_fun import md5

class BcBorrow(BcUsers):
    def __init__(self, phone=None, password=None):
        self.phone = phone
        self.password = password
        self.data = {}
    
    def home_borrow_list(self):
        self.data['home_borrow_list'] = {}
        data = self.data['home_borrow_list']
        payload = dict(
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/top/borrow/manage/list'
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data 

    def borrow_list(self, pageSize=10, pageIndex=1):
        self.data['borrow_list'] = {}
        data = self.data['borrow_list']
        payload = dict(pageSize = pageSize,
                       pageIndex = pageIndex
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/invests/general'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data 

    def borrow_data(self, borrowid):
        self.data['borrow_data'] = {}
        data = self.data['borrow_data']
        payload = dict(
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/invests/general/'+borrowid
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def borrow_records(self, borrowid, pageSize=10, pageIndex=1):
        self.data['borrow_data'] = {}
        data = self.data['borrow_data']
        payload = dict(pageSize=pageSize,
                        pageIndex=pageIndex
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/invests/general/'+borrowid+ '/records'
        req = requests.request("POST", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data 

    def borrow_tender_msg(self, borrowid):
        self.data['borrow_tender_msg'] = {}
        data = self.data['borrow_tender_msg']
        payload = dict(
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/invests/general/'+borrowid+ '/tender'
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data
    
    def tender_status(self):
        self.data['tender_status'] = {}
        data = self.data['tender_status']
        payload = dict(
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/invests/precheck'
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data

    def tender_protocol(self):
        self.data['tender_status'] = {}
        data = self.data['tender_status']
        payload = dict(
                )
        header = {}
        url = 'https://mapi.baocai.com/v2/invests/protocol'
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data
    
    def borrow_tender(self,borrowId,bidAmount,paypwd,bonusTicketId=0,increaseTicketId=0,tenderUseTicketStyle='hand'):
        self.data['borrow_tender'] = {}
        data = self.data['borrow_tender']
        payload = dict(bidAmount=bidAmount,
                        payPassword=paypwd
                )
        print(self.phone)
        print(self.password)
        token = BcUsers(self.phone, self.password).login()
        print(token)
        token = token['login']['token']
        header = {"X-Authorization":token}
        url = 'https://mapi.baocai.com/v2/invests/general/'+borrowId+'/tender'
        req = requests.request("GET", url, data = payload, headers = header)
        text_json = json.loads(req.text)
        #print(text_json)
        if text_json['message'] == 'OK':
            data['flag'] = True
            data['status'] = req.status_code
            data['data'] = text_json['data']
        else:
            data['flag'] = False
            data['message'] = text_json['message']
        return self.data