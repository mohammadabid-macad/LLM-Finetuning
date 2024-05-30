from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
import time

chromedriver_autoinstaller.install()

# Input
website = "https://brickset.com/sets/year-2024/theme-Star-Wars"
wait_time = 10

# Extract the set details from the webpage
def get_set_details(driver, set_url):
    driver.get(set_url)
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".featurebox")))
    details_section = driver.find_element(By.CSS_SELECTOR, "section.featurebox")
    details_text = details_section.text
    return details_text

# Save the scraped data
def save_data(filename, set_details):
    directory = "scrape_data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(set_details)

# Run
driver = webdriver.Chrome()
driver.get(website)

all_set_details = []
set_links = []

# Collect set links from the main page
sets = WebDriverWait(driver, wait_time).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".set .meta h1 a")))
for s in sets:
    set_links.append(s.get_attribute("href"))

for set_link in set_links:
    try:
        print(f"Processing {set_link}")
        set_number = set_link.split('/')[-1]
        
        # Get set details
        set_details = get_set_details(driver, set_link)
        
        # Save each set's details to a file named by set number
        save_data(f"{set_number}.txt", set_details)

    except Exception as e:
        print(f"Error processing {set_link}: {e}")
        continue

# Close the WebDriver
driver.quit()

print("Finished scraping.")

