from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.tezo.com")

element = driver.find_element("css selector", "h2")
print("Content from h1 tag" + element.text)

driver.quit()
