#coding:utf-8
import sys
sys.path.append('../..')

# from myutils.con_mysql import C_mysql
from myutils.con_sqlserver import SQLServers
from myutils.operation_excel import OperationExcel
# from xlrd import xldate_as_datetime
# 操作excle文档 拼接sql在数据库执行
class DataToSql(object):
    def __init__(self):
        print('-------init DataToSql-----')

    def loadExcelData(self):
        print('-------loadExcelData---------')
        # 实例化OperationExcel类 传入参数：文件名 sheet_id 
        excels = OperationExcel('dataconfig/api.xlsx', 1)
        # 调用类方法 获取sheet页数据
        sheetData = excels.get_data()
        
        rowdatas = []
        # 实例化mysql类
        # mysql = C_mysql()
        # 实例化sqlserver
        mssql =SQLServers()
        # 遍历行
        for a in range(sheetData.nrows):  #  for a in range(1,sheetData.nrows):

            #获取sheet页的有数据的总列数赋值colnum
            colnum = sheetData.ncols
            # 跳过表头
            if a > 0: 
                # 拼接sql
                sql = 'INSERT INTO AUTO_TEST_ALMCOA_TR VALUES ('
                # 遍历列
                for i in range(colnum):
                    if i==colnum-1:
                        sql += "'{0["+str(i)+"]}'" # sql = sql + '{0["+str(i)+"]}' #  {0[2]}
                    else:
                        sql += "'{0["+str(i)+"]}',"
                # sql = " INSERT INTO AUTO_TEST_ALMCOA_TR VALUES ('{0["+str(i)+"]}','{0["+str(i)+"]}','{0["+str(i)+"]}' "    缺失右括号)  
                sql += ')'  # sql = sql +")"
                # 获取某行所有单元格数据
                rowdatas = sheetData.row_values(a)
                sql = sql.format(rowdatas)
                # print(sql)
                result = mssql.exrunsql(sql)
                # print(result)
        return 1111111       
    # 直接执行sql文件
    def insert(self):
        with open ('dataconfig/inster.sql',encoding='utf8',mode='r')as f:
            sql_list=f.read().split(';')
            mysql = C_mysql()
            try:
                for x in sql_list:
                    if(x is not None):
                        sql_item=x+';'
                        print('sql_item')
                        a = mysql.exrunsql(sql_item)
                        print(a)
            except IOError:
                print('执行失败')
            else:
                mysql.close()

if __name__ =="__main__":
    run=DataToSql()
    print(run)