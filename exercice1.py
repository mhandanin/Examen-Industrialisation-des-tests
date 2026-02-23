from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
btn.click()

success_message = driver.find_element(By.ID, "flash")
assert "You logged into a secure area!" in success_message.text
print(success_message.text)
time.sleep(15)
driver.close()