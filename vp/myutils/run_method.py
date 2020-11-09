import requests
import json
class RunMethod:

    def post_main(self,url,data,header=None,cookies=None):
        res = None
        if header !=None:
            res = requests.post(url=url,data=data,headers=header,cookies=cookies)
        else:
            res = requests.post(url=url,data=data,cookies=cookies)
        return self.callback(res)

    def get_main(self,url,data=None,header=None,cookies=None):
        res =None
        if header !=None:
            res = requests.get(url=url,params=data,headers=header,cookies=cookies)
        else:
            res = requests.get(url=url,params=data,cookies=cookies)
        return self.callback(res)

    def callback(self, res):
        # if (res.status_code == 200):
        #     return res.json()
        # else:
        return res

    def run_main(self,method,url,data=None,cookies=None,header=None):
        res = None
        if method =='post':
            res = self.post_main(url,data,header,cookies)
        else:
            res =self.get_main(url,data,header,cookies)
        return res

