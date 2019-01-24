import requests
import re
from PIL import Image
import hashlib
from bs4 import BeautifulSoup
import os

class library():
    def __init__(self):
        self.s = requests.session()
        self.username = '你的学号'
        password = '你的密码'
        hl = hashlib.md5()  # MD5加密
        hl.update(password.encode(encoding='utf-8'))
        self.password = hl.hexdigest()

    def login(self):
        r = self.s.get('http://cas.upc.edu.cn/cas/login')
        ltt = re.findall('<input type="hidden" name="lt" value="(.*?)">', r.text, re.S)[0]
        lt = re.findall('(.*?)" />', ltt, re.S)[0]
        data = {
            'username': self.username,
            'password': self.password,
            'encodedService': 'http%3a%2f%2fi.upc.edu.cn',
            'service': 'http://i.upc.edu.cn',
            'lt': lt
        }
        url = 'http://cas.upc.edu.cn/cas/login'
        req = self.s.post(url, data=data)
        r = self.s.get('http://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=home')
        r = re.findall('<a href="(.*?)">', r.text, re.S)[0]
        r = self.s.get(r)
        self.s.get('http://i.upc.edu.cn/dcp/forward.action?path=dcp/core/appstore/menu/jsp/redirect&appid=1186&ac=1')
        req = self.s.get('http://211.87.177.4/reader/book_lst.php')
        soup = BeautifulSoup(req.text, "lxml")
        table = soup.find(width="100%")
        tr = table.find_all("tr")
        try:
            temp = 0
            for t in tr:
                if(temp):
                    book = t.find(attrs="blue")
                    title = t.find(title="renew")
                    print(book.string)
                    onclick = title.get("onclick", "")
                    self.bar_code = onclick[10:18]
                    self.check = onclick[21:29]
                    self.captcha()
                temp += 1
        except Exception as e:
            print(e)


    def captcha(self):
        # 下载验证码
        with open('captcha.jpg', 'wb') as f:
            f.write(self.s.get('http://211.87.177.4/reader/captcha.php').content)
        img = Image.open('captcha.jpg')
        img.show()
        # 手动输入验证码
        captcha_code = input('输入验证码>>')
        # 自动识别验证码
        # captcha_code = self.recognize_captcha().strip()
        url = 'http://211.87.177.4/reader/ajax_renew.php?bar_code=' + self.bar_code + '&check=' + self.check + '&captcha=' + captcha_code
        r = self.s.get(url)
        if r.text.find('green'):
            print("续借成功ヾ(≧▽≦*)o")
        else:
            print("续借失败╥﹏╥...")

if __name__ == '__main__':
    run = library()
    run.login()
    run.captcha()
    os.remove('captcha.jpg')
