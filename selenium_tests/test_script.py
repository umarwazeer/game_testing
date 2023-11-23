import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os



chromedriver_path = r'C:\Users\Umar khan\Downloads\Compressed\chromedriver_win32\chromedriver.exe'


os.environ['PATH'] += ';' + chromedriver_path

# Create the WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Open the game URL
driver.get("https://word-corners.nodehill.se/")


# Wait for document ready state
WebDriverWait(driver, 60).until(
    lambda driver: driver.execute_script('return document.readyState == "complete"')
)

# Wait for the start button to be clickable
start_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'start-btn'))
)
print("Current URL:", driver.current_url)
start_button.click()

# Wait for the result message element
try:
    result_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'result-message'))
    )
    print("Result Message:", result_message.text)


except TimeoutException:
    print("Result message element not found within 10 seconds. Continuing...")
    # You can add further actions or handle the situation as needed

