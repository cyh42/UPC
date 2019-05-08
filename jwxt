import cgi
import requests
import re
import hashlib
from bs4 import BeautifulSoup
import sys
import pandas as pd

print ("Content-type: text/html\n")
sys.setrecursionlimit(1000000)  # 解决递归限制
allScore = []
cnt = []
kcmc = []
result = []
xueqi = []
leibie = []
xuefen = []

def convertToHtml(result,title):
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

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
    print(allScore)
    for i in range(num):
        u = allScore[i]
        cnt.append(i+1)
        xueqi.append(u[1])
        kcmc.append(u[3])
        result.append(u[4])
        leibie.append(u[9])
        xuefen.append(u[5])

def cjcx(username, psw):
    allScore.clear()
    cnt.clear()
    kcmc.clear()
    result.clear()
    xueqi.clear()
    leibie.clear()
    xuefen.clear()
    s = requests.session()
    r = s.get('http://cas.upc.edu.cn/cas/login')
    ltt = re.findall('<input type="hidden" name="lt" value="(.*?)">', r.text, re.S)[0]
    lt = re.findall('(.*?)" />', ltt, re.S)[0]
    password = psw
    hl = hashlib.md5() #MD5加密
    hl.update(password.encode(encoding='utf-8'))
    password = hl.hexdigest()
    payload = {
        'username': username,
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
    r = re.findall('<a href="(.*?)">', r.text, re.S)[0]
    s.get(r)
    r = s.get('http://211.87.177.34/jsxsd/kscj/cjcx_list?kksj=2018-2019-2&kcxz=&kcmc=&xsfs=all')
    # print(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    fillScoreList(soup)
    printScoreList(len(allScore))
    title = [u'序号', u'开课学期', u'课程名称', u'成绩', u'课程类别', u'学分']
    return convertToHtml([cnt] + [xueqi] + [kcmc] + [result] + [leibie] + [xuefen], title)
