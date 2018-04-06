from selenium import webdriver
import time
import getpass
from selenium.webdriver.support.ui import Select

userName = input("输入你的数字石大账号：")
passWord = getpass.getpass("输入你的数字石大密码：")
service = input("输入开课时间：0:全部成绩，1:2017-2018-2，2:2017-2018-1，3:2016-2017-3，4:2016-2017-2，5:2016-2017-1：")

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
elem = browser.find_element_by_xpath("//*[@id='appMenuWidget-content']/div/div[5]/span")
elem.click()

time.sleep(2)
elem = browser.find_element_by_xpath("//*[@id='appMenuWidget-content']/div/div[6]/ul/li[2]")
elem.click()

time.sleep(2)
windows = browser.window_handles
browser.switch_to.window(windows[1])
browser.close()
browser.switch_to.window(windows[0])
browser.get('http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logonBySSO')
time.sleep(2)
browser.get('http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj')

elem = browser.find_element_by_xpath("//*[@id='tblHeadDiv']").text
print(elem)

#全部成绩
if service == '0':
    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("//*[@id='PageNavigation']/a[1]")
    elem.click()

    time.sleep(5)
    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("//*[@id='PageNavigation']/a[3]")
    elem.click()

    time.sleep(5)
    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("//*[@id='PageNavigation']/a[3]")
    elem.click()

    time.sleep(5)
    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)

    elem = browser.find_element_by_xpath("/html/body/font[2]").text
    print(elem)

#开课时间
if service == '1':
    #返回
    elem = browser.find_element_by_xpath("// *[ @ id = 'tbTable'] / tbody / tr[1] / td / a[1]")
    elem.click()

    s1 = Select(browser.find_element_by_name('kksj'))  # 实例化Select
    s1.select_by_value("2017-2018-2")  # 选择value="o2"的项
    elem = browser.find_element_by_xpath("//*[@id='search_values']/tbody/tr[5]/td/input")
    elem.click()

    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)

    elem = browser.find_element_by_xpath("/html/body/font[2]").text
    print(elem)

if service == '2':
    #返回
    elem = browser.find_element_by_xpath("// *[ @ id = 'tbTable'] / tbody / tr[1] / td / a[1]")
    elem.click()

    s1 = Select(browser.find_element_by_name('kksj'))  # 实例化Select
    s1.select_by_value("2017-2018-1")  # 选择value="o2"的项
    elem = browser.find_element_by_xpath("//*[@id='search_values']/tbody/tr[5]/td/input")
    elem.click()

    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("//*[@id='PageNavigation']/a[1]")
    elem.click()

    time.sleep(5)
    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)

    elem = browser.find_element_by_xpath("/html/body/font[2]").text
    print(elem)

if service == '3':
    #返回
    elem = browser.find_element_by_xpath("// *[ @ id = 'tbTable'] / tbody / tr[1] / td / a[1]")
    elem.click()

    s1 = Select(browser.find_element_by_name('kksj'))  # 实例化Select
    s1.select_by_value("2016-2017-3")  # 选择value="o2"的项
    elem = browser.find_element_by_xpath("//*[@id='search_values']/tbody/tr[5]/td/input")
    elem.click()

    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("/html/body/font[2]").text
    print(elem)

if service == '4':
    #返回
    elem = browser.find_element_by_xpath("// *[ @ id = 'tbTable'] / tbody / tr[1] / td / a[1]")
    elem.click()

    s1 = Select(browser.find_element_by_name('kksj'))  # 实例化Select
    s1.select_by_value("2016-2017-2")  # 选择value="o2"的项
    elem = browser.find_element_by_xpath("//*[@id='search_values']/tbody/tr[5]/td/input")
    elem.click()

    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("//*[@id='PageNavigation']/a[1]")
    elem.click()

    time.sleep(5)
    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("/html/body/font[2]").text
    print(elem)

if service == '5':
    #返回
    elem = browser.find_element_by_xpath("// *[ @ id = 'tbTable'] / tbody / tr[1] / td / a[1]")
    elem.click()

    s1 = Select(browser.find_element_by_name('kksj'))  # 实例化Select
    s1.select_by_value("2016-2017-1")  # 选择value="o2"的项
    elem = browser.find_element_by_xpath("//*[@id='search_values']/tbody/tr[5]/td/input")
    elem.click()

    elem = browser.find_element_by_xpath("//*[@id='mxh']/tbody").text
    print(elem)
    elem = browser.find_element_by_xpath("/html/body/font[2]").text
    print(elem)

#print("查询完毕！")