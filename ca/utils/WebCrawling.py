from bs4 import BeautifulSoup
import requests


class WebCrawling():

    def __init__(self,url):
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
        self.url = url

    def loadWeb(self):
        string = requests.get(self.url,self.header)
        string.encoding =string.apparent_encoding
        htmldocument = BeautifulSoup(string.text,'html.parser')
        return htmldocument


        



        