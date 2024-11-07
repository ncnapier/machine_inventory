from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_hardware_specs(service_tag):
    url = f"https://www.dell.com/support/home/en-us/product-support/servicetag/{service_tag}/overview"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        # Wait for the hardware specs element to be present
        specs_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'h2'))
        )
        specs_text = specs_section.text

        # Check if the warranty element exists
        try:
            warranty_section = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'warrantyExpiringLabel'))
            )
            warranty_text = warranty_section.text
        except:
            warranty_text = "Warranty information not found."

        return specs_text, warranty_text
    except Exception as e:
        return f"An error occurred: {e}", ""
    finally:
        driver.quit()

# Get the service tags from user input
service_tags = input("Enter the service tags separated by commas: ").split(',')

results = []
for tag in service_tags:
    tag = tag.strip().upper()  # Remove any leading/trailing whitespace
    specs, warranty = get_hardware_specs(tag)
    results.append(f"Service Tag: {tag}, Computer: {specs}, Exp: {warranty}")

# Print the results
for result in results:
    print(result)