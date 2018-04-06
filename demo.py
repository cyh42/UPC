import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import webbrowser
import time
from PIL import ImageGrab

text = open('Path.txt').read( )
chromePath = text
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))#这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
webbrowser.get('chrome').open_new('http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logon')
time.sleep(10)
webbrowser.get('chrome').open_new('http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logonBySSO')
time.sleep(1)
webbrowser.get('chrome').open_new('http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj')
for i in range(10):
    time.sleep(5)
    im = ImageGrab.grab()
    im.save('test.txt','jpeg')

    msg_from = '931282603@qq.com'  # 发送方邮箱
    passwd = 'krlbraovzmvibcfh'  # 填入发送方邮箱的授权码
    msg_to = '931282603@qq.com'  # 收件人邮箱

    message = MIMEMultipart()
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, message.as_string())
    finally:
        s.quit()


