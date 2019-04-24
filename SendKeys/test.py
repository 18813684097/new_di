from page.login import WebTools
from selenium import webdriver


def login_test():
    browers = webdriver.firefox()


    WebTools.wait(5)
login_test()