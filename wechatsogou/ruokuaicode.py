# -*- coding: utf-8 -*-

import requests
from hashlib import md5
from PIL import Image
from io import BytesIO
from .base import WechatSogouBase
import base64
import time
import datetime


class RClient(WechatSogouBase):

    def __init__(self, appCode, appKey, appSecret, v_type):
        self.appCode = appCode
        self.appKey = appKey
        self.appSecret = appSecret
        self.v_type = v_type
        # self.username = username
        # self.password = md5(password.encode('utf-8')).hexdigest()
        # self.soft_id = soft_id
        # self.soft_key = soft_key
        # self.base_params = {
        #     'username': self.username,
        #     'password': self.password,
        #     'softid': self.soft_id,
        #     'softkey': self.soft_key,
        # }
        # self.headers = {
        #     'Connection': 'Keep-Alive',
        #     'Expect': '100-continue',
        #     'User-Agent': 'ben',
        # }

    def create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        # params = {
        #     'typeid': im_type,
        #     'timeout': timeout,
        # }
        # params.update(self.base_params)
        # files = {'image': ('a.jpg', im)}
        # r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        # return r.json()
        image = Image.open(BytesIO(im))
        t = time.time()
        nowtime = str(round(t * 1000))
        cap_path = "/Users/allmight/PycharmProjects/Aquarius/temp_cap/"+nowtime+'.jpg'
        image.save(cap_path)
        host = 'http://apigateway.jianjiaoshuju.com'
        path = '/api/v_1/fzyzm.html'
        method = 'POST'
        querys = ''
        bodys = {}
        url = host + path
        base64_data = ""
        with open(cap_path, 'rb') as fin:
            image_data = fin.read()
            base64_data = base64.b64encode(image_data)
        headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
            'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
            'appCode': self.appCode,
            'appKey': self.appKey,
            'appSecret': self.appSecret
        }
        params = {
            'v_pic': base64_data,
            'v_type': self.v_type
        }
        r = requests.post('http://apigateway.jianjiaoshuju.com/api/v_1/fzyzm.html', data=params, headers=headers)
        return r.json()
    def report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()