from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.tezo.com")

element = driver.find_element("css selector", "h2")
print("Text present in the h2 tag is " + element.text)

driver.quit()
