from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

link = browser.find_element("link text","Sign in")
link.click()
login_box = browser.find_element("By.ID","login_field")
login_box.send_keys("awaissaddiqui")
