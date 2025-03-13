from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get("http://localhost:8000/login.html")

    # Find elements and perform actions
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys("testuser")
    password.send_keys("password123")
    login_button.click()

    # Wait for alert and verify
    time.sleep(2)
    alert = driver.switch_to.alert
    assert alert.text == "Login successful!"
    alert.accept()

finally:
    # Close the browser
    driver.quit()