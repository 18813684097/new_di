from selenium import webdriver

l_name = ''
l_pwd = ''
url = ''
class login_in(object):
    def login(self):
        d = webdriver.chrome()
        d.get(url)
        d.maximize_window()
