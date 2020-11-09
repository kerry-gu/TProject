import cx_Oracle as cx
import json

class Operation_Oracle:

    def __init__(self):
        self.conn = cx.connect('kp20200217','kp123456','192.168.13.125:1521/ORCL'))
        self.cur=self.conn.cursor()

    def search_one(self,sql):
        self.cur.execute(sql)
        result=self.cur.fetchone()
        result=json.dumps(result)
        return result

    def exrunsql(self):
        self.cur.execute(sql)
        r