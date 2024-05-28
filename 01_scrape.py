from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os 
chromedriver_autoinstaller.install()

# Readme: This script is used to scrape a particular website and save its content to a txt.

# Input
website = "WEBSITE-URL"
wait_time = 50
num_pages = 500

# Extract the paragraph elements from the webpage
def get_paragraphs(driver):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.ID, "single-content")))
    text_body = driver.find_element(By.ID, "single-content")
    paragraph_elements = text_body.find_elements(By.TAG_NAME, "p")
    paragraphs = [p.text for p in paragraph_elements]
    return paragraphs

# Extract the title element for each webpage
def get_title(driver):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.afd-title-big.afd-title-big--full.afd-title-big--bmargin-big.afd-relativeposition")))
    title_element = driver.find_element(By.CSS_SELECTOR, "h1.afd-title-big.afd-title-big--full.afd-title-big--bmargin-big.afd-relativeposition")
    project_name = title_element.text
    filename = f"{project_name}.txt"
    valid_filename = "".join(c for c in filename if c.isalnum() or c in (' ', '_', '-')).rstrip()
    valid_filename = valid_filename.replace(" ", "_")
    directory = "scrape_data"
    filepath = os.path.join(directory, valid_filename)
    if os.path.exists(filepath):
        print(f"File already exists: {filepath}. Skipping project.")
        return None
    return valid_filename

# Navigate to the next project
def next_project(driver):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article-nav-next"]')))
    next_button = driver.find_element(By.XPATH, '//*[@id="article-nav-next"]')
    next_url = next_button.get_attribute("href")
    driver.get(next_url)

# Clean unwanted text
def clean_paragraphs(paragraphs):
    cleaned_paragraphs = []
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        # Only add paragraphs that are not empty and have 5 or more words
        if paragraph.startswith("Text description provided by the architects."):
            paragraph = paragraph.replace("Text description provided by the architects.", "").strip()
        if paragraph and len(paragraph.split()) >= 5:
            cleaned_paragraphs.append(paragraph)
    return cleaned_paragraphs

# Save the scraped text
def save_text(filepath, paragraphs):
    content = "\n\n".join(paragraphs)
    directory = "scrape_data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

# Run 
driver = webdriver.Chrome()
driver.get(website)
i = 0
while i < num_pages:
    try:
        # Get project title and check if we already scraped it
        valid_filename = get_title(driver)
        txt_file_name = valid_filename[:-3] + '.' + valid_filename[-3:]
        filepath = os.path.join("scrape_data", txt_file_name)
        if valid_filename is None or os.path.exists(filepath):
            next_project(driver)
            continue

        print(f"\nTitle: {valid_filename}")

        # Get text
        paragraphs = get_paragraphs(driver)
        paragraphs = clean_paragraphs(paragraphs)
        print(paragraphs)

        # Export to txt
        save_text(filepath, paragraphs)

        # Move to next project
        next_project(driver)
        i += 1

    except Exception as e:
        print("Error: ", e)
        break

# Close the WebDriver
driver.quit()

print("Finished scraping.")