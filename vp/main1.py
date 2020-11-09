import sys
sys.path.append('../..')
from data.r_adi import DataToapi
from data.load_data_run_sql import DataToSql
import requests
from myutils.run_method import RunMethod
import json

class main(object):
    def __init__(self):
        # self.a = DataToapi()
        # self.cookie = {}
        print('----init----main')
        run=DataToSql().loadExcelData()
        # print('--------------------')
        print(run)

    def get_cookieT(self):
        res = self.run_api(2)
        cookies = res.cookies #requests.utils.dict_from_cookiejar(res.cookies)
        for item in cookies:
            # if item.name == 'index_cookiename_username':
            self.cookie[item.name] = item.value
        print(self.cookie)

    def api(self,row):
        iscookie=self.a.col_excels(row,5)
        print(iscookie =='是')
        if iscookie =='是':
            self.get_cookieT()
        self.url =self.a.col_excels(row,2)
        self.method=self.a.col_excels(row,3)
        self.datas = self.a.col_excels(row,4)
        if '{' in self.datas:
            self.datas =self.a.datatojson(self.datas)
        print(self.datas)

    def run_api(self,r):
        self.api(r)
        res = RunMethod().run_main(self.method,self.url,self.datas,self.cookie)
        print(res.json())
        return res

c=main()
# c.run_api(2)
# c.run_api(5)
# c.run_api(3)
# c.run_api(4)

