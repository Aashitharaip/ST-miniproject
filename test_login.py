from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://www.demoblaze.com")
    
    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    # Enter valid credentials
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys("Aashitha")
    driver.find_element(By.ID, "loginpassword").send_keys("ash")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()

    # Verify successful login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logout2"))
    )
    print("Valid login successful")

def test_invalid_login(driver):
    driver.get("https://www.demoblaze.com")
    
    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    # Enter invalid credentials
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys("InvalidUser")
    driver.find_element(By.ID, "loginpassword").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()

    # Verify login failed
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login2"))
    )
    print("Invalid login test passed")

def test_login_with_empty_fields(driver):
    driver.get("https://www.demoblaze.com")
    
    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    # Attempt to login with empty fields
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='logIn()']"))
        ).click()
        # Check for alert
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_message = alert.text
        alert.accept()
        assert "Please fill out Username and Password" in alert_message
        print("Login with empty fields test passed")
    except Exception as e:
        print("Error during empty field login: ", e)
        assert False, "No alert message found for empty fields or other error."

def test_login_with_only_username(driver):
    driver.get("https://www.demoblaze.com")
    
    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    # Enter only username
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys("Aashitha")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()

    # Check if an alert is present
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_message = alert.text
        alert.accept()
        assert "Please fill out Username and Password" in alert_message
        print("Login with only username test passed")
    except Exception as e:
        print("No alert message found or other error.")
        print(e)
        assert False, "No alert message found for missing password."

def test_login_with_only_password(driver):
    driver.get("https://www.demoblaze.com")
    
    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    # Enter only password
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    ).send_keys("ash")

    # Click login button
    try:
        driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
        
        # Check for alert
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_message = alert.text
        alert.accept()
        assert "Please fill out Username and Password" in alert_message
        print("Login with only password test passed")
    except Exception as e:
        print("Error during login with only password: ", e)
        assert False, "No alert message found for missing username or element not interactable."

def test_login_alert_on_failed_login(driver):
    driver.get("https://www.demoblaze.com")
    
    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    # Enter invalid credentials and submit
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys("InvalidUser")
    driver.find_element(By.ID, "loginpassword").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()

    # Check for alert message
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_message = alert.text
        alert.accept()
        print(f"Alert message: {alert_message}")
        assert "Wrong password." in alert_message or "User does not exist" in alert_message
    except Exception as e:
        print("No alert message found.")
        print(e)
        assert False, "No alert message found for failed login."
