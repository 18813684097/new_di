from selenium import webdriver
def webdriverChrome(url) :
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(60)
    driver.quit()
webdriverChrome('https://lingxi.di-an.com')