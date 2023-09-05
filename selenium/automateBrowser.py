from selenium import webdriver
# from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/driver/chromedriver')
browser.get("https://github.com")
link = browser.find_elements("By.LINK_TEXT","Sign in")
link.click()
# login_box = browser.find_elements( "By.LINK_TEXT","login_field")
# login_box.send_keys("awaissaddiqui")
