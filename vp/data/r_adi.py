import sys
sys.path.append('..')

from myutils.operation_excel import OperationExcel as ex
import xlrd
import json

class DataToapi(object):
    #获取表格和sheet页
    def __init__(self):
        print('-------init DataToapi-----')
        self.sheet = ex('dataconfig/api.xlsx',0)
        self.table = self.sheet.get_data()    

    def loadExcleapi(self):
        print('------loadExcleapi--------')    
    
    #获取行
    def r_excels(self,row):
        rowonedata = self.table.row_values(row)
        return rowonedata
   
    #获取某单元格
    def col_excels(self,row,col):
        self.row =row
        self.col = col
        colonedata = self.table.cell_value(row,col)
        return colonedata
    
    #转换json
    def datatojson(self, _json):
        return json.loads(_json)


        

        



    
