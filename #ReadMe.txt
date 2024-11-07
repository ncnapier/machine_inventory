# Hardware Specifications and Warranty Information Script

This script retrieves hardware specifications and warranty information for Dell devices using their service tags. The results are saved to an Excel spreadsheet.

## Prerequisites

- Windows operating system
- Internet connection
- Google Chrome Installed 

## Step-by-Step Guide

### 1. Download and Install Python

1. Open Command Prompt (cmd) and download the latest version of Python from the official website:
    
    curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
    

2. Run the installer:
   
    python-installer.exe
    

3. During installation, make sure to check the box that says "Add Python to PATH".

### 2. Install Dependencies

1. Open PowerShell and navigate to the directory where the script is located. For example:
    
    cd C:\path\to\your\script
   

2. Install the required Python packages using `pip`:
  
    pip install selenium webdriver-manager openpyxl
    

### 3. Run the Script

1. In PowerShell, navigate to the directory where the script is located if you haven't already:
    
    cd C:\path\to\your\script
    

2. Run the script:
    
    python your_script_name.py
   

### 4. Follow the Prompts

1. The script will prompt you to enter the location. This will be used in the name of the Excel file.
2. Enter the room number and the associated service tags separated by commas.
3. The script will ask if there is another room. If yes, repeat the process for the next room.
4. Once you have entered all rooms and service tags, the script will retrieve the hardware specifications and warranty information for each service tag.
5. The results will be saved to an Excel file named `hardware_specs_<location>.xlsx`.

### Example


Enter the location: OfficeA
Enter the room number: 101
Enter the service tags for room 101 separated by commas: ABC123, DEF456
Is there another room? (yes/no): yes
Enter the room number: 102
Enter the service tags for room 102 separated by commas: GHI789, JKL012
Is there another room? (yes/no): no