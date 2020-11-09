class Sql():
        
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