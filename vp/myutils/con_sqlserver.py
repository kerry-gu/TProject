import pymssql

class SQLServers(object):

    def __init__(self):
        self.conn = pymssql.connect(
            server='(local)',
            port=1433,
            user='sa',
            password='12345678',
            database='pythontest'
        )
        if self.conn:
            print('连接成功')
        self.cur =self.conn.cursor()


# if __name__=="__main__":
#     c=SQLServers()
#     con=c.conn()
    def exrunsql(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        self.close()
        # self.query()

    def query(self, sql):
        self.cur.execute(sql)
        _data = self.cur.fetchone()
        self.close()
        return _data

    def close(self):
        self.cur.close()
        self.conn.close() 