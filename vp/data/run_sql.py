#coding:utf-8
import sys
sys.path.append('../..')

from myutils.con_mysql import C_mysql

class exrun(object):
    def __init__(self):
        print('init runsql')

    def createtable(self):
        with open ('dataconfig/create.sql',encoding='utf8',mode='r')as f:
            print('drop & create table')
            sql_list=f.read().split(';')
            mysql = C_mysql()
            for x in sql_list:
                if(x is not None):
                    print(x)
                    sql_item=x+';'
                    print(sql_item)
                    a = mysql.exrunsql(sql_item)
                    print(a)
            mysql.close()

    def insert(self):
        with open ('dataconfig/inster.sql',encoding='utf8',mode='r')as f:
            sql_list=f.read().split(';')
            mysql = C_mysql()
            for x in sql_list:
                if(x is not None):
                    sql_item=x+';'
                    print('sql_item')
                    a = mysql.exrunsql(sql_item)
                    print(a)
            mysql.close()
