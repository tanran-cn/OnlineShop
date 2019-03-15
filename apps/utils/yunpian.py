# _*_ coding: utf-8 _*_
__auther__ = "tanran"
__date__ = "2018/2/4 15:35"

import  requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【慕学生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__=="__main__":
    yun_pian = YunPian("c310b8691ac5d4ad7c0a479213891eb2")
    yun_pian.send_sms("2017", "18540136696")