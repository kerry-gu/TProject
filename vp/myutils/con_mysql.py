#coding:utf-8
import pymysql.cursors
class C_mysql(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='gkl',
            password='123456',
            db='srs',
            charset='utf8')
        self.cur=self.conn.cursor()
        
    def exrunsql(self, sql):
        self.cur.execute(sql)
        r = self.conn.commit()
        return r

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def close(self):
        self.cur.close()
        self.conn.close()
    
# dbmy = Conn_mysql()
# cur = conn.cursor()
# cur.execute("SELECT * FROM ALM_POSITION_CURRENT")
# print (cur.fetchone())

# db = pymysql.connect(host='127.0.0.1',
#              port=3306,
#              user='gkl',
#              password='123456',
#              db='srs',
#              charset='utf8' )
# cursor = db.cursor()
# cursor.execute("SELECT * FROM auto_test_almcoa_tr")
# data = cursor.fetchone() 
# print (data)
# db.close()