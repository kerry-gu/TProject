from data.load_data_run_sql import DataToSql
# from data.run_sql import exrun
# from data.r_adi import DataToapi
import json


class main(object):
    def __init__(self):
        print('----init----main')
        # self.runs = exrun()
        self.runs = DataToSql()

    def exc(self):
        self.runs.createtable()
        self.runs.insert()

    def excelsql(self):
        self.runs.loadExcelData()

    def test(self):
        m = '{0[0]},{0[1]}'
        print('{0[' + str(12) + ']}')

    def api(self):
        a = DataToapi()
        self.url = a.col_excels(1,2)
        self.me_thod =a.col_excels(1,4)
        self.cookies =a.col_excels(1,5)
        self.parm_a = a.datatojson(a.col_excels(1,6))

    # def run_api(self):
        
c = main()
c.excelsql()