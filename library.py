import datetime
from urllib import request
from urllib import parse
import urllib.parse
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys
from PIL import Image
import pytesser3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
time1 = time.time()
sys.setrecursionlimit(1000000) #解决递归限制

j = 0
fp = open("Cookie.txt", "a")
fp.close()
while(True):
    def Email(str):
        msg_from = '931282603@qq.com'  # 发送方邮箱
        passwd = 'krlbraovzmvibcfh'  # 填入发送方邮箱的授权码
        msg_to = '931282603@qq.com'  # 收件人邮箱

        message = MIMEMultipart()
        message['From'] = Header("sky", 'utf-8')
        message['To'] = Header("cyh", 'utf-8')
        subject = '借阅到期提醒'
        message['Subject'] = Header(subject, 'utf-8')
        # 邮件正文内容
        message.attach(MIMEText(str, 'plain', 'utf-8'))
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, message.as_string())
        finally:
            s.quit()

    def save_to_file(file_name, contents):
        fh = open(file_name, 'w')
        fh.write(contents)
        fh.close()

    Cookie = ''
    f = open("Cookie.txt")
    for line2 in f:
        Cookie = line2
        #print(line2)

    def getHeaders(ID = Cookie):
        headers = {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'Keep-Alive',
            'Cookie': ID,
            'Host': '211.87.177.4',
            'Referer': 'http://211.87.177.4/reader/redr_verify.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        return headers

    image_pic = 'http://211.87.177.4/reader/captcha.php?'
    image_data = urllib.request.urlopen(urllib.request.Request(url=image_pic, headers=getHeaders()))
    with open('verify.png', 'wb') as f:
        f.write(urllib.request.urlopen(urllib.request.Request(url=image_pic, headers=getHeaders())).read())

    l = image_data.headers["Set-Cookie"]
    #print(l)
    try:
        ID = l.split(";")[0]
        #print(ID)
        save_to_file('Cookie.txt', ID)
    except:
        ''

    j = j + 1
    book_lst = 'http://211.87.177.4/reader/book_lst.php'
    r = urllib.request.urlopen(urllib.request.Request(url=book_lst,headers=getHeaders(Cookie))).read().decode('utf-8')
    soup = BeautifulSoup(r, "lxml")
    info = soup.find_all('li')[10].string
    #print(info)
    if (info):
        verify = "1234"
    else:
        img = Image.open("verify.png")
        verify = pytesser3.image_to_string(img)
        verify = verify[0:4]
        print(verify)

    post_url = 'http://211.87.177.4/reader/redr_verify.php'
    post_data = {
        'number': '你的图书馆账号',
        'passwd': '你的图书馆密码',
        'captcha': verify,
        'select': 'cert_no',
        'returnUrl': ''
    }
    book_lst = 'http://211.87.177.4/reader/book_lst.php'
    #print(urllib.request.urlopen(urllib.request.Request(url=post_url, data=urllib.parse.urlencode(post_data).encode('utf-8'),headers=getHeaders(Cookie))).read().decode('utf-8'))
    s = urllib.request.urlopen(urllib.request.Request(url=post_url, data=urllib.parse.urlencode(post_data).encode('utf-8'),headers=getHeaders(Cookie))).read().decode('utf-8')
    r = urllib.request.urlopen(urllib.request.Request(url=book_lst, data=urllib.parse.urlencode(post_data).encode('utf-8'),headers=getHeaders(Cookie))).read().decode('utf-8')
    soup = BeautifulSoup(r, "lxml")
    info = soup.find_all('li')[10].string
    #print(info)
    if(info):
        x = PrettyTable(["书名", "借阅日期", "当前日期", "应还日期", "剩余天数"])
        table = soup.find(width="100%")
        tr = table.find_all("tr")
        i = 0
        for t in tr:
            i = i + 1
            if(i > 1):
                td = t.find_all("td")
                book = t.find(attrs="blue")
                future = td[3].string.replace(' ', '')
                now = datetime.datetime.now()
                now = now.strftime('%Y-%m-%d %H:%M:%S')
                d1 = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
                d2 = datetime.datetime.strptime(future, '%Y-%m-%d')
                delta = d2 - d1
                x.add_row([book.string, td[2].string, d1, d2, delta.days])
                if(delta.days < 10):
                    str = '《' + book.string + '》还有' +  str(delta.days) + '天就要到期了，记得续借哟！\n' + '应还日期' + str(d2)
                    print(str)
                    Email(str)

        print(x)
        input()
        break
    else:
        continue
