from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com")
driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("Nested Frames").click()
# switch to frame with name
driver.switch_to.frame("frame-bottom")
# identify element and get text method
s = driver.find_element_by_xpath("//body").text
print ("Test inside frame: " + s)
# move out of frame to parent page
driver.switch_to.default_content()
driver.quit()