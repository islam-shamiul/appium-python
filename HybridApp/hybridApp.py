from appium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = ('C:/Users/Himu/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'

# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# 3. Open the URL in Browser
ele = wait.until(lambda x: x.find_element_by_id(
    "com.android.chrome:id/terms_accept"))
ele.click()

ele2 = wait.until(lambda x: x.find_element_by_id(
    "com.android.chrome:id/next_button"))
ele2.click()

ele3 = wait.until(lambda x: x.find_element_by_id(
    "com.android.chrome:id/negative_button"))
ele3.click()

ele4 = wait.until(lambda x: x.find_element_by_id(
    "com.android.chrome:id/search_box_text"))
ele4.click()

ele5 = wait.until(lambda x: x.find_element_by_id(
    "com.android.chrome:id/url_bar"))
ele5.click()
ele5.send_keys("http://www.dummypoint.com/")

driver.press_keycode(66)

time.sleep(5)

# 4. Get the list of Contexts in App
appContexts = driver.contexts
print("AppContexts : ", appContexts)

# 5. switch to webview to perform action on Required URL or on WebView
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        print("In WebView")
        driver.switch_to.context(appType)

# 6. Do testing on Webview screen in chrome browser or any if we want

enterText = wait.until(lambda x: x.find_element_by_class_name("form-control"))
enterText.click()
enterText.send_keys("Code2Lead")

# 7. Switch back to native view to perform action
for appType in appContexts:
    if appType == "NATIVE_APP":
        print("In Native App")
        driver.switch_to.context(appType)

# 8. Do testing on native app screen if we want
ele5.click()
ele5.send_keys("http://www.kennisworld.com/")
driver.press_keycode(66)

# 9. Quit or close the driver object
time.sleep(10)
driver.quit()
