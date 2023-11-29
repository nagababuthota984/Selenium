from selenium import webdriver

webDriver= webdriver.Chrome()
webDriver.get("https://www.tezo.com")

element = webDriver.find_element("css selector", "h2")
print("123" + element.text)

webDriver.quit()
