from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = ('C:/Users/Himu/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn1"]')
# ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')  - Using Xpath_and id
# ele_xapth = driver.find_element_by_xpath('//android.widget.Button[2]')  - Using Xpath_and index
# ele_xapth = driver.find_element_by_xpath('//android.widget.Button[@text="ScrollView"]')  - Using Xpath_and text
ele_xapth = driver.find_element_by_xpath(
    '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
ele_xapth.click()
time.sleep(2)
# - Using Xpath_and className
driver.find_element_by_xpath(
    '//android.widget.EditText').send_keys("Code2Lead")


time.sleep(2)
driver.quit()
