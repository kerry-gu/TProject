import sys
sys.path.append('..')

from utils.WebCrawling import WebCrawling

class lmain():
    def __init__(self):
        url ='https://www.rwtext.com/default.asp'
        self.H = WebCrawling(url)
    
    def findlabel(self, labels): 
        web = self.H.loadWeb()
        getlabel = web.select(labels)
        for li in getlabel:
            print(li.string)

if __name__ == "__main__":
    a = lmain().findlabel('div#main tr td a')
