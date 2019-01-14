import requests
import re
import hashlib
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys

sys.setrecursionlimit(1000000)  # 解决递归限制
allScore = []
x = PrettyTable(["开课学期", "课程名称", "总成绩", "课程类别", "学分"])

def fillScoreList(soup):
    data = soup.find_all('tr')
    for tr in data:
        singleScore = []
        ltd = tr.find_all('td')
        if len(ltd) != 13:
            continue
        for td in ltd:
            singleScore.append(td.string)
        allScore.append(singleScore)


def printScoreList(num):
    for i in range(num):
        u = allScore[i]
        x.add_row([u[3], u[4], u[5], u[8], u[10]])

s = requests.session()
r = s.get('http://cas.upc.edu.cn/cas/login')
ltt = re.findall('<input type="hidden" name="lt" value="(.*?)">', r.text, re.S)[0]
lt = re.findall('(.*?)" />', ltt, re.S)[0]
password = '你的密码'
hl = hashlib.md5() # MD5加密
hl.update(password.encode(encoding='utf-8'))
password = hl.hexdigest()
payload = {
    'username': '你的学号',
    'password': password,
    'encodedService': 'http%3a%2f%2fi.upc.edu.cn',
    'service': 'http://i.upc.edu.cn',
    'lt': lt
}
postMessage = s.post('http://cas.upc.edu.cn/cas/login', data=payload)
r = s.get('http://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=home')
r = re.findall('<a href="(.*?)">', r.text, re.S)[0]
r = s.get(r)
r.encoding = 'utf-8'
r = s.get('http://i.upc.edu.cn/dcp/forward.action?path=dcp/core/appstore/menu/jsp/redirect&appid=1180&ac=3')
r = s.get('http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logonBySSO')
r = s.post('http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj', data = {'kksj': '2018-2019-1'})
soup = BeautifulSoup(r.text, "lxml")
fillScoreList(soup)
printScoreList(len(allScore))
print(x)
input()
