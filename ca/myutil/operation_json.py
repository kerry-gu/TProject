#coding:utf-8
import json

class OperationJson():

    def __init__(self):
        self.data =self.read_json()
    def read_json(self):
        with open('D:/github/ca/dataconfig/data.json') as fp:
            data = json.load(fp)
            return data

    def get_json(self,id):
        return self.data[id]

# if __name__=='__main__':
#     op = OperationJson()
#     print(op.get_json('a'))
a = OperationJson()
print (a.get_json("a"))
