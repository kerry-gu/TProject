import sys
sys.path.append('../..')
from data.r_adi import DataToapi
import requests
# import json

class Cookies:
    def __init__(self):
        print('------initcookies-------')
    
    def get_cookies(self,row,col):
        url = DataToapi().col_excels(row,col)
        data={
            "username":"sysadmin",
            "password":"111111"	
        }
        res = requests.post(url,data)
        r=requests.utils.dict_from_cookiejar(res.cookies)
        return r

# class Cookies:
    
#     def cc(self):
#         url = 'http://192.168.13.125:7001/vp/login.jsp'
#         data={
#             "username":"13810173310" ,
#             "password":"123456"	
#         }
#         res = requests.get(url,data)
#         r=requests.utils.dict_from_cookiejar(res.cookies)
#         return r



