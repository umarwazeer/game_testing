from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set the path to the chromedriver executable
chromedriver_path = r'C:\Users\Umar khan\Downloads\Compressed\chromedriver_win32\chromedriver.exe'

# Set the PATH environment variable
os.environ['PATH'] += ';' + chromedriver_path

# Create the WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Open the game URL
driver.get("https://word-corners.nodehill.se/")

try:
    # Example: Start the game
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'start-btn'))
    )
    start_button.click()

    # Add more actions based on your game testing progress
    # Example: Enter a word
    input_field = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, 'word'))
    )
    input_field.send_keys("exampleword")
    input_field.send_keys(Keys.RETURN)

    # Example: Click a button or interact with other elements

finally:
    # Add any cleanup steps or close the browser window after testing
    driver.quit()
