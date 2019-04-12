import time 
import sys
import os

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 


IS_FIREFOX = True

if IS_FIREFOX:
    # os.environ['MOZ_HEADLESS'] = '1'
    print("oo")
    profile = webdriver.FirefoxProfile('/home/rohit/.mozilla/firefox/yta7s61l.default')
    driver = webdriver.Firefox(executable_path='./geckodriver',firefox_profile=profile)
   # driver = webdriver.Firefox(executable_path='/home/rohit/geckodriver')
else:
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=/home/sirius0027/.config/\
google-chrome/')
    options.headless = True
    driver = webdriver.Chrome(executable_path = '/home/rohit/chromedriver',
                              options = options)

driver.implicitly_wait(60)
target = sys.argv[1]
message = sys.argv[2]
try:
    driver.get("https://web.whatsapp.com/")
    x_arg = '//span[@title="{}"]'.format(target)
    for i in range(10):
        title = driver.find_element_by_xpath(x_arg)
    title.click()

    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(5)

    # To send attachments
        # click to add
        driver.find_element_by_css_selector('span[data-icon="clip"]').click()
        # add file to send by file path
        driver.find_element_by_css_selector('input[type="file"]').sendKeys('./demo.png')
        # click to send
        driver.find_element_by_css_selector('span[data-icon="send-light"]').click()
        

except Exception as e:
    f = open("error.log", "a")
    print("Error Occured.\n Check the error.log file")
    f.write(str(e))
    f.close()
#finally:
  #  driver.close()
