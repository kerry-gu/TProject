import sys
import allure
sys.path.append('..')

from utils.WebCrawling import WebCrawling

class lmain():
    def __init__(self):
        url ='http://www.airkx.com/'
        self.H = WebCrawling(url)
    
    def findlabel(self, labels): 
        web = self.H.loadWeb()
        getlabel = web.select(labels)
        t = web.find(labels)
        print(t)
        for li in getlabel:
            print(li.get('src'))

if __name__ == "__main__":
    a = lmain().findlabel('div.hzhb-box div.swiper-container div.com-logo[0]')
