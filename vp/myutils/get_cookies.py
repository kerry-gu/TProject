# import sys
# sys.path.append('../..')
# from data.r_adi import DataToapi
import requests
# # import json

# class Cookies:
#     def __init__(self):
#         print('------initcookies-------')
    
#     def get_cookies(self,row,col):
#         url = DataToapi().col_excels(row,col)
#         data={
#             "username":"sysadmin",
#             "password":"111111"	
#         }
#         res = requests.post(url,data)
#         r=requests.utils.dict_from_cookiejar(res.cookies)
#         return r

class Cookies:
    
    def cc(self):
        url = 'http://192.168.13.125:7001/vp/login.jsp'
        data={
            "username":"sysadmin" ,
            "password":"000000"	
        }
        res = requests.get(url,data)
        r=requests.utils.dict_from_cookiejar(res.cookies)
        return r
a=Cookies()
b= a.cc()
print(b)

