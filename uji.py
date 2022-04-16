from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\\bin\\chromedriver.exe")
driver.get("https://syncnau.poltektegal.ac.id/login")
print(driver.title)
username = driver.find_element_by_name("username")
username.clear()
username.send_keys("19090057")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("diisipasswordnt")
password.send_keys(Keys.RETURN)
print(driver.current_url)
