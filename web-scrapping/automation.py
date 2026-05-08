import os
import time
import schedule
from bs4 import BeautifulSoup
from openpyxl import Workbook

def scrape_and_export():
    print("Executing job: Parsing HTML and generating Excel...")
    
    file_path = 'data.html'
    
    # Safely check if the target file exists in the current directory
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found in the current directory.")
        return

    # 1. Parse the HTML file with Beautiful Soup
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Locate the table by its ID
    table = soup.find('table', id='workout-table')
    if not table:
        print("Error: Could not find the table in the HTML.")
        return
        
    # Find all rows in the table
    rows = table.find_all('tr')
    
    # 2. Initialize openpyxl Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Extracted HTML Data"
    
    # 3. Iterate through HTML rows and append to Excel
    for row in rows:
        # Extract both headers (th) and standard cells (td)
        columns = row.find_all(['th', 'td'])
        
        # Clean the text and create a list representing the row data
        row_data = [col.text.strip() for col in columns]
        
        # Write the row to the Excel sheet
        ws.append(row_data)
        
    # 4. Save the Workbook
    output_filename = 'Scheduled_Extraction.xlsx'
    wb.save(output_filename)
    print(f"Success! Data saved to {output_filename}\n")


# --- SCHEDULING LOGIC ---

# Option A: Run immediately once to verify it works
scrape_and_export()

# Option B: Schedule for a specific time every day
schedule.every().day.at("09:00").do(scrape_and_export)

# Option C: For testing purposes, uncomment the line below to run every 10 seconds
# schedule.every(10).seconds.do(scrape_and_export)

print("Automated scheduler is now active. Press Ctrl+C to stop.")

# The infinite loop that keeps the script alive to run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1) # Sleep for 1 second to prevent maxing out the CPU