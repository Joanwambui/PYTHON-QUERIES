from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time

# Load credentials from YAML file
conf = yaml.safe_load(open('secretpasswords.yml'))
username = conf['max_user']['Username']
password = conf['max_user']['Password']

# Initialize the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def login(url):
    # Open the URL
    driver.get(url)
    
    # Find elements and interact with them
    driver.find_element(By.ID, "ext-comp-1001").send_keys(username)
    driver.find_element(By.ID, "ext-comp-1002").send_keys(password)
    driver.find_element(By.ID, "ext-gen23").click()

def expand_survey_section():
    # Wait for the left pane to load (adjust sleep time if necessary or use WebDriverWait)
    time.sleep(3)
    
    # Locate the 7th "+" button using XPath
    seventh_plus_button = driver.find_element(
        By.XPATH, "(//img[contains(@class, 'x-tree-ec-icon') and contains(@class, 'x-tree-elbow-plus')])[6]"
    )
    
    # Click on the 6th "+" button
    seventh_plus_button.click()
    
    print("7th '+' button clicked, and the survey section expanded!")

# Example execution
login("https://portal.visi")
expand_survey_section()