from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import re
from datetime import datetime

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

            # Extract the date from the warranty text and format it as mm/dd/yyyy
            match = re.search(r'Ending (\d{1,2} \w{3} \d{4})', warranty_text)
            if match:
                date_str = match.group(1)
                date_obj = datetime.strptime(date_str, '%d %b %Y')
                warranty_text = date_obj.strftime('%m/%d/%Y')
            else:
                warranty_text = "Warranty information not found."
        except:
            warranty_text = "Warranty information not found."

        return specs_text, warranty_text
    except Exception as e:
        return f"An error occurred: {e}", ""
    finally:
        driver.quit()

# Get the location from user input
location = input("Enter the location: ")

# Initialize a list to store all room information
all_rooms = []

while True:
    # Get the room number from user input
    room_number = input("Enter the room number: ")

    # Get the service tags from user input for the current room
    service_tags = input(f"Enter the service tags for room {room_number} separated by commas: ").split(',')

    # Store the room number and associated service tags
    all_rooms.append((room_number, service_tags))

    # Ask if there is another room
    another_room = input("Is there another room? (yes/no): ").strip().lower()
    if another_room != 'yes':
        break

# Initialize a list to store all results
all_results = []

# Process each room and its service tags
for room_number, service_tags in all_rooms:
    # Process each service tag for the current room
    for i, tag in enumerate(service_tags):
        tag = tag.strip()  # Remove any leading/trailing whitespace
        specs, warranty = get_hardware_specs(tag)
        machine_number = i + 1  # Machine number corresponds to the sequence of entry
        formatted_location = f"{location}_{room_number}_{machine_number}"
        all_results.append([tag, specs, formatted_location, "", "", "", "", "", warranty])

# Print the results to console
for result in all_results:
    print(result)

# Create a new Excel workbook and add a worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Set the headers for the first row
headers = ["CI", "Model", "Location", "Application", "Serial_Number", "Options Pack", "Request Code", "Activation Key", "Life Cycle Date"]
ws.append(headers)

# Add the results to the worksheet
for result in all_results:
    ws.append(result)

# Save the workbook to a file with location in the name
file_name = f"hardware_specs_{location}.xlsx"
wb.save(file_name)
print(f"Results have been saved to {file_name}")