from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.demoblaze.com")

    login_button = driver.find_element(By.ID, "login2")
    login_button.click()
    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginusername")))
    username_input = driver.find_element(By.ID, "loginusername")
    username_input.send_keys("Aashitha")
    time.sleep(2)

    password_input = driver.find_element(By.ID, "loginpassword")
    password_input.send_keys("ash")
    time.sleep(2)

    login_submit = driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']")
    login_submit.click()

    time.sleep(10)  

    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Samsung galaxy s6")))
    product_link = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")

    if product_link:
        product_link.click()
    else:
        print("Product link not found!")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.btn.btn-success.btn-lg")))

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-success.btn-lg")
    add_to_cart_button.click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    
    cart_link = driver.find_element(By.ID, "cartur")
    cart_link.click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-success")))

    place_order_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
    place_order_button.click()
    time.sleep(2)

    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
    driver.find_element(By.ID, "name").send_keys("Aashitha")
    time.sleep(2)
    driver.find_element(By.ID, "country").send_keys("India")
    time.sleep(2)
    driver.find_element(By.ID, "city").send_keys("Bangalore")
    time.sleep(2)
    driver.find_element(By.ID, "card").send_keys("1234567890")
    time.sleep(2)
    driver.find_element(By.ID, "month").send_keys("12")
    time.sleep(2)
    driver.find_element(By.ID, "year").send_keys("2024")
    time.sleep(2)

    purchase_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='purchaseOrder()']")
    purchase_button.click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible h2")))
    confirmation_message = driver.find_element(By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible h2").text
    print("Order Confirmation: " + confirmation_message)
    time.sleep(10)

finally:
    driver.quit()