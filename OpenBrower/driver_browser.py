from selenium import  webdriver
import  unittest
from time import sleep
class Login(unittest.TestCase):
    def OpenBrower(self):
       webdriver_handle = webdriver.Chrome()
       webdriver_handle.maximize_window()
       return webdriver_handle
