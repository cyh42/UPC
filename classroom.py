import urllib
import requests
from urllib.parse import urlparse
import json
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
d1 = datetime.date.today()
d2 = datetime.date(2018, 3, 4)
cha = (d1-d2).days + 1
week = int(cha/7)+1
day = cha%7

def Email(Emailstr, week, day):
    num = ['七', '一', '二', '三', '四', '五', '六']
    msg_from = '发送方邮箱'  # 发送方邮箱
    passwd = '发送方邮箱的授权码'  # 填入发送方邮箱的授权码
    msg_to = '收件人邮箱'  # 收件人邮箱

    message = MIMEMultipart()
    message['From'] = Header("sky", 'utf-8')
    message['To'] = Header("cyh", 'utf-8')
    subject = '第' + str(week) + '周星期' + str(num[day]) + '空闲教室'
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText(Emailstr, 'plain', 'utf-8'))
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, message.as_string())
    finally:
        s.quit()

s = requests.session()

payload = {'username': "你的学号", 'password':"你的数字石大密码"}
postMessage = s.post("https://zhxyapp.upc.edu.cn/wap/login/commit.html",data=payload)

course = 0
Emailstr = ''
for i in range(5):
    Emailstr = Emailstr + '第' + str(int(course/2+1)) + '大节\n'
    course = course + 2
    data = {
        'week': week,
        'day': day,
        'course': course
    }
    r = s.post("https://zhxyapp.upc.edu.cn/extensions/wap/clsroom/search.html",data=data)
    #print(r.text)

    sJOSN = r.text
    #print(sJOSN)
    sValue = json.loads(sJOSN)
    #print(sValue)

    tJOSN = ''
    for k in sValue.keys():
        if str(type(sValue[k]))!="<class 'dict'>":
            #print(k+':'+ str(sValue[k]))
            ''
        else:
            #print(str(k)+':')
            for k1 in sValue[k].keys():
                #print(str(sValue[k][k1]))
                tJOSN = str(sValue[k][k1])

    #print(tJOSN)

    tJOSN = re.sub('\'','\"',tJOSN)
    tValue = json.loads(tJOSN)
    #print(tValue)

    #print(Emailstr1)
    for k in tValue.keys():
        if str(type(tValue[k]))!="<class 'dict'>":
            #print(k+':'+ str(tValue[k]))
            Emailstr = Emailstr + k+':'+ str(tValue[k]) + '\n'
        else:
            print(str(k)+':')
            for k1 in sValue[k].keys():
                print(str(tValue[k][k1]))
                tJOSN = str(tValue[k][k1])
    Emailstr = Emailstr + '\n'
Email(Emailstr, week, day)
