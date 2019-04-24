from selenium import webdriver
from time import sleep
from hanlde.element import *

url = 'https://lingxi.di-an.com'
account = '132'
pwd = '123'

def webdriverChrome(url) :
    driver = webdriver.Chrome()
    print('启动浏览器')
    driver.maximize_window()
    print('最大化窗口')
    driver.get(url)
    print('打开链接')
    sleep(15)
    print('等待完成15秒')
    print('进入输入')
    driver.find_element_by_id('account').clear()
    driver.find_element_by_id('account').send_keys(account)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(pwd)
    print('进行登录')
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/form/div[3]/div/div/span/button").click()
    print('进入等待')
    try:
        driver.find_elements_by_link_text('账号密码错误')
        print('账号密码错误')
    except:
        print('账号密码正确')
    sleep(15)
    # driver.quit()
webdriverChrome(url)