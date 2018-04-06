from selenium import webdriver
import time
import getpass
from selenium.webdriver.support.ui import Select

userName = input("输入你的数字石大账号：")
passWord = getpass.getpass("输入你的数字石大密码：")

browser = webdriver.Chrome()
browser.get('http://cas.upc.edu.cn/cas/login?service=http%3A%2F%2Fi.upc.edu.cn%2Fdcp%2Findex.jsp')

elem = browser.find_element_by_name("username")
elem.send_keys(userName)
elem = browser.find_element_by_name("password")
elem.click()
elem.send_keys(passWord)

elem = browser.find_element_by_xpath("//*[@id='login_form']/span/input")
elem.click()

time.sleep(2)
elem = browser.find_element_by_xpath("//*[@id='yiban']/span[2]")
elem.click()
time.sleep(2)

windows = browser.window_handles
browser.switch_to.window(windows[1])
browser.close()
browser.switch_to.window(windows[0])
browser.get('http://www.yiban.cn/t/index/')
elem = browser.find_element_by_xpath("//*[@id='4481']")
elem.click()

#重新开始
time.sleep(2)
elem = browser.find_element_by_xpath("//*[@id='Alert']/div[1]/div[2]/button[1]")
elem.click()

while True:
    elem = browser.find_element_by_xpath("//*[@id='questions']/div[1]").text
    print(elem)
    elem = browser.find_element_by_xpath("//*[@id='checkAnalyze']")
    elem.click()

    #inputs = browser.find_elements_by_xpath('//*[@id="questions"]/div[2]/div[1]')
    inputs = browser.find_elements_by_class_name('ok_cur')
    for input in inputs:
        print(input.text)

    elem = browser.find_element_by_xpath("//*[@id='pTool']/div[2]/a[2]")
    elem.click()
