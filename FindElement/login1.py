import string

from selenium import webdriver

class findElement():
    text_id
    def FE_login(d,**arg):
        if text_id in arg:
            ele_login = get_ele_times(d, 10, lambda d:d.find_element_by_link_text(arg['text_id']))
        useEle = d.find_element_by_id(arg['userid'])
        pwdEle = d.find_element_by_id(arg['pwdid'])
        logEle = d.find_element_by_id(arg['loginid'])
        return useEle, pwdEle, logEle