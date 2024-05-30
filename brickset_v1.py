from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os

chromedriver_autoinstaller.install()

# Input
website = "https://brickset.com/sets/theme-Star-Wars"
wait_time = 50
num_pages = 10

# Extract the set details from the webpage
def get_set_details(driver):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".setlist")))
    sets = driver.find_elements(By.CSS_SELECTOR, ".set")
    set_details = []
    for s in sets:
        try:
            name = s.find_element(By.CSS_SELECTOR, ".meta h1 a").text
            number = s.find_element(By.CSS_SELECTOR, ".meta h1 span").text
            description = s.find_element(By.CSS_SELECTOR, ".description").text
            set_details.append((name, number, description))
        except:
            continue
    return set_details

# Save the scraped data
def save_data(filename, set_details):
    directory = "scrape_data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        for detail in set_details:
            file.write(f"Name: {detail[0]}\nNumber: {detail[1]}\nDescription: {detail[2]}\n\n")

# Run 
driver = webdriver.Chrome()
driver.get(website)
i = 0
all_set_details = []
while i < num_pages:
    try:
        print(f"Processing page {i + 1}")
        
        # Get set details
        set_details = get_set_details(driver)
        all_set_details.extend(set_details)

        # Move to the next page if it exists
        next_button = driver.find_element(By.CSS_SELECTOR, ".next")
        if next_button:
            next_button.click()
            WebDriverWait(driver, wait_time).until(EC.staleness_of(next_button))
        else:
            break
        i += 1

    except Exception as e:
        print(f"Error on page {i + 1}: {e}")
        break

# Save all set details to a file
save_data("star_wars_sets.txt", all_set_details)

# Close the WebDriver
driver.quit()

print("Finished scraping.")
