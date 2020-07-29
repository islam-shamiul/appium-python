from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = ('C:/Users/Himu/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[
                     ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
print("Text on the button :", ele_id.text)
print("Text on the button :", ele_id.get_attribute("name"))
ele_id.click()

ele_classname = wait.until(
    lambda x: x.find_element_by_class_name("android.widget.EditText"))


ele_classname.send_keys("Hello World")
time.sleep(2)
ele_classname.clear()
