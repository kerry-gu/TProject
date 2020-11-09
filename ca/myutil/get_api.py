import requests
from bs4 import BeautifulSoup

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
url =('https://www.rwtext.com/default.asp')
r=requests.get(url,headers=header)
r.encoding = r.apparent_encoding
text = r.text
soup = BeautifulSoup(text,'html.parser')

print (soup.find('td').string)

for i in soup.select('tr td a',limit=60):
    print(i.string)

# class Getapi():

#     def 