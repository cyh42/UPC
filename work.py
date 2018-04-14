import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys
import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Sheet 1')
sys.setrecursionlimit(1000000) #解决递归限制
x = PrettyTable(['姓名', '性别', '专业', '学历', '班级', '单位', '年度'])
worksheet.write(0, 0, label='姓名')
worksheet.write(0, 1, label='性别')
worksheet.write(0, 2, label='专业')
worksheet.write(0, 3, label='学历')
worksheet.write(0, 4, label='班级')
worksheet.write(0, 5, label='单位')
worksheet.write(0, 6, label='年度')
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return  r.text
    except:
        return ""
m = 1
for k in range(1, 90):
    url = "http://career.upc.edu.cn/index.php/index/index/allstulist/np/" + str(k) + "/major/%E6%9D%90%E6%96%99%E6%88%90%E5%9E%8B"
    r = requests.get(url)
    #print(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    tr = soup.find_all('tr')
    i = 0
    for td in tr:
        i = i + 1
        if (i > 1):
            t = td.find_all('td')
            x.add_row([t[0].string, t[1].string, t[2].string, t[3].string, t[4].string, t[5].string, t[6].string])
            for n in range(7):
                worksheet.write(m, n, label=t[n].string)
            m = m + 1

print(x)
workbook.save('材控专业历年毕业生就业去向.xls')