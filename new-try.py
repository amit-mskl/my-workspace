from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Task 1: Ask the user for the project_id from prompt
project_id = input("Please enter the project_id: ")

# Task 2: Go to link: app.enqurious.com/<project_id>
url = f"https://app.enqurious.com/projects/{project_id}"

# Task 3: Search for input: Email and enter the username
username = "mentorskool1@gmail.com"
password = "mentorskool1@gmail.com_password"

# Task 4: Click on the "Deploy" button in the project page
intent = "Select Learning"
description = "For learning purpose"
start_date = str(int(time.time()))
end_date = str(int(time.time()) + 604800)  # 1 week later
service = Service(executable_path='G:/My Drive/research/experiments/amit-work/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # Task 2: Go to link: app.enqurious.com/<project_id>
    driver.get(url)

    # Task 3: Search for input: Email and enter the username
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(username)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(20)

    # Task 4: Once logged into the project page, look for the "Deploy" button and click on it
    deploy_button = driver.find_element(By.NAME, "Deploy")
    deploy_button.click()

    # Task 5: Fill up the details in the modal that appears
    intent_input = driver.find_element(By.NAME, "Intent")
    intent_input.send_keys(intent)

    description_input = driver.find_element(By.NAME, "Description")
    description_input.send_keys(description)

    start_date_input = driver.find_element(By.NAME, "Start_date")
    start_date_input.send_keys(start_date)

    end_date_input = driver.find_element(By.NAME, "End_date")
    end_date_input.send_keys(end_date)

    next_button = driver.find_element(By.NAME, "Next")
    next_button.click()

    # Task 6: End
    print("Task completed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
