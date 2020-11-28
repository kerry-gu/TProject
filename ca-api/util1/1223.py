class Datas:
    _class = {}
    def set(self, a):
        self._class = a

    def get(self):
        return self._class
    

d=Datas()

def test1(a1):
    d.set('2222')
    fn(1)

def fn(v):
    d.set({
        'code': 200,
        'data': {
            'realName': 'gu'
        }
    })
    fn2()

def fn2():
    f = d.get()
    _z = {
        'a': 'gu1',
        'b': f['data']['realName']
    }
    print(_z)

def test2(a1):
    f = d.get()
    _z = {
        'a': 'gu1',
        'b': f['data']['realName']
    }
    print(_z)

if __name__ == "__main__":
    pytest.main(['-s','test_t1.py'])