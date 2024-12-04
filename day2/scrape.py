import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL of the website
url = 'https://www.gsa-spark.com/speedtest/391cdbb6-1640-4d40-a8c2-323404f3b459'  # Replace with the actual URL

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in your PATH
driver.get(url)

# Wait for the page to load
# time.sleep(1)

# Scrape the page content
page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')

# Find the sum question (assuming it's in a specific element, e.g., <div id="sum-question">)
number1 = int(soup.find('span', id='number1').text)
number2 = int(soup.find('span', id='number2').text)


# Extract the numbers from the question

# Calculate the sum
result = number1 + number2

# Find the input field and submit the answer (assuming the input field has id="answer")
answer_input = driver.find_element(By.ID, 'answer')
answer_input.send_keys(str(result))
answer_input.send_keys(Keys.RETURN)

# Wait for the result to be processed
time.sleep(2)

# Optionally, you can scrape the result or take further actions here

# Close the browser

driver.quit()