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

# try:
#     # Example: Wait for document ready state
#     WebDriverWait(driver, 120).until(
#         lambda driver: driver.execute_script('return document.readyState == "complete"')
#     )

#     # Find the file input field using its name attribute
#     file_input = WebDriverWait(driver, 120).until(
#         EC.presence_of_element_located((By.NAME, 'file'))
#     )

#     # Unhide the file input field using JavaScript
#     driver.execute_script("arguments[0].style.display = 'block';", file_input)

#     # Set the file path and send keys to the file input field
#     file_input.send_keys("path/to/your/file.txt")

#     # Continue with other actions based on your game testing progress

# finally:
#     # Add any cleanup steps or close the browser window after testing
#     driver.quit()


try:
    WebDriverWait(driver, 120).until(
    lambda driver: driver.execute_script('return document.readyState == "complete"')
    )

    # Example: Start the game
    start_button = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'start-btn'))
    )
    print("Current URL:", driver.current_url)


    start_button.click()
    

    # Add more actions based on your game testing progress
    # Example: Enter a word
    WebDriverWait(driver, 120).until(
    lambda driver: driver.execute_script('return document.readyState == "complete"')
    )
    # print("Waiting for word input field...")
    # input_field = WebDriverWait(driver, 120).until(
    #     EC.presence_of_element_located((By.NAME, 'word'))
    # )
    # print("Word input field found.")

    # input_field.send_keys("exampleword")
    # input_field.send_keys(Keys.RETURN)

    # Example: Interact with another element after submitting the word
    result_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'result-message'))
    )
    print("Result Message:", result_message.text)

    # Example: Click a button or interact with other elements

finally:
    # Add any cleanup steps or close the browser window after testing
    driver.quit()
