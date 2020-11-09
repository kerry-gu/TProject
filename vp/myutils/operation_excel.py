#coding:utf-8
import xlrd


class OperationExcel(object):
     
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
             self.file_name=file_name
             self.sheet_id = sheet_id
        else:
             self.file_name='../dataconfig/case1.xls'
             self.sheet_id=0
        # self.data=self.get_data()

    # 获取sheet内容
    def get_data(self):
        self.data = xlrd.open_workbook(self.file_name)
        tables = self.data.sheets()[self.sheet_id]
        return tables
    
    # 获取单元格行数
    
    def get_lines(self):
        tables = self.data
        return tables.nrows

    
    # 获取某个单元格内容
    
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    
    # 写入数据
    
    def write_value(self,roe,col,value):
        read_data= xlrd.open_workbook(self.file_name)
        write_data= copy(read_data)
        sheet_data= write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    
    # 根据对应的caseid 找到对应行的内容
    
    def get_rows_data(self,case_id):
        row_num=self.get_row_num(case_id)
        rows_data=self.get_row_values(row_num)
        return rows_data

    
    # 根据对应的caseid 找到对应行的行号
    
    def get_row_num(self,case_id):
        num=0
        clols_data=self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num 
            num =num +1 

    
    # 根据行号，找到该行的内容
    
    def get_row_values(self,row):
        table=self.data
        row_data=table.row_values(row)
        return row_data
    
    # 获取某一列的内容
    
    def get_cols_data(self,col_id=None):
        print (self.data)
        if col_id !=None:
            cols=self.data.col_value(col_id)
        else:
            cols=self.data.col_value(0)
        return cols       






