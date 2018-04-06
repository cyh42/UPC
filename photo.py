import requests

url = 'http://jwxt.upc.edu.cn/jwxt/uploadfile/studentphoto/pic/'

for year in range(14, 18):
    for yuan in range(4,5):
        for zhuanye in range(1,6):
            for bj in range(1, 5):
                for i in range(1, 31):
                    if i < 10:
                        xuehao = str(year) +  '0' + str(yuan) + '0' + str(zhuanye) + '0' + str(bj) + '0' +str(i)
                        student_url = url + xuehao + '.JPG'
                        with open('E:/student_img/%s.jpg' % xuehao, 'wb') as file:
                            file.write(requests.get(student_url).content)
                    else:
                        xuehao = str(year) + '0' + str(yuan) + '0' + str(zhuanye) + '0' + str(bj) + str(i)
                        student_url = url + xuehao + '.JPG'
                        with open('E:/student_img/%s.jpg' % xuehao, 'wb') as file:
                            file.write(requests.get(student_url).content)

print('OK!')