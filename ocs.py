from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ocs.ca")
input_day = driver.find_element_by_name("dob__day")
input_day.send_keys("02")
input_month = driver.find_element_by_name("dob__month")
input_month.send_keys("september")
input_year = driver.find_element_by_name("dob__year")
input_year.send_keys("1981")
driver.find_element_by_class_name("dob").submit()
driver.find_element_by_class_name("checkbox").click()
driver.find_element_by_class_name("overlay__navigation").submit()
#Need to Click START BROWSING BUTTON
#ids = driver.find_elements_by_xpath('//*[@id]')
#for ii in ids:
#    print("ID:")
#    print(ii.get_attribute('id'))
#    print("CLASS:")
#    print(ii.get_attribute('class'))
#    print("TEXT:")
#    print(ii.text)
#    print(dir(ii))
#    print("*************************************************")

driver.find_element_by_id("terms_confirm--flyout").submit()
driver.get("https://ocs.ca/collections/bottled-oils")

#rip contents
#check for NEXT PAGE BUTTON and Click
#if no button, done


#btn = driver.find_elements_by_xpath("//button[text()='Start Browsing']")
#dir(btn)
#vars(btn)
#type(btn)

#driver.quit()
