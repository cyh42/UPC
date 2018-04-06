import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import lxml
from prettytable import PrettyTable
import getpass
import  sys
sys.setrecursionlimit(1000000) #解决递归限制

userName = input("输入你的数字石大账户：")
passWord = getpass.getpass("输入你的数字石大密码：")

x = PrettyTable(["开课学期", "课程名称", "总成绩", "课程类别", "学分"])
allScore = []

def fillScoreList(soup):
    data =soup.find_all('tr')
    for tr in data:
        singleScore = []
        ltd = tr.find_all('td')
        #print(len(ltd))
        if len(ltd) != 13:
            continue
        for td in ltd:
            singleScore.append(td.string)
            #print(td.string)
        allScore.append(singleScore)

def printScoreList(num):
    for i in range(num):
        u=allScore[i]
        x.add_row([u[3], u[4], u[5], u[8], u[10]])

def getHeaders(temp_data=''):
    headers = {
        'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Connection': 'Keep-Alive',
        'Cookie': 'JSESSIONID = 2EA76D6527A2CE5362A29C5CCB31648A',
        'Host': 'jwxt.upc.edu.cn',
        'Referer': 'http://jwxt.upc.edu.cn/jwxt/',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; LCTE)'
    }
    return headers

image_pic = 'http://jwxt.upc.edu.cn/jwxt/verifycode.servlet'
with open('verify.png', 'wb') as f:
    f.write(urllib.request.urlopen(urllib.request.Request(url=image_pic, headers=getHeaders())).read())

verify = input('Please input verify:')
post_url = 'http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logon'
post_data = {
    'PASSWORD': passWord,
    'RANDOMCODE': verify,
    'useDogCode': '',
    'useDogCode': '',
    'USERNAME': userName,
    'x': '47',
    'y': '6'
}

#print(urllib.request.urlopen(urllib.request.Request(url=post_url,data=urllib.parse.urlencode(post_data).encode('utf-8') ,headers=getHeaders())).read().decode('utf-8'))

def getHeaders1(temp_data=''):
    headers1 = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Connection': 'Keep-Alive',
        'Cookie': 'JSESSIONID = EFC28E6AE2A0F43A6477566850DE0649',
        'Host': 'jwxt.upc.edu.cn',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; LCTE)'
    }
    return headers1

post_url1 = 'http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj'

#print(urllib.request.urlopen(urllib.request.Request(url=post_url1 ,headers=getHeaders1())).read().decode('utf-8'))
r = urllib.request.urlopen(urllib.request.Request(url=post_url1, headers=getHeaders1())).read().decode('utf-8')

soup = BeautifulSoup(r, "lxml")
fillScoreList(soup)
#print(soup.find_all('td', {'title': '蔡宇航'}))
#print(allScore[0])
#print(allScore[8][4])

def getHeaders2(temp_data=''):
    headers2 = {
        'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
		'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
		'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID = EFC28E6AE2A0F43A6477566850DE0649',
        'Host': 'jwxt.upc.edu.cn',
		'Referer': 'http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; LCTE)'
    }
    return headers2

for i in range (2,5):
    try:
        post_data2 = {
           'PageNum': i,
        }
        #print(urllib.request.urlopen(urllib.request.Request(url=post_url1 ,data=urllib.parse.urlencode(post_data2).encode('utf-8'),headers=getHeaders1())).read().decode('utf-8'))
        r = urllib.request.urlopen(urllib.request.Request(url=post_url1, data=urllib.parse.urlencode(post_data2).encode('utf-8'), headers=getHeaders1())).read().decode('utf-8')
        soup = BeautifulSoup(r, "lxml")
        #print(soup)
        fillScoreList(soup)
    except:
        continue

print(len(allScore))
printScoreList(len(allScore))
print(x)