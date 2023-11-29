from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.tezo.com")

element = driver.find_element("css selector", "h2")
print("Version 3: " + element.text)

driver.quit()
