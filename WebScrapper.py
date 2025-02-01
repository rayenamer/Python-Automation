from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    """Initialize and return a Chrome WebDriver instance with options."""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only the temperature from text."""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    driver.find_element("id", "id_username").send_keys("automated")
    driver.find_element("id", "id_password").send_keys("automatedautomated" + Keys.RETURN)

    # Wait for login success
    time.sleep(2)  

    # Verify login by checking URL or element presence
    if driver.current_url:  
        driver.find_element("xpath", "/html/body/nav/div/a").click()
        print(driver.current_url)
    else:
        print("Login failed. Check credentials or site status.")

    driver.quit()

if __name__ == "__main__":
    main()
