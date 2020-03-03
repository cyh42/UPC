from selenium import webdriver
import time

# 请先下载Edge WebDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
driver = webdriver.Edge()
url = 'https://app.upc.edu.cn/ncov/wap/default/index'
driver.get(url)

try:
    # 登录
    username = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input')
    username.send_keys('你的学号')
    psw = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input')
    psw.send_keys('你的密码')
    login = driver.find_element_by_xpath('//*[@id="app"]/div[3]')
    login.click()
    time.sleep(5)
    # 定位
    ip = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[6]/div/input')
    ip.click()
    time.sleep(2)
    btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a')
    btn.click()
    # 二次确认
    btn_ok = driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]')
    btn_ok.click()
    print('签到成功！')
except Exception as e:
    print(e)
